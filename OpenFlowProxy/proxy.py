"""Proxy Module"""
import sys
import os
import time
import re
import json

import asyncio
from datetime import datetime
from logging import getLogger, Logger

from ofproto.packet import OFMsg
import threading

from generation.StrategyGenerator import Strategy
from OpenFlowProxy.build_operation import build_msg
from OpenFlowProxy.common_struct_util import entries_struct_del_process, entries_struct_process, is_number, match_struct_add_process, match_struct_del_process, match_struct_process,flow_struct_add_process,entries_struct_add_process, string_to_bytes
pyloxi_project = 'pyloxi3'
sys.path.append(os.getcwd() +"/"+ pyloxi_project)
from loxi import ProtocolError, of13 as ofp
from RestAPP.RyuRESTAPP import RyuInfo
from RestAPP.RyuRESTAPP import switch_url as ryu_switch_url 
from RestAPP.FloodlightRESTAPP import FLInfo
from RestAPP.FloodlightRESTAPP import switch_url as fl_switch_url 
from RestAPP.OnosRESTAPP import OnosInfo
from RestAPP.ODLRESTAPP import ODLInfo


OpenFlow_type = ["of_hello","of_error","of_echo_request","of_echo_reply","of_experimenter",
                "of_features_request","of_features_reply","of_get_config_request","of_get_config_reply","of_set_config",
                "of_packet_in","of_flow_removed","of_port_status","of_packet_out","of_flow_mod",
                "of_group_mod","of_port_mod","of_table_mod","of_multipart_request","of_multipart_reply",
                "of_barrier_request","of_barrier_reply","of_get_config_request","of_get_config_reply","of_role_request",
                "of_role_reply","of_async_get_request","of_async_get_reply","of_async_set","of_meter_mod"
                ]

sub_type = ["of_desc_stats_reply","of_flow_stats_reply","of_aggregate_stats_reply","of_table_stats_reply","of_port_stats_reply",
            "of_queue_stats_reply","of_group_stats_reply","of_group_desc_stats_reply","of_group_features_stats_reply","of_meter_stats_reply",
            "of_meter_config_stats_reply","of_meter_features_stats_reply","of_table_features_stats_reply","of_port_desc_stats_reply"
            ]


# global var

strategy_str = ""
strategy = Strategy()

# test case only exec once for all controller
exec_flag = False

# test case exec flag for each controller
ryu_exec_flag = False
fl_exec_flag = False
onos_exec_flag = False
odl_exec_flag = False

# represent test case has been exection
exec_finished_flag = False
executing_flag = False
flag_before_test = ""
compare_different_controller = False

same_message_process_flag = True

lock = asyncio.Lock()

"""global info for each controller"""
flinfo = FLInfo()
ryuinfo = RyuInfo()
onosinfo = OnosInfo()
odlinfo = ODLInfo()

def come_back_to_init_state():
    global strategy_str,strategy,exec_flag,ryu_exec_flag,fl_exec_flag,onos_exec_flag,odl_exec_flag,exec_finished_flag
    global executing_flag,same_message_process_flag,flinfo,ryuinfo,onosinfo,odlinfo,flag_before_test,compare_different_controller
    strategy_str = ""
    strategy = Strategy()
    exec_flag = False
    ryu_exec_flag = False
    fl_exec_flag = False
    onos_exec_flag = False
    odl_exec_flag = False
    exec_finished_flag = False
    executing_flag = False
    same_message_process_flag = True
    flag_before_test = ""
    compare_different_controller = False
    same_message_process_flag = True
    flinfo = FLInfo()
    ryuinfo = RyuInfo()
    onosinfo = OnosInfo()
    odlinfo = ODLInfo()

# reverse replace
def rreplace(self, old, new, *max):
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0] 
        while count:
            index = self.rfind(old)
            if index >= 0:
                chunk = self.rpartition(old)
                self = chunk[0] + new + chunk[2] 
                count -= 1
    return self

"strategy(str) --> strategy(Strategy Object)"
def strategy_process(strategy_str):
    strategy = Strategy()
    strategy_str = strategy_str.replace('[', '',1) 
    strategy_str = rreplace(strategy_str,']','',1)
    strategy_slice = strategy_str.split(",",maxsplit=3)
    strategy.priority = strategy_slice[0]
    strategy.pkt_type = strategy_slice[1]
    strategy.field = strategy_slice[2]
    action_list_str = strategy_slice[3]
    strategy.action = action_list_str
    return strategy

