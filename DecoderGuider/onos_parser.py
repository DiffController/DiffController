import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scapy.all import *
from OpenFlowProxy.proxy import Channel
from OpenFlowProxy.proxy import strategy_process,OpenFlow_type,sub_type
from jpype import JByte,JArray
import jpype

matched_flag = False

# type conversion : python byte list to Java byte[]
def to_byte_array(para):
    
    return JArray(JByte)(para)

def to_byte(para):
    return JByte(para)

# python bytes to [byte,byte,......]
def bytes_to_list(para):
    byte_list = list(para)
    new_byte_list = []
    for byte in byte_list:
        if byte >= 128:
            new_byte_list.append(byte-256)
        else:
            new_byte_list.append(byte)
    return new_byte_list

# convert python pkt seq to java pkt seq
def pkt_seq_to_openflowj(processed_list):
    java_pkt_seq = [] 
    for pkt in processed_list:
        pkt_byte_list = bytes_to_list(pkt)
        pkt_Jarray = to_byte_array(pkt_byte_list)
        java_pkt_seq.append(pkt_Jarray)
    return java_pkt_seq

class TestOfproto_Parser():
    def testOpenFlow(self,processed_list):
        result = []
        java_pkt_seq = pkt_seq_to_openflowj(processed_list)
        try:
            for pkt in java_pkt_seq:
                javaClass = jpype.JClass("org.onosproject.onosopenflowtest.onos_openflowj_test")
                javaInstance = javaClass()
                decoder_result = javaInstance.OpenFlowMsgDecoder(pkt)
                result = ("succeed","")
        except Exception as e:
            result = ("fail",e.__class__.__name__)
        finally:
            global matched_flag
            matched_flag = False
            return result

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

"DELAY action does not affect the result of decoder parsing"
def onos_decoder_parsered_result(pcap_path,strategy_str):
    result = []
    test = TestOfproto_Parser()
    pkt_list = rdpcap(pcap_path)
    channel = Channel(None,None,None,None,None)
    processed_list = []
    strategy = strategy_process(strategy_str)
    strategy = del_delay_action(strategy)
    processed_list = packet_list_process(channel,strategy,pkt_list)
    return test.testOpenFlow(processed_list)

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