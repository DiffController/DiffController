"""
OpenFlow parser module

This module provides methods to decode OpenFlow messages.
This hides various external OpenFlow modules to ofcaputure.
"""
import os
import sys
pyloxi_project = 'pyloxi3' 
sys.path.append(os.getcwd() +"/"+ pyloxi_project)
from loxi import of13 as ofp

from enum import Enum

from pyof.foundation.base import GenericMessage, UBIntBase, GenericBitMask, GenericType
from pyof.v0x04.common.header import Header
from pyof.v0x04.common.utils import unpack_message, new_message_from_header, MESSAGE_TYPES
from ofproto.packet import OFMsg

def parse(msg, logger=None):
    """parse OpenFlow message

    Args:
        msg (Message) :
        logger (Logger) :

    Returns:
        list[Message]

    """
    msgs = []
    
    try:
        header = ofp.message.parse_header(msg.data)
        header_len = header[2] 
        data = msg.data[:int(header_len)]
        rest = msg.data[int(header_len):]
        msg.data = data

        of_msg = ofp.message.parse_message(msg.data)
        msg.of_msg = of_msg
        msgs.append(msg)

        if logger:
            logger.info("Parsed msg : {}(xid={}) ".format(msg.msg_name, of_msg.xid))

        if len(rest) > 0:
            msg_rest = OFMsg(msg.timestamp, msg.local_ip, msg.remote_ip, msg.local_port, msg.remote_port,
                             rest, msg.switch2controller)
            rest_msgs = parse(msg_rest, logger=logger)
            msgs.extend(rest_msgs)

        return msgs
    except Exception as e:
        if msg.of_msg is not None:
            msg_name = msg.of_msg.msg_name
            if logger:
                logger.error("Failed to unpack msg({}) : {}".format(msg_name, str(e)))
    return []


def get_header(msg):
    header = Header()
    header.unpack(msg.data[:header.get_size()])
    return header