def start_loop(thread_loop):
    asyncio.set_event_loop(thread_loop)
    thread_loop.run_forever()

def msg_length_extract(header):
    length_bytes = header[2:4]
    length = int.from_bytes(length_bytes,"big")
    return length

class Channel:
    """OpenFlow channel"""

    filter_func = None
    def __init__(self, queue, c2s_list,s2c_list,port_to_dpid_mapper,peername,switch_handler=None, switch_writer=None, controller_handler=None, controller_writer=None,logger_name = ""):
        """init
        Args:
            queue (asyncio.Queue) : queue to store packet
            switch_handler (SwitchHandler) :
            switch_writer (asyncio.StreamWriter) :
            controller_handler (ControllerHandler) :
            controller_writer (asyncio.StreamWriter) :
        """

        self.q_all = queue
        self.c2s_list = c2s_list
        self.s2c_list = s2c_list
        self.port_to_dpid_mapper = port_to_dpid_mapper
        self.peername = peername
        self.logger = getLogger(logger_name+"." + __name__)

        self._switch_handler = switch_handler
        self.switch_writer = switch_writer
        self._controller_handler = controller_handler
        self.controller_writer = controller_writer

    def set_switch(self, switch_handler, switch_writer):
        """set switch handler to send switch
        Args:
            switch_handler (SwitchHandler) :
            switch_writer (asyncio.StreamWriter) :
        """
        self._switch_handler = switch_handler
        self.switch_writer = switch_writer

    def set_controller(self, controller_handler, controller_writer):
        """set controller handler to send controller
        Args:
            controller_handler (ControllerHandler) :
            controller_writer (asyncio.StreamWriter) :
        """
        self._controller_handler = controller_handler
        self.controller_writer = controller_writer

    def _filter(self, data, switch2controller):
        """On Packet
        Args:
            data (bytes) :
            switch2controller (bool) :

        Returns:
            bytes
        """
        cls = self.__class__
        if cls.filter_func:
            data = cls.filter_func(data, switch2controller)
        return data
    
    
    def get_header(self,data):
        header = tuple()
        version = int.from_bytes(data[0:1],byteorder="big")
        type = int.from_bytes(data[1:2],byteorder="big")
        length = int.from_bytes(data[2:4],byteorder="big")
        xid = int.from_bytes(data[4:8],byteorder="big")
        header = (version,type,length,xid)
        return header

    async def data_process(self,data,strategy,controller_info_class):

        global exec_flag
        global ryu_exec_flag
        global fl_exec_flag
        global onos_exec_flag
        global odl_exec_flag
        processed_data = data
        msg_type = ofp.message.parse_header(data)[1]
        if exec_flag == False:
            if type(controller_info_class) == RyuInfo :
                processed_data = self.controller_flag_process(msg_type,ryu_exec_flag,data,strategy)
            if type(controller_info_class) == FLInfo :
                processed_data = self.controller_flag_process(msg_type,fl_exec_flag,data,strategy)
            if type(controller_info_class) == OnosInfo :
                processed_data = self.controller_flag_process(msg_type,onos_exec_flag,data,strategy)
            if type(controller_info_class) == ODLInfo :
                processed_data = self.controller_flag_process(msg_type,odl_exec_flag,data,strategy)
        return processed_data
    
    def controller_flag_process(self,msg_type,controller_exec_flag,data,strategy):
        global exec_finished_flag
        processed_data = data
        if controller_exec_flag == False:
            "deal the bizarre msg_type"
            if msg_type < 30:
                sub_type = "of_"+ofp.message.parse_message(data).__class__.__name__
                if OpenFlow_type[msg_type] == "of_hello":
                    processed_data = self.action_switch_case(strategy,data,processed_data)
                    exec_finished_flag = True
                elif OpenFlow_type[msg_type] == strategy.pkt_type :
                    if self.port_to_dpid_mapper[self.peername[1]] == 1:
                        processed_data = self.action_switch_case(strategy,data,processed_data)
                        exec_finished_flag = True
                elif OpenFlow_type[msg_type] == "of_multipart_reply" and strategy.pkt_type == sub_type:
                    if self.port_to_dpid_mapper[self.peername[1]] == 1:
                        processed_data = self.action_switch_case(strategy,data,processed_data)
                        exec_finished_flag = True
        return processed_data

    def action_switch_case(self,strategy,data,processed_data):
        action_list = strategy.action.split("|")
        for item in action_list:
            action_type = item.split(",",1)[0]
            if action_type == "DUP":
                par_str = item.split(",",1)[1]
                par = int(par_str.split("=")[1])
                for i in range(0,par-1):
                    processed_data = processed_data + data
                self.logger.debug("sent data to controller: {}".format(processed_data))
            elif action_type == "DROP":
                processed_data = bytes()
            elif action_type == "DELAY":
                par_str = item.split(",",1)[1]
                par = int(par_str.split("=")[1])
                time.sleep(par)
                self.logger.debug("sent data to controller: {}".format(data))
                processed_data = data
            elif action_type == "MOD":
                # field = strategy.field
                field = re.findall('field=\(.*?\)',item.split(",",1)[1])[0]
                field = field.split("=")[1]
                field = field.replace('(', '')
                field = field.replace(')', '')
                value = re.findall('val=\(.*?\)',item.split(",",1)[1])[0]
                value = value.split("=")[1]
                value = value.replace('(', '')
                value = value.replace(')', '')
                of_msg_data = ofp.message.parse_message(data)
                """'openflow msg' object is not subscriptable"""
                if 'match' in field:
                    of_msg_data = match_struct_process(of_msg_data,field,value)
                elif 'entries' in field:
                    of_msg_data = entries_struct_process(of_msg_data,field,value)
                elif is_number(value):
                    setattr(of_msg_data,field,int(value,16))
                else:
                    if field == "data":
                        setattr(of_msg_data,field,string_to_bytes(value))
                    else:
                        setattr(of_msg_data,field,value)
                processed_data = of_msg_data.pack()
                self.logger.debug("sent data to controller: {}".format(data))
            elif action_type == "DEL":
                block = re.findall('field=\(.*?\)',item.split(",",1)[1])[0]
                block = block.split("=")[1]
                block = block.replace('(', '')
                block = block.replace(')', '')
                of_msg_data = ofp.message.parse_message(data)
                if 'match' in block:
                    of_msg_data = match_struct_del_process(of_msg_data,block)
                elif 'entries' in block:
                    of_msg_data = entries_struct_del_process(of_msg_data,block)
                else:
                    of_msg_data.__dict__[block] = bytes()

                processed_data = of_msg_data.pack()
            elif action_type == "ADD":
                block = re.findall('field=\(.*?\)',item.split(",",1)[1])[0]
                block = block.split("=")[1]
                block = block.replace('(', '')
                block = block.replace(')', '')
                value = re.findall('val=\(.*?\)',item.split(",",1)[1])[0]
                value = value.split("=")[1]
                value = value.replace('(', '')
                value = value.replace(')', '')
                """convert quotes to double quotes"""
                value = value.replace("'", '"')
                value = json.loads(value)
                of_msg_data = ofp.message.parse_message(data)
                if 'match' in block:
                    of_msg_data = match_struct_add_process(of_msg_data,value)
                elif 'entries' in block:
                    of_msg_data = entries_struct_add_process(of_msg_data,value,block) 
                processed_data = of_msg_data.pack()
            elif action_type == "BUILD":
                build_type = re.findall('type=\(.*?\)',item.split(",",1)[1])[0]
                build_type = build_type.split("=")[1]
                build_type = build_type.replace('(', '')
                build_type = build_type.replace(')', '')
                build_type = build_type.split("_",1)[1]
                value = re.findall('val=\(.*?\)',item.split(",",1)[1])[0]
                value = value.split("=")[1]
                value = value.replace('(', '')
                value = value.replace(')', '')
                """convert quotes to double quotes"""
                value = value.replace("'", '"')
                """load can not convert 16 list"""
                value = json.loads(value)
                if len(data) >= 8:
                    # why need build ? It seems that build don't need to parse
                    built_msg = build_msg(build_type,value)
                    processed_data = data + built_msg
                # drop bytes -> 0 , then build
                else:
                    built_msg = build_msg(build_type,value)
                    processed_data = built_msg
            data = processed_data
        return processed_data

    async def controller_result_compare(self,controller_info_class):
        global exec_flag
        global ryu_exec_flag
        global fl_exec_flag
        global onos_exec_flag
        global odl_exec_flag
        global same_message_process_flag
        if type(controller_info_class) == RyuInfo :                
            ryu_exec_flag = True
            same_message_process_flag = True
        elif type(controller_info_class) == FLInfo :
            fl_exec_flag = True
            same_message_process_flag = True
        elif type(controller_info_class) == OnosInfo :
            onos_exec_flag = True
            same_message_process_flag = True
        elif type(controller_info_class) == ODLInfo :
            odl_exec_flag = True
            same_message_process_flag = True
        if ryu_exec_flag == True and fl_exec_flag == True and onos_exec_flag == True and odl_exec_flag == True:
            exec_flag = True

    async def send_to_controller(self, data, strategy,switch_handler,controller_info_class,controller_result=[]):
        """set data and sent to controller

        Args:
            data (bytes) : data that is sent to controller

        Returns:
            int : -1 if failed to send
        """
        global exec_flag
        global ryu_exec_flag
        global fl_exec_flag

        if not self.is_closing():
            filtered_data = self._filter(data, switch2controller=True)
            await self._put_queue_all(filtered_data, switch2controller=True)
            msg_type = ofp.message.parse_header(filtered_data)[1]
            if msg_type == 6:
                features_reply = ofp.message.parse_message(filtered_data)
                self.port_to_dpid_mapper[self.peername[1]]=features_reply.__dict__['datapath_id']
            if msg_type < 30:
                if OpenFlow_type[msg_type] == "of_packet_in":
                    try:
                        prased_data = ofp.message.parse_message(filtered_data)
                        self.s2c_list.append(prased_data.__dict__)
                    except:
                        pass
            processed_data = await self.data_process(filtered_data,strategy,controller_info_class)
            await self._controller_handler.send_to_controller(self.controller_writer, processed_data)
            
            if controller_info_class != None:
                thread_loop1 = asyncio.new_event_loop()
                threading.Thread(target=start_loop,args=(thread_loop1,)).start()
                asyncio.run_coroutine_threadsafe(controller_info_class.getSwitchInfoAfterExec(),thread_loop1)
                controller_info_class.switches_after_test  = switch_handler.switches
                asyncio.run_coroutine_threadsafe(controller_info_class.compare_before_and_after(controller_result),thread_loop1)
                asyncio.run_coroutine_threadsafe(self.controller_result_compare(controller_info_class),thread_loop1)
            self.logger.debug("set data and sent to controller : {}".format(processed_data))
            return 0
        else:
            self.logger.warning("Failed to send to controller : {}".format(data))
            return -1 
    
    async def send_to_switch(self, data):
        """set data and sent to switch

        Args:
            data (bytes) : data that is sent to switch

        Returns:
            int : -1 if failed to send
        """
        if not self.is_closing():
            filtered_data = self._filter(data, switch2controller=False)
            msg_type = ofp.message.parse_header(data)[1]
            if OpenFlow_type[msg_type] == "of_packet_out":
                prased_data = ofp.message.parse_message(data)
                self.c2s_list.append(prased_data.__dict__)
            await self._put_queue_all(filtered_data, switch2controller=False)
            await self._switch_handler.send_to_switch(self.switch_writer, filtered_data)
            self.logger.debug("set data and sent to switch : {}".format(filtered_data))
            return 0
        else:
            self.logger.warning("Failed to send to switch : {}".format(data))
            return -1
    
    async def _put_queue_all(self, data, switch2controller):
        """put data as message

        Args:
            data (bytes) : data
            switch2controller (bool) : Was the data sent from switch to controller?
        """
        timestamp = datetime.now().timestamp()
        local_ip, local_port = self.switch_writer.get_extra_info('peername')
        remote_ip, remote_port = self.controller_writer.get_extra_info('peername')
        msg = OFMsg(timestamp, local_ip, remote_ip, local_port, remote_port, data, switch2controller)
        await self.q_all.put(msg)

    def is_closing(self):
        """Is this channel closing?

        Returns:
            bool : Is this channel established?
        """
        is_closing = True
        if self.switch_writer is not None and self.controller_writer is not None\
                and self._switch_handler is not None and self._controller_handler is not None:
            is_closing = self.switch_writer.is_closing() or self.controller_writer.is_closing()

        if is_closing:
            self.logger.debug("is_closing is {}, s writer is {}, c writer is {}, s handler is {}, c handler is {},"
                              " s writer close? {}, c writer close? {}"
                              .format(is_closing, self.switch_writer is not None, self.controller_writer is not None,
                                      self._switch_handler is not None, self._controller_handler is not None,
                                      self.switch_writer.is_closing(), self.controller_writer.is_closing()))
        return is_closing
    
    @classmethod
    def filter(cls, func):
        """decorator"""
        def wrapper(data, switch2controller):
            data = func(data, switch2controller)
            return data

        cls.filter_func = wrapper
        return wrapper

