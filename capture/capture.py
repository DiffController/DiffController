"""
Capture App
"""

import os
import sys
pyloxi_project = 'pyloxi3'
sys.path.append(os.getcwd() +"/"+ pyloxi_project)
from loxi import of13 as ofp

from pyof.foundation.basic_types import DPID
from pyof.v0x04.common.header import Type
from pyof.v0x04.controller2switch.common import MultipartType

from OpenFlowProxy.observer import OFObserver
from capture.of_msg_repository import packet_in_out_repo
from ofproto.packet import OFMsg
from ofproto.datapath import Port, Datapath
from ofproto.packet import todict

class CaptureBase(OFObserver):
    """CaptureBase

    This is a base class for saving messages to a repository or output to stdout.
    """

    def __init__(self, observable, do_capture=True,logger_name=""):
        super(CaptureBase, self).__init__(observable,logger_name)
        # local port to datapath id mapping
        self.lport_to_dpid = {}
        # local port to port obj mapping
        self.lport_to_port = {}

        # all captured messages
        self._messages = []
        self.do_capture = do_capture

        # datapathes
        self._datapathes: list[Datapath] = []

        # handlers
        self.handlers = {}

    def update(self, msg):
        """handle msg

        * this method called by observable

        Args:
            msg (OFMsg) : openflow message object
        """
        # datapthes
        datapath = self._get_datapath(msg.local_port)
        if datapath is None:
            datapath = Datapath()
            datapath.local_port = msg.local_port
            self._datapathes.append(datapath)
        
        # set datapathid
        if msg.of_msg.type == ofp.message.features_reply.type:
            # set datapath id (and check the dpid format)
            """
            if isinstance(msg.of_msg.datapath_id, DPID):
                datapath_id = int(''.join(msg.of_msg.datapath_id.value.split(':')), 16)
                self.lport_to_dpid[msg.local_port] = datapath_id
                datapath.datapath_id = datapath_id
            """
            # in pyloxi., we need not to parse datapath id again
            datapath_id = msg.of_msg.datapath_id
            self.lport_to_dpid[msg.local_port] = datapath_id
            datapath.datapath_id = datapath_id



        # set port obj
        elif msg.of_msg.type == ofp.message.port_desc_stats_reply.type and msg.of_msg.stats_type == ofp.message.port_desc_stats_reply.stats_type:
                # Note: OFPMP_PORT_DESC message body is a list of port
                port_list = []
                for p in msg.of_msg.entries:
                    port_list.append(Port.from_dict(todict(p)))
                self.lport_to_port[msg.local_port] = port_list
                datapath.ports = port_list

        # update msg datapath id (before FeaturesReply)
        if msg.local_port in self.lport_to_dpid.keys():
            msg.datapath_id = self.lport_to_dpid[msg.local_port]

        if self.do_capture:
            self._messages.append(msg)

        # notify subclass
        self.msg_handler(msg)

    def msg_handler(self, msg):
        if msg.message_type in self.handlers.keys():
            self.handlers[msg.message_type](msg)
        if "*" in self.handlers.keys():
            self.handlers["*"](msg) 

    def get_datapathid(self, local_port):
        """get datapath id

        Args:
            local_port (int) : local port

        Returns:
            int or None : datapath id
        """
        if local_port in self.lport_to_dpid.keys():
            return self.lport_to_dpid[local_port]
        else:
            return None   

    def _get_datapath(self, local_port: int):
        datapath = None
        for d in self._datapathes:
            if d.local_port == local_port:
                datapath = d
                break
        return datapath

    def get_port(self, datapath_id):
        """get local port of datapath

        Args:
            datapath_id (int or string) : Datapath ID that can be converted to int.

        Returns:
            int or None : local port
        """
        if not isinstance(datapath_id, int):
            datapath_id = int(datapath_id)
        for p, d in self.lport_to_dpid.items():
            if d == datapath_id:
                return p
        return None

    def get_port_name(self, local_port, port_no):
        """get port name from port number
        """
        for port in self.lport_to_port[local_port]:
            if int(port_no) == port_no:
                return port.name
        return None

    def __str__(self):
        msgs = ""
        for msg in self._messages:
            datapathid = self.get_datapathid(msg.local_port)
            order = "switch(dpid={}) -> controller".format(datapathid)
            if not msg.switch2controller:
                order = "controller -> switch(dpid={})".format(datapathid)
            msg_name = "{}(xid={})".format(msg.msg_name, msg.xid)

            msgs += "{} {} {} \n".format(msg.datetime, order, msg_name)
        return msgs

class SimpleCapture(CaptureBase):

    def __init__(self, observable,logger_name):
        super(SimpleCapture, self).__init__(observable,logger_name=logger_name)