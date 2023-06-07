# coding:utf8
import struct
import socket
import requests
from enum import Enum
import sys
import time
from socket import error as socket_error
import errno

from RestAPP.ControllerResult import ControllerResult
from RestAPP.listcompare import infodifferdict,infodifferlist,infodifferset

controller_ip = '172.17.0.2'
headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json'}
server_address = ('127.0.0.1', 5555)

switch_url = "http://"+controller_ip+":8080/collectswithes/switcheslist/json"
host_url = "http://"+controller_ip+":8080/hosts/json"

# the url depend on ryu app ryu/app/rest_topology.py
link_url = "http://"+controller_ip+":8080/v1.0/topology/links"
# must specify dpid in the url
flow_url = "http://"+controller_ip+":8080/stats/flow/"
# must specify dpid in the url
group_url = "http://"+controller_ip+":8080/stats/groupdesc/"
# must specify dpid in the url
meter_url = "http://"+controller_ip+":8080/stats/meterconfig/"

# collected info before & after test case
switch_list_before_test = []
switch_list_after_test = []
port_list_before_test = []
port_list_after_test = []
links_before_test = []
links_after_test = []
hosts_before_test = []
hosts_after_test = []
flow_before_test = []
flow_after_test = []
group_before_test = []
group_after_test = []
meter_before_test = []
meter_after_test = []

class APPInterfaceState(Enum):
    NO_CONNECTED = 0
    HELLO = 1
    BEFORE_TEST = 2
    AFTER_TEST = 3