class ChannelManager:
    """Channel Manager
    * This has queue that stores all data and gives the queue to api_module
    * This creates new channel

    Attributes:
        q_all (asyncio.Queue) : all data (from switch and controller)
        logger (Logger) : logger
        has_switch_join (bool) : True if a switch has join
        has_controller_join (bool) : True if a controller has join
        controller_handler (ControllerHandler) : client communicating with controller
    """

    def __init__(self, loop, controller_ip='127.0.0.1', controller_port=6633,logger_name="",controller_type=""):
        """init

        Args:
            loop (asyncio.AbstractEventLoop) : event loop
            controller_ip (str) : controller ip
            controller_port (int) : controller port
        """
        self.loop = loop
        self.q_all = asyncio.Queue(loop=self.loop)
        self.logger = getLogger(logger_name+"." + __name__)

        self.has_switch_join = False
        self.has_controller_join = False
        
        self.controller_type = controller_type

        self.controller_handler = ControllerHandler(controller_ip, controller_port, loop, self,logger_name=logger_name)
        
        self.c2s_list = []
        self.s2c_list = []
        self.port_to_dpid_mapper = {}

    async def create_channel(self, switch_handler, switch_writer,port_to_dpid_mapper,peername):
        """create openflow channel

        Args:
            switch_handler (SwitchHandler) : switch connection handler
            switch_writer (StreamWriter) : switch writer

        Returns:
            Channel or None : OpenFlow channel. If the controller cannot be connected, return None.
        """
        try:
            channel = Channel(self.q_all,self.c2s_list,self.s2c_list,port_to_dpid_mapper,peername)
            controller_writer = await self.controller_handler.open_connection(channel)
            if controller_writer:
                channel.set_switch(switch_handler, switch_writer)
                channel.set_controller(self.controller_handler, controller_writer)
                return channel
            else:
                self.logger.debug("no connectable controller")
                return None
        except Exception as e:
            raise

    def get_queue_all_data(self):
        """queue for all traffic data

        Returns:
            asyncio.Queue
        """
        return self.q_all

    def _has_open_channel(self):
        has_open_channel = self.has_switch_join and self.has_controller_join
        return has_open_channel

