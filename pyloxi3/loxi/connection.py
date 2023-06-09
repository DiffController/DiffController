# Copyright 2015, Big Switch Networks, Inc.

"""
OpenFlow connection class

This class creates a thread which continually parses OpenFlow messages off the
supplied socket and places them in a queue. The class has methods for reading messages
from the RX queue, sending messages, and higher level operations like request-response
and multipart transactions.
"""

import loxi
import loxi.of14
import logging
import time
import socket
import errno
import os
import select
from threading import Condition, Lock, Thread

DEFAULT_TIMEOUT = 1

class TransactionError(Exception):
    def __str__(self):
        return self.args[0]

    @property
    def msg(self):
        return self.args[1]

class Connection(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock
        self.logger = logging.getLogger("connection")
        self.rx = []
        self.rx_cv = Condition()
        self.tx_lock = Lock()
        self.next_xid = 1
        self.wakeup_rd, self.wakeup_wr = os.pipe()
        self.finished = False
        self.read_buffer = None

    def run(self):
        while not self.finished:
            rd, wr, err = select.select([self.sock, self.wakeup_rd], [], [])
            if self.sock in rd:
                self.process_read()
            if self.wakeup_rd in rd:
                os.read(self.wakeup_rd, 1)
        self.logger.debug("Exited event loop")

    def process_read(self):
        recvd = self.sock.recv(4096)

        self.logger.debug("Received %d bytes", len(recvd))

        buf = self.read_buffer
        if buf:
            buf += recvd
        else:
            buf = recvd

        offset = 0
        while offset < len(buf):
            if offset + 8 > len(buf):
                # Not enough data for the OpenFlow header
                break

            # Parse the header to get type
            hdr_version, hdr_type, hdr_msglen, hdr_xid = loxi.of14.message.parse_header(buf[offset:])

            # Use loxi to resolve ofp of matching version
            ofp = loxi.protocol(hdr_version)

            # Extract the raw message bytes
            if (offset + hdr_msglen) > len(buf):
                # Not enough data for the body
                break
            rawmsg = buf[offset : offset + hdr_msglen]
            offset += hdr_msglen

            msg = ofp.message.parse_message(rawmsg)
            if not msg:
                self.logger.warn("Could not parse message")
                continue

            self.logger.debug("Received message %s.%s xid %d length %d",
                              type(msg).__module__, type(msg).__name__, hdr_xid, hdr_msglen)

            with self.rx_cv:
                self.rx.append(msg)
                self.rx_cv.notify_all()

        if offset == len(buf):
            self.read_buffer = None
        else:
            self.read_buffer = buf[offset:]
            self.logger.debug("%d bytes remaining", len(self.read_buffer))

    def recv(self, predicate, timeout=DEFAULT_TIMEOUT):
        """
        Remove and return the first message in the RX queue for
        which 'predicate' returns true
        """
        assert self.is_alive()

        deadline = time.time() + timeout
        while True:
            with self.rx_cv:
                for i, msg in enumerate(self.rx):
                    if predicate(msg):
                        return self.rx.pop(i)

                now = time.time()
                if now > deadline:
                    return None
                else:
                    self.rx_cv.wait(deadline - now)

    def recv_any(self, timeout=DEFAULT_TIMEOUT):
        """
        Return the first message in the RX queue
        """
        return self.recv(lambda msg: True, timeout)

    def recv_xid(self, xid, timeout=DEFAULT_TIMEOUT):
        """
        Return the first message in the RX queue with XID 'xid'
        """
        return self.recv(lambda msg: msg.xid == xid, timeout)

    def recv_class(self, klass, timeout=DEFAULT_TIMEOUT):
        """
        Return the first message in the RX queue which is an instance of 'klass'
        """
        return self.recv(lambda msg: isinstance(msg, klass), timeout)

    def send_raw(self, buf):
        """
        Send raw bytes on the socket
        """
        assert self.is_alive()
        self.logger.debug("Sending raw message length %d", len(buf))
        with self.tx_lock:
            if self.sock.sendall(buf) is not None:
                raise RuntimeError("failed to send message to switch")

    def send(self, msg):
        """
        Send a message
        """
        assert self.is_alive()

        if msg.xid is None:
            msg.xid = self._gen_xid()
        buf = msg.pack()
        self.logger.debug("Sending message %s.%s xid %d length %d",
                          type(msg).__module__, type(msg).__name__, msg.xid, len(buf))
        with self.tx_lock:
            if self.sock.sendall(buf) is not None:
                raise RuntimeError("failed to send message to switch")

    def transact(self, msg, timeout=DEFAULT_TIMEOUT):
        """
        Send a message and return the reply
        """
        self.send(msg)
        reply = self.recv_xid(msg.xid, timeout)
        if reply is None:
            raise TransactionError("no reply for %s" % type(msg).__name__, None)
        elif isinstance(reply, loxi.protocol(reply.version).message.error_msg):
            raise TransactionError("received %s in response to %s" % (type(reply).__name__, type(msg).__name__), reply)
        return reply

    def transact_multipart_generator(self, msg, timeout=DEFAULT_TIMEOUT):
        """
        Send a multipart request and yield each entry from the replies
        """
        self.send(msg)
        finished = False
        while not finished:
            reply = self.recv_xid(msg.xid, timeout)
            if reply is None:
                raise TransactionError("no reply for %s" % type(msg).__name__, None)
            elif not isinstance(reply, loxi.protocol(reply.version).message.stats_reply):
                raise TransactionError("received %s in response to %s" % (type(reply).__name__, type(msg).__name__), reply)
            for entry in reply.entries:
                yield entry
            finished = reply.flags & loxi.protocol(reply.version).OFPSF_REPLY_MORE == 0

    def transact_multipart(self, msg, timeout=DEFAULT_TIMEOUT):
        """
        Send a multipart request and return all entries from the replies
        """
        entries = []
        for entry in self.transact_multipart_generator(msg, timeout):
            entries.append(entry)
        return entries

    def stop(self):
        """
        Signal the thread to exit and wait for it
        """
        assert not self.finished
        self.logger.debug("Stopping connection")
        self.finished = True
        os.write(self.wakeup_wr, b"x")
        self.join()
        self.sock.close()
        os.close(self.wakeup_rd)
        os.close(self.wakeup_wr)
        self.logger.debug("Stopped connection")

    def _gen_xid(self):
        xid = self.next_xid
        self.next_xid += 1
        return xid

def connect(ip, port=6653, daemon=True, ofp=loxi.of14):
    """
    Actively connect to a switch
    """
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip, port))
    soc.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
    cxn = Connection(soc)
    cxn.daemon = daemon
    cxn.logger.debug("Connected to %s:%d", ip, port)
    cxn.start()

    cxn.send(ofp.message.hello())
    if not cxn.recv(lambda msg: msg.type == ofp.OFPT_HELLO):
        raise Exception("Did not receive HELLO")

    return cxn

def connect_unix(path, daemon=True, ofp=loxi.of14):
    """
    Connect over a unix domain socket
    """
    soc = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    soc.connect(path)
    cxn = loxi.connection.Connection(soc)
    cxn.daemon = daemon
    cxn.logger.debug("Connected to %s", path)
    cxn.start()

    cxn.send(ofp.message.hello())
    if not cxn.recv(lambda msg: msg.type == ofp.OFPT_HELLO):
        raise Exception("Did not receive HELLO")

    return cxn
