import binascii
import struct
from scapy.all import *

from ryu.ofproto import ofproto_common,ofproto_parser
from ryu.ofproto import ofproto_v1_0, ofproto_v1_0_parser

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from OpenFlowProxy.proxy import Channel
from OpenFlowProxy.proxy import strategy_process,OpenFlow_type,sub_type

import logging
LOG = logging.getLogger(__name__)

matched_flag = False

class TestOfproto_Parser():
    def setUp(self):
        LOG.debug('setUp')
        self.bufHello = binascii.unhexlify('0100000800000001')
        fr = '010600b0000000020000000000000abc' \
            + '00000100010000000000008700000fff' \
            + '0002aefa39d2b9177472656d61302d30' \
            + '00000000000000000000000000000000' \
            + '000000c0000000000000000000000000' \
            + 'fffe723f9a764cc87673775f30786162' \
            + '63000000000000000000000100000001' \
            + '00000082000000000000000000000000' \
            + '00012200d6c5a1947472656d61312d30' \
            + '00000000000000000000000000000000' \
            + '000000c0000000000000000000000000'
        self.bufFeaturesReply = binascii.unhexlify(fr)
        pi = '010a005200000000000001010040' \
            + '00020000000000000002000000000001' \
            + '080045000032000000004011f967c0a8' \
            + '0001c0a8000200010001001e00000000' \
            + '00000000000000000000000000000000' \
            + '00000000'
        self.bufPacketIn = binascii.unhexlify(pi)
    
    def equal(self,parsed_value,except_value):
        if parsed_value == except_value:
            return True
        else:
            return False


    def tearDown(self):
        LOG.debug('tearDown')
        pass

    def testHello(self):
        (version,
         msg_type,
         msg_len,
         xid) = ofproto_parser.header(self.bufHello)

        print(self.equal(version, 1))
        print(self.equal(msg_type, 0))
        print(self.equal(msg_len, 8))
        print(self.equal(xid, 1))

    def testFeaturesReply(self):
        (version,
         msg_type,
         msg_len,
         xid) = ofproto_parser.header(self.bufFeaturesReply)

        msg = ofproto_parser.msg(self,
                                 version,
                                 msg_type,
                                 msg_len,
                                 xid,
                                 self.bufFeaturesReply)
        LOG.debug(msg)
        print(isinstance(msg, ofproto_v1_0_parser.OFPSwitchFeatures))
        LOG.debug(msg.ports[65534])
        print(isinstance(msg.ports[1], ofproto_v1_0_parser.OFPPhyPort))
        print(isinstance(msg.ports[2], ofproto_v1_0_parser.OFPPhyPort))
        print(isinstance(msg.ports[65534], ofproto_v1_0_parser.OFPPhyPort))

    def testPacketIn(self):
        (version,
         msg_type,
         msg_len,
         xid) = ofproto_parser.header(self.bufPacketIn)

        msg = ofproto_parser.msg(self,
                                 version,
                                 msg_type,
                                 msg_len,
                                 xid,
                                 self.bufPacketIn)
        LOG.debug(msg)
        print(isinstance(msg, ofproto_v1_0_parser.OFPPacketIn))

    def testOpenFlow(self,raw_packet):
        (version,msg_type,msg_len,xid) = ofproto_parser.header(raw_packet)
        msg = ofproto_parser.msg(self,version,msg_type,msg_len,xid,raw_packet)
        return msg

# process the packet sequence using strategy
def packet_list_process(default_channel,strategy,pkt_list):
    global matched_flag
    processed_list = []

    for pkt in pkt_list:
        scapy_openflow_pkt = pkt.payload.payload.payload
        raw_pkt = bytes(scapy_openflow_pkt)
        msg_type = raw_pkt[1]
        if not matched_flag:
            if OpenFlow_type[msg_type] == "of_multipart_reply":
                sub_type_field = int.from_bytes(raw_pkt[8:10],"big")
                if strategy.pkt_type == sub_type[sub_type_field]:
                    processed_data = default_channel.action_switch_case(strategy,raw_pkt,raw_pkt)
                    processed_list.append(processed_data)
                    matched_flag = True
                else:
                    processed_list.append(raw_pkt)
            elif OpenFlow_type[msg_type] == strategy.pkt_type:
                processed_data = default_channel.action_switch_case(strategy,raw_pkt,raw_pkt)
                processed_list.append(processed_data)
                matched_flag = True
            else:
                processed_list.append(raw_pkt)
        else:
            processed_list.append(raw_pkt)
    processed_list = packet_split(processed_list)
    return processed_list

# split the packet sequece processed by strategy
def packet_split(processed_list):
    new_processed_list = []
    for pkt in processed_list:
        split_list = []
        data_split(pkt,split_list)
        for item in split_list:
            new_processed_list.append(item)
    return new_processed_list

# split multiple openflow msg in one packet 
def data_split(data,data_list):
    if len(data)!=0:
        length_bytes = data[2:4]
        length = int.from_bytes(length_bytes,"big")
        """filter table feature msg"""
        if len(data) > length and len(data) < 1000:
            of_msg = data[0:length]
            remain_data = data[length:]
            data_list.append(of_msg)
            data_split(remain_data,data_list)
        else:
            """don't split"""
            data_list.append(data)

def ryu_decoder_parsered_result(pcap_path,strategy_str):
    result = []
    test = TestOfproto_Parser()
    test.setUp()
    pkt_list = rdpcap(pcap_path)
    channel = Channel(None,None,None,None,None)
    processed_list = []
    strategy = strategy_process(strategy_str)
    strategy = del_delay_action(strategy)
    processed_list = packet_list_process(channel,strategy,pkt_list)
    parsed_ofmsg = []
    try:
        for pkt in processed_list:
            openflow_msg = test.testOpenFlow(pkt)
            parsed_ofmsg.append(openflow_msg)
        result = ("succeed","")
        for ofmsg in parsed_ofmsg:
            if ofmsg.__class__.__name__ == "NoneType":
                result = ("fail","NoneType")
    except Exception as e:
        result = ("fail",e.__class__.__name__)
    finally:
        global matched_flag
        matched_flag = False
        return result

"DELAY action does not affect the result of decoder parsing"
def del_delay_action(strategy):
    action_list_str = strategy.action
    action_list = action_list_str.split("|")
    del_index = None
    for index in range(0,len(action_list),1):
        action_type = action_list[index].split(",",1)[0]
        if action_type == "DELAY":
            del_index = index
    if del_index is not None:
        del action_list[del_index]
    strategy.action = "|".join(action_list)
    return strategy