class SwitchHandler:
    """server communicating with switches

    Attributes:
        host (str) : switch ip
        port (int) : switch port
        loop (asyncio.AbstractEventLoop) : event loop
        channel_manager (ChannelManager) : channel manager
        logger (Logger) : logger
        switches (set) : switch set
    """
    
    def __init__(self, host, port, loop, channel_manager,logger_name,controller_type,strategy_queue,result_queue=[]):
        """init SwitchHandler

        Args:
            host (str) : switch ip
            port (int) : switch port
            loop (asyncio.AbstractEventLoop) :
            channel_manager (ChannelManager) :
        """
        self.host = host
        self.port = port
        self.loop = loop
        self.channel_manager = channel_manager
        self.logger = getLogger(logger_name+"." + __name__)
        
        self.contoller_type = controller_type

        self.switches = set()
        self.disconnected_switches = []
        self.port_to_dpid_mapper = {}
        self.strategy_queue = strategy_queue
        self.controller_result_queue = result_queue

    async def start_server(self):
        """start server"""
        server = await asyncio.start_server(self.handle_switch, host=self.host, port=self.port)
        self.logger.info("Server on {}".format(server.sockets[0].getsockname()))

        async with server:
            self.logger.info("Server serve forever {}".format(server.sockets[0].getsockname()))
            await server.serve_forever()
        
    async def handle_switch(self, reader, writer):
        """Accepting connections from switches

        This creates a channel and receives data from the switch.
        This tries to send the received data to the controller, if the connection is established.
        If the connection is not established, the data is discarded.

        Args:
            reader (asyncio.StreamReader) :
            writer (asyncio.StreamWriter) :

        Returns:

        """
        peername = writer.get_extra_info('peername')
        self.logger.info("Client {} is connected".format(peername))
        self.switches.add(peername)
        self.port_to_dpid_mapper[peername[1]] = 0
        self.channel_manager.has_switch_join = True

        channel = await self.channel_manager.create_channel(self, writer,self.port_to_dpid_mapper,peername)
        if channel is None:
            writer.close()
            return

        global strategy_str
        global strategy
        if not self.strategy_queue.if_empty():
            strategy_str = self.strategy_queue.dequeue()
            if strategy_str != "":
                strategy = strategy_process(strategy_str)
        try:
            while True:
                self.logger.debug("waiting data ......")
                # 64000 is default buffer size
                data = await reader.read(64000)                
                if not self.strategy_queue.if_empty():
                    strategy_str = self.strategy_queue.dequeue()
                    strategy = strategy_process(strategy_str)
                self.logger.debug("read {}".format(data))
                if not data:
                    self.logger.debug("no data from switch read")
                    break
                if not channel.is_closing():
                    data_list = []
                    self.data_split(data,data_list)
                    for data_item in data_list:
                        await self.data_process(data_item,channel,strategy,peername)
                else:
                    self.logger.debug("the channel is closing")
                    break
            time.sleep(0.01)
        except BrokenPipeError as e:
            self.logger.error("Failed to read: {}".format(str(e)))
        except ConnectionResetError as e:
            self.logger.error("Failed to read: {}".format(str(e)))
        except Exception as e:
            self.logger.error("Failed to read: {}".format(str(e)))
            raise
        finally:
            self.logger.info("Close the connection and do exit processing")
            if peername in self.switches:
                if self.contoller_type == "floodlight":
                    self.disconnected_switches.append(peername)
                    flinfo.controller_result.switches_change = ('remove',len(self.disconnected_switches),self.disconnected_switches)
                elif self.contoller_type == "ryu":
                    self.disconnected_switches.append(peername)
                    ryuinfo.controller_result.switches_change = ('remove',len(self.disconnected_switches),self.disconnected_switches)
                elif self.contoller_type == "onos":
                    self.disconnected_switches.append(peername)
                    onosinfo.controller_result.switches_change = ('remove',len(self.disconnected_switches),self.disconnected_switches)
                elif self.contoller_type == "odl":
                    self.disconnected_switches.append(peername)
                    odlinfo.controller_result.switches_change = ('remove',len(self.disconnected_switches),self.disconnected_switches)
                self.switches.remove(peername)
                del self.port_to_dpid_mapper[peername[1]]
            if len(self.switches) == 0:
                self.channel_manager.has_switch_join = False
            writer.close()

    async def send_to_switch(self, writer, data):
        """send data to switch if queue has data

        Args:
            writer (asyncio.StreamWriter) :
            data (bytes) : data from controller

        Returns:

        """
        try:
            if not writer.is_closing():
                writer.write(data)
                await writer.drain()
                self.logger.debug("sent data to switch: {}".format(data))
            else:
                self.logger.debug("channel is closed")
        except ConnectionResetError as e:
            self.logger.info("Connection reset: {}".format(str(e)))

    async def data_process(self,data,channel,strategy,peername):
        tasks = []
        
        global exec_flag
        global ryu_exec_flag
        global fl_exec_flag
        global onos_exec_flag
        global odl_exec_flag
        global same_message_process_flag
        global compare_different_controller

        loop = asyncio.get_running_loop()
        thread_loop = asyncio.new_event_loop()
        msg_type = ofp.message.parse_header(data)[1]
        sub_type = ""
        if msg_type<=30 and OpenFlow_type[msg_type] == 'of_multipart_reply':
            try:
                sub_type = "of_"+ofp.message.parse_message(data).__class__.__name__
            except ProtocolError:
                pass
        new_task = loop.create_task(channel.send_to_controller(data,strategy,None,None,self.controller_result_queue))
        print("fl_exec_flag :",fl_exec_flag,"ryu_exec_flag",ryu_exec_flag,"onos_exec_flag",onos_exec_flag,"odl_exec_flag",odl_exec_flag)
        if msg_type < 30 and exec_flag == False:
            if OpenFlow_type[msg_type] == 'of_multipart_reply' and sub_type == strategy.pkt_type and same_message_process_flag == True and self.port_to_dpid_mapper[peername[1]] == 1 :
                self.controller_process_case(thread_loop,new_task,loop,channel,data,strategy)
            elif OpenFlow_type[msg_type] == strategy.pkt_type and same_message_process_flag == True and self.port_to_dpid_mapper[peername[1]] == 1 :
                self.controller_process_case(thread_loop,new_task,loop,channel,data,strategy)
            elif OpenFlow_type[msg_type] == strategy.pkt_type == "of_hello" and same_message_process_flag == True:
                self.controller_process_case(thread_loop,new_task,loop,channel,data,strategy)
            elif OpenFlow_type[msg_type] == strategy.pkt_type == "of_features_reply" or OpenFlow_type[msg_type] == strategy.pkt_type == "of_get_config_reply": 
                self.controller_process_case(thread_loop,new_task,loop,channel,data,strategy)
            else:
                await asyncio.gather(*tasks)
        elif exec_flag == True and compare_different_controller == False:
            print("Floodlight Info:")
            flinfo.controller_result.to_str()
            print("Ryu Info:")
            ryuinfo.controller_result.to_str()
            print("Onos Info:")
            onosinfo.controller_result.to_str()
            print("ODL Info:")
            odlinfo.controller_result.to_str()
            if self.contoller_type == "ryu":
                print("ryu controller result queue",self.controller_result_queue)
            elif self.contoller_type == "floodlight":
                print("fl controller result queue",self.controller_result_queue)
            elif self.contoller_type == "onos":
                print("onos controller result queue",self.controller_result_queue)
            elif self.contoller_type == "odl":
                print("odl controller result queue",self.controller_result_queue)

            difference1 = ryuinfo.controller_result.controller_compare(flinfo.controller_result)
            difference2 = ryuinfo.controller_result.controller_compare(onosinfo.controller_result)
            difference3 = ryuinfo.controller_result.controller_compare(odlinfo.controller_result)
            difference = difference1 or difference2 or difference3
            print("difference :",difference)
            if self.controller_result_queue.size() != 0:
                time.sleep(0.5)
                compare_different_controller = True
        else:
            tasks.append(new_task)
            await asyncio.gather(*tasks)
    
    def controller_process_case(self,thread_loop,new_task,loop,channel,data,strategy):
        global same_message_process_flag
        print("exec_flag:",exec_flag,"compare_different_controller:",compare_different_controller)
        if self.contoller_type == "floodlight" and fl_exec_flag == False:
            global flinfo
            flinfo.switches_before_test = self.switches
            threading.Thread(target=start_loop,args=(thread_loop,)).start()
            new_task.cancel()
            """do not process same msg"""
            same_message_process_flag = False
            future = asyncio.run_coroutine_threadsafe((flinfo.getSwitchInfoBeforeExec(loop,channel,data,strategy,flinfo,self)),thread_loop)
        elif self.contoller_type == "ryu" and ryu_exec_flag == False:
            global ryuinfo
            ryuinfo.switches_before_test = self.switches
            threading.Thread(target=start_loop,args=(thread_loop,)).start()
            new_task.cancel()
            """do not process same msg"""
            same_message_process_flag = False
            future = asyncio.run_coroutine_threadsafe((ryuinfo.getSwitchInfoBeforeExec(loop,channel,data,strategy,ryuinfo,self)),thread_loop)
        elif self.contoller_type == "onos" and onos_exec_flag == False:
            global onosinfo
            onosinfo.switches_before_test = self.switches
            threading.Thread(target=start_loop,args=(thread_loop,)).start()
            new_task.cancel()
            """do not process same msg"""
            same_message_process_flag = False
            future = asyncio.run_coroutine_threadsafe((onosinfo.getSwitchInfoBeforeExec(loop,channel,data,strategy,onosinfo,self)),thread_loop)
        elif self.contoller_type == "odl" and odl_exec_flag == False:
            global odlinfo
            odlinfo.switches_before_test = self.switches
            threading.Thread(target=start_loop,args=(thread_loop,)).start()
            new_task.cancel()
            """do not process same msg"""
            same_message_process_flag = False
            future = asyncio.run_coroutine_threadsafe((odlinfo.getSwitchInfoBeforeExec(loop,channel,data,strategy,odlinfo,self)),thread_loop)

    def data_split(self,data,data_list):
        if len(data)!=0:
            length_bytes = data[2:4]
            length = int.from_bytes(length_bytes,"big")
            """filter table feature msg"""
            if len(data) > length and len(data) < 1000:
                of_msg = data[0:length]
                remain_data = data[length:]
                data_list.append(of_msg)
                self.data_split(remain_data,data_list)
            else:
                """don't split"""
                data_list.append(data)