class AppInterface():
    threadlist = []
    app_socket = None
    appinterfacestate = APPInterfaceState.NO_CONNECTED

    def readUTF(self,socket):
        size = struct.unpack("!H", socket.recv(2))[0]
        message = socket.recv(size)
        return message

    def writeUTF(self,socket,message):
        size = len(message)
        socket.send(struct.pack("!H",size))
        socket.send(message)

    def ConnectServer(self,server_address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[AppInterface] Connecting to {} port {}".format(server_address[0],server_address[1]))
        sock.connect(server_address)
        self.app_socket = sock
        message = "ryu_appinterface"
        self.writeUTF(sock, message)
        if self.readUTF(sock) =="Hello":
            self.appinterfacestate = APPInterfaceState.HELLO

class RyuInfo():
    def __init__(self):
        """ collected info before & after test case """
        self.switch_list_before_test = []
        self.port_list_before_test = []
        self.links_before_test = []
        self.hosts_before_test = []
        self.flow_before_test = []
        self.group_before_test = []
        self.meter_before_test = []

        self.switch_list_after_test = []
        self.port_list_after_test = []
        self.links_after_test = []
        self.hosts_after_test = []
        self.flow_after_test = []
        self.group_after_test = []
        self.meter_after_test = []   
        
        self.switches_before_test = set()
        self.switches_after_test = set()

        self.controller_result = ControllerResult("Ryu")

    async def getSwitchInfoBeforeExec(self,loop,channel,data,strategy,ryuinfo,switch_handler):
        print("get switch info before exec")
        res = requests.get(url=switch_url ,headers=headers)
        res = res.json()

        for switch in res:
                self.switch_list_before_test.append(switch.encode("utf-8"))
                for port in res[switch]:
                    self.port_list_before_test.append(port)
        print("switch %d %s"%(len(self.switch_list_before_test),self.switch_list_before_test))
        if len(self.switch_list_before_test) != 0:
            print("port no  hwAddr                 portName   portState    portConfig")
            for port in self.port_list_before_test:
                port_state = []
                if port["state"] == 0x4 :
                    port_state.append("LIVE")
                if port["state"] == 0x2 :
                    port_state.append("BLOCKED")
                if port["state"] == 0x1 :
                    port_state.append("LINK_DOWN")
                port_config = []
                if port["config"] == 0x1  :
                    port_config.append("PORT_DOWN")
                if port["config"] == 0x4 :
                    port_config.append("NO_RECV")
                if port["config"] == 0x20 :
                    port_config.append("NO_FWD")
                if port["config"] == 0x40 :
                    port_config.append("NO_PACKET_IN")
                print("%s        %s      %s     %s       %s"%(port["port_no"],port["hw_addr"],port["name"],port_state,port_config))
        
        res = requests.get(url=link_url ,headers=headers)
        res = res.json()

        if len(res) == 0:
            print("can not find link message")
        else:
            self.links_before_test = links_process(res)
            links_print(self.links_before_test)

        # host related
        res = requests.get(url=host_url ,headers=headers)
        res = res.json()

        if len(res) == 0:
            print("can not find host message")
        else:
            self.hosts_before_test = host_process(res)
            host_print(self.hosts_before_test )

        # flow related
        all_flows = []
        all_flows= flow_aggregation(self.switch_list_before_test,flow_url,headers)
        self.flow_before_test = flow_process(all_flows)
        
        if len(self.flow_before_test) == 0:
            print("can not find flow info")
        else:
            flow_print(self.flow_before_test)

        # group related
        all_groups = []
        all_groups= group_aggregation(self.switch_list_before_test,group_url,headers)
        self.group_before_test = group_process(all_groups)
        if len(self.group_before_test) == 0:
            print("can not find group info")
        else:  
            group_print(self.group_before_test)

        # meter related
        all_meters = []
        all_meters= meter_aggregation(self.switch_list_before_test,meter_url,headers)
        self.meter_before_test = meter_process(all_meters)
        if len(meter_before_test) == 0:
            print("can not find meter info")
        else:  
            meter_print(self.meter_before_test)

        new_task = loop.create_task(channel.send_to_controller(data,strategy,switch_handler,ryuinfo,switch_handler.controller_result_queue)) 

    async def getSwitchInfoAfterExec(self):
        print("get switch info after exec")
        res = requests.get(url=switch_url ,headers=headers)
        res = res.json()

        for switch in res:
            self.switch_list_after_test.append(switch.encode("utf-8"))
            for port in res[switch]:
                self.port_list_after_test.append(port)
        print("switch %d %s"%(len(self.switch_list_after_test),self.switch_list_after_test))
        if len(self.switch_list_after_test) != 0:
            print("port no  hwAddr                 portName   portState    portConfig")
            for port in self.port_list_after_test:
                port_state = []
                if port["state"] == 0x4 :
                    port_state.append("LIVE")
                if port["state"] == 0x2 :
                    port_state.append("BLOCKED")
                if port["state"] == 0x1 :
                    port_state.append("LINK_DOWN")
                port_config = []
                if port["config"] == 0x1  :
                    port_config.append("PORT_DOWN")
                if port["config"] == 0x4 :
                    port_config.append("NO_RECV")
                if port["config"] == 0x20 :
                    port_config.append("NO_FWD")
                if port["config"] == 0x40 :
                    port_config.append("NO_PACKET_IN")
                print("%s        %s      %s     %s       %s"%(port["port_no"],port["hw_addr"],port["name"],port_state,port_config))
        res = requests.get(url=link_url ,headers=headers)
        res = res.json()

        if len(res) == 0:
            print("can not find link message")
        else:
            self.links_after_test = links_process(res)
            links_print(self.links_after_test)

        # host related
        res = requests.get(url=host_url ,headers=headers)
        res = res.json()

        if len(res) == 0:
            print("can not find host message")
        else:
            self.hosts_after_test = host_process(res)
            host_print(self.hosts_after_test )


        # flow related
        all_flows = []
        all_flows= flow_aggregation(self.switch_list_after_test,flow_url,headers)
        self.flow_after_test = flow_process(all_flows)
        if len(self.flow_after_test) == 0:
            print("can not find flow info")
        else:
            flow_print(self.flow_after_test)

        # group related
        all_groups = []
        all_groups= group_aggregation(self.switch_list_after_test,group_url,headers)
        self.group_after_test = group_process(all_groups)
        if len(self.group_after_test) == 0:
            print("can not find group info")
        else:  
            group_print(self.group_after_test)

        # meter related
        all_meters = []
        all_meters= meter_aggregation(self.switch_list_after_test,meter_url,headers)
        self.meter_after_test = meter_process(all_meters)
        if len(self.meter_after_test) == 0:
            print("can not find meter info")
        else:  
            meter_print(self.meter_after_test)

    async def compare_before_and_after(self,ryu_controller_result):
        self.controller_result.switch_change = infodifferlist(self.switch_list_before_test,self.switch_list_after_test)
        self.controller_result.port_change = infodifferdict(self.port_list_before_test,self.port_list_after_test)
        self.controller_result.host_change = infodifferdict(self.hosts_before_test,self.hosts_after_test)
        self.controller_result.link_change = infodifferdict(self.links_before_test,self.links_after_test)
        self.controller_result.flow_length_change = infodifferdict(self.flow_before_test,self.flow_after_test)
        self.controller_result.group_length_change = infodifferdict(self.group_before_test,self.group_after_test)
        self.controller_result.meter_length_change = infodifferdict(self.meter_before_test,self.meter_after_test)
        self.controller_result.switches_change = infodifferset(self.switches_before_test,self.switches_after_test)

        ryu_controller_result.enqueue(self.controller_result)
        self.controller_result.to_str()

def getSwitchInfoBeforeExec():
    print("get switch info before exec")
    res = requests.get(url=switch_url ,headers=headers)
    res = res.json()

    for switch in res:
        switch_list_before_test.append(switch.encode("utf-8"))
        for port in res[switch]:
            port_list_before_test.append(port)
    print("switch %d %s"%(len(switch_list_before_test),switch_list_before_test))
    if len(switch_list_before_test) != 0:
        print("port no  hwAddr                 portName   portState    portConfig")
        for port in port_list_before_test:
            port_state = []
            if port["state"] == 0x4 :
                port_state.append("LIVE")
            if port["state"] == 0x2 :
                port_state.append("BLOCKED")
            if port["state"] == 0x1 :
                port_state.append("LINK_DOWN")
            port_config = []
            if port["config"] == 0x1  :
                port_config.append("PORT_DOWN")
            if port["config"] == 0x4 :
                port_config.append("NO_RECV")
            if port["config"] == 0x20 :
                port_config.append("NO_FWD")
            if port["config"] == 0x40 :
                port_config.append("NO_PACKET_IN")
            print("%s        %s      %s     %s       %s"%(port["port_no"],port["hw_addr"],port["name"],port_state,port_config))

    res = requests.get(url=link_url ,headers=headers)
    res = res.json()

    if len(res) == 0:
        print("can not find link message")
    else:
        links_before_test = links_process(res)
        links_print(links_before_test)

    # host related
    res = requests.get(url=host_url ,headers=headers)
    res = res.json()

    if len(res) == 0:
        print("can not find host message")
    else:
        host_before_test = host_process(res)
        host_print(host_before_test )

    # flow related
    all_flows = []
    all_flows= flow_aggregation(switch_list_before_test,flow_url,headers)
    flow_before_test = flow_process(all_flows)
    if len(flow_before_test) == 0:
        print("can not find flow info")
    else:
        flow_print(flow_before_test)

    # group related
    all_groups = []
    all_groups= group_aggregation(switch_list_before_test,group_url,headers)
    group_before_test = group_process(all_groups)
    if len(group_before_test) == 0:
        print("can not find group info")
    else:  
        group_print(group_before_test)

    # meter related
    all_meters = []
    all_meters= meter_aggregation(switch_list_before_test,meter_url,headers)
    meter_before_test = meter_process(all_meters)
    if len(meter_before_test) == 0:
        print("can not find meter info")
    else:  
        meter_print(meter_before_test)


def getSwitchInfoAfterExec():
    print("get switch info after exec")
    res = requests.get(url=switch_url ,headers=headers)
    res = res.json()

    for switch in res:
        switch_list_after_test.append(switch.encode("utf-8"))
        for port in res[switch]:
            port_list_after_test.append(port)
    print("switch %d %s"%(len(switch_list_after_test),switch_list_after_test))
    if len(switch_list_after_test) != 0:
        print("port no  hwAddr                 portName   portState    portConfig")
        for port in port_list_after_test:
            port_state = []
            if port["state"] == 0x4 :
                port_state.append("LIVE")
            if port["state"] == 0x2 :
                port_state.append("BLOCKED")
            if port["state"] == 0x1 :
                port_state.append("LINK_DOWN")
            port_config = []
            if port["config"] == 0x1  :
                port_config.append("PORT_DOWN")
            if port["config"] == 0x4 :
                port_config.append("NO_RECV")
            if port["config"] == 0x20 :
                port_config.append("NO_FWD")
            if port["config"] == 0x40 :
                port_config.append("NO_PACKET_IN")
            print("%s        %s      %s     %s       %s"%(port["port_no"],port["hw_addr"],port["name"],port_state,port_config))
    res = requests.get(url=link_url ,headers=headers)
    res = res.json()

    if len(res) == 0:
        print("can not find link message")
    else:
        links_after_test = links_process(res)
        links_print(links_after_test)

    # host related
    res = requests.get(url=host_url ,headers=headers)
    res = res.json()

    if len(res) == 0:
        print("can not find host message")
    else:
        host_after_test = host_process(res)
        host_print(host_after_test )


    # flow related
    all_flows = []
    all_flows= flow_aggregation(switch_list_after_test,flow_url,headers)
    flow_after_test = flow_process(all_flows)
    flow_print(flow_after_test)

    # group related
    all_groups = []
    all_groups= group_aggregation(switch_list_after_test,group_url,headers)
    group_after_test = group_process(all_groups)
    if len(group_after_test) == 0:
        print("can not find group info")
    else:  
        group_print(group_after_test)

    # meter related
    all_meters = []
    all_meters= meter_aggregation(switch_list_after_test,meter_url,headers)
    meter_after_test = meter_process(all_meters)
    if len(meter_after_test) == 0:
        print("can not find meter info")
    else:  
        meter_print(meter_after_test)

def links_process(res):
    links = [] 
    for link_from_controller in res:
        link = {}
        link["LINK_SRC_SWITCH"] = link_from_controller["src"]["dpid"]
        link["LINK_SRC_PORT"] = link_from_controller["src"]["port_no"]
        link["LINK_DST_SWITCH"] = link_from_controller["dst"]["dpid"]
        link["LINK_DST_PORT"] = link_from_controller["dst"]["port_no"]        
        links.append(link)
    return links

def links_print(links):
    count = len(links)
    for index in range(0,count):
        print("---------------------------------------------------")
        print("LINK INFO FROM CONTROLLER : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("LINK_SRC_SWITCH = {}".format(links[index]["LINK_SRC_SWITCH"]))
        print("LINK_SRC_PORT   = {}".format(links[index]["LINK_SRC_PORT"]))
        print("LINK_DST_SWITCH = {}".format(links[index]["LINK_DST_SWITCH"]))
        print("LINK_DST_PORT   = {}".format(links[index]["LINK_DST_PORT"]))
        print("---------------------------------------------------")
        print("")

def host_process(res):
    hosts = [] 
    for host_from_controller in res:
        host = {}
        host["HOST_IP"] = host_from_controller["ipv4"]
        host["HOST_MAC"] = host_from_controller["mac"]
        host["ATTACH_SWITCH"] = host_from_controller["dpid"]
        host["ATTACH_PORT"] = host_from_controller["port_no"]        
        hosts.append(host)
    return hosts

def host_print(hosts):
    count = len(hosts)
    for index in range(0,count):
        print("---------------------------------------------------")
        print("HOST INFO FROM CONTROLLER : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("HOST_IP       = {}".format(hosts[index]["HOST_IP"]))
        print("HOST_MAC      = {}".format(hosts[index]["HOST_MAC"]))
        print("ATTACH_SWITCH = {}".format(hosts[index]["ATTACH_SWITCH"]))
        print("ATTACH_PORT   = {}".format(hosts[index]["ATTACH_PORT"]))
        print("---------------------------------------------------")
        print("")

def flow_aggregation(switches,flow_url,headers):
    all_flows = []
    for switch in switches:
        switch = str(switch,encoding='utf-8')
        switch_flow_url = flow_url + switch

        res = requests.get(url=switch_flow_url,headers=headers)
        res = res.json()

        flow_entry_list = res[switch]
        
        for flow in flow_entry_list:
            flow["switch"] = switch 
            all_flows.append(flow)
    return all_flows

def flow_process(res):
    flow_list = []
    for flow_from_stats in res:
        flow = {}
        flow["SWITCH"] =  flow_from_stats["switch"]
        flow["TABLE ID"] = flow_from_stats["table_id"]
        flow["PRIORITY"] = flow_from_stats["priority"]
        flow["MATCH"]= flow_from_stats["match"]
        flow["ACTIONS"]= flow_from_stats["actions"]
        flow_list.append(flow)
    return flow_list
 
def flow_print(flows):
    count = len(flows)
    for index in range(0,count):
        print("---------------------------------------------------")
        print("FLOW INFO FROM FLOW STATS : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH   = {}".format(flows[index]["SWITCH"]))
        print("TABLE ID = {}".format(flows[index]["TABLE ID"]))
        print("PRIORITY = {}".format(flows[index]["PRIORITY"]))
        print("MATCH    = {}".format(flows[index]["MATCH"]))
        print("ACTIONS  = {}".format(flows[index]["ACTIONS"]))
        print("---------------------------------------------------")
        print("")

def group_aggregation(switches,group_url,headers):
    all_groups = []
    for switch in switches:
        switch = str(switch,encoding='utf-8')
        switch_group_url = group_url + switch
        
        res = requests.get(url=switch_group_url,headers=headers)
        res = res.json()

        group_entry_list = res[switch]
        
        for group in group_entry_list:
            group["switch"] = switch 
            all_groups.append(group)
    return all_groups

def group_process(res):
    group_list = []
    for group_from_stats in res:
        group = {}
        group["SWITCH"] =  group_from_stats["switch"]
        group["GROUP ID"] = group_from_stats["group_id"]
        group["GROUP TYPE"] = group_from_stats["type"]
        group["BUCKETS"]= group_from_stats["buckets"]
        group_list.append(group)
    return group_list

def group_print(groups):
    count = len(groups)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" GROUP INFO FROM GROUP STATS : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH     = {}".format(groups[index]["SWITCH"]))
        print("GROUP ID   = {}".format(groups[index]["GROUP ID"]))
        print("GROUP TYPE = {}".format(groups[index]["GROUP TYPE"]))
        print("BUCKETS    = {}".format(groups[index]["BUCKETS"]))
        print("---------------------------------------------------")
        print("")    

def meter_aggregation(switches,meter_url,headers):
    all_meters = []
    for switch in switches:
        switch = str(switch,encoding='utf-8')
        switch_meter_url = meter_url + switch
        
        res = requests.get(url=switch_meter_url,headers=headers)
        res = res.json()

        meter_entry_list = res[switch]
        
        for meter in meter_entry_list:
            meter["switch"] = switch 
            all_meters.append(meter)
    return all_meters

def meter_process(res):
    meter_list = []
    for meter_from_stats in res:
        meter = {}
        meter["SWITCH"] =  meter_from_stats["switch"]
        meter["METER ID"] = meter_from_stats["meter_id"]
        meter["METER FLAGS"] = meter_from_stats["flags"]
        meter["METER BANDS"]= meter_from_stats["bands"]
        meter_list.append(meter)
    return meter_list

def meter_print(meters):
    count = len(meters)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" METER INFO FROM METER STATS : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH      = {}".format(meters[index]["SWITCH"]))
        print("METER ID    = {}".format(meters[index]["METER ID"]))
        print("METER FLAGS = {}".format(meters[index]["METER FLAGS"]))
        print("METER BANDS = {}".format(meters[index]["METER BANDS"]))
        print("---------------------------------------------------")
        print("")  

def runAppinterface():
    appInterface = AppInterface()
    try:
        appInterface.ConnectServer(server_address=server_address)
        while True:
            if appInterface.appinterfacestate == APPInterfaceState.HELLO:
                data = appInterface.readUTF(appInterface.app_socket)
                if  "KeepAlive" in data:
                    print("received KeepAlive")
                    appInterface.writeUTF(appInterface.app_socket,"KeepAlive received")
                elif data == "beforetest":
                    print("-----------------beforetest----------------------")
                    getSwitchInfoBeforeExec()
                    appInterface.appinterfacestate = APPInterfaceState.BEFORE_TEST
            if appInterface.appinterfacestate == APPInterfaceState.BEFORE_TEST:
                data = appInterface.readUTF(appInterface.app_socket)
                if data == "KeepAlive":
                    print("received KeepAlive")
                    continue
                elif data == "aftertest":
                    print("------------------aftertest-----------------------")
                    getSwitchInfoAfterExec()
                    appInterface.appinterfacestate = APPInterfaceState.AFTER_TEST
                    break
    except socket_error as serr:
        if serr.errno == errno.ECONNREFUSED:
            print("[AppInterface] Agent Manager is not listening")
    except:
        e = sys.exc_info()
        print("[AppInterface] error: " + str(e))
    finally:
        time.sleep(5)