class ControllerHandler:
    """client communicating with controller

    Attributes:
        host (str) :
        port (int) :
        loop (asyncio.AbstractEventLoop) :
        channel_manager (ChannelManager) :
    """
    def __init__(self, host, port, loop, channel_manager,logger_name):
        """init SwitchHandler

        Args:
            host (str) : controller ip address
            port (int) : controller listen port
            loop (asyncio.AbstractEventLoop) : event loop
            channel_manager (ChannelManager) : channel manager
        """
        self.host = host
        self.port = port
        self.loop = loop
        self.channel_manager = channel_manager
        self.exec_flag = False
        self.logger = getLogger(logger_name+"." + __name__)

        self.controllers = set()

    async def open_connection(self, channel):
        """try to connect to controller

        Args:
            channel (Channel) :

        Returns:
            asyncio.StreamWriter or None : if succeeded to connect, return writer, else None
        """
        try:
            reader, writer = await asyncio.open_connection(host=self.host, port=self.port, loop=self.loop)
            asyncio.ensure_future(self.handle_controller(reader, writer, channel))
        except ConnectionRefusedError as e:
            self.logger.error("Failed to connect to controller : {}".format(str(e)))
            return None
        else:
            return writer

    async def handle_controller(self, reader, writer, channel):
        """handle controller connection

        Args:
            reader (asyncio.StreamReader) :
            writer (asyncio.StreamWriter) :
            channel (Channel) :
        """
        peername = writer.get_extra_info('peername')
        self.logger.info("connected Controller {}".format(peername))
        self.controllers.add(peername)
        self.channel_manager.has_controller_join = True
        try:
            while True:
                self.logger.debug("waiting data ......")
                data = await reader.read(64000)
                self.logger.debug("read {}".format(data))
                if not data:
                    self.logger.debug("no data from controller read")
                    break
                if not channel.is_closing():
                    data_list = []
                    self.data_split(data,data_list)
                    for data_item in data_list:
                        await channel.send_to_switch(data_item)
                else:
                    self.logger.debug("the channel is close")
                    if channel.controller_writer is not None:
                        break
                time.sleep(0.01)
        except Exception as e:
            self.logger.error("Failed to read: {}".format(str(e)))
            raise
        finally:
            self.logger.info("Close the connection and do exit processing")
            if peername in self.controllers:
                self.controllers.remove(peername)
            if len(self.controllers) == 0:
                self.channel_manager.has_controller_join = False
            writer.close()

    async def send_to_controller(self, writer, data):
        """send data to controller if queue has data

        Args:
            writer (asyncio.StreamWriter) :
            data (bytes) :
        """

        try:
            if not writer.is_closing():
                    writer.write(data)
                    await writer.drain()
                    self.logger.debug("sent data to controller: {}".format(data))
            else:
                self.logger.debug("channel is closed")
        except ConnectionResetError as e:
            self.logger.info("Connection reset: {}".format(str(e)))
        except Exception as e:
            self.logger.error("Connection error: {}".format(str(e)))
            raise e

    def data_split(self,data,data_list):
        if len(data)!=0:
            length_bytes = data[2:4]
            length = int.from_bytes(length_bytes,"big")
            """filter table feature msg"""
            if len(data) > length and len(data) < 1000:
                of_msg = data[0:length]
                remain_data = data[length:]
                data_list.append(of_msg)
                self.data_split(remain_data,data_list)
            else:
                """don't split"""
                data_list.append(data)