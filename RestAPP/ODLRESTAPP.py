# coding:utf8
import struct
import socket
import traceback
import requests
from enum import Enum
import sys
import time
from socket import error as socket_error
import errno
import urllib
from RestAPP.ControllerResult import ControllerResult
from RestAPP.listcompare import infodifferdict,infodifferlist,infodifferset

controller_ip = '172.17.0.5'
topo_url = "http://"+controller_ip+":8181/restconf/operational/network-topology:network-topology"
# in fact , the response of this url including switch info & topolopy info
link_url = "http://"+controller_ip+":8181/restconf/operational/network-topology:network-topology"
# after packet in , controller can trace host,and host info is mixed with node(switch) info
# hosts and switches are both data plane nodes
# we can also get host info from link (another method)
host_url = "http://"+controller_ip+":8181/restconf/operational/network-topology:network-topology"
config_flow_url = "http://"+controller_ip+":8181/restconf/config/opendaylight-inventory:nodes/node/"
config_group_url = "http://"+controller_ip+":8181/restconf/config/opendaylight-inventory:nodes/node/"
config_meter_url = "http://"+controller_ip+":8181/restconf/config/opendaylight-inventory:nodes/node/"
operational_flow_url = "http://"+controller_ip+":8181/restconf/operational/opendaylight-inventory:nodes/node/"
operational_group_url = "http://"+controller_ip+":8181/restconf/operational/opendaylight-inventory:nodes/node/"
operational_meter_url = "http://"+controller_ip+":8181/restconf/operational/opendaylight-inventory:nodes/node/"

headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json'}
server_address = ('127.0.0.1', 3456)
auth_info = ('admin','admin')

# collected info before & after test case
switch_list_before_test = []
switch_list_after_test = []
port_list_before_test = []
port_list_after_test = []
links_before_test = []
links_after_test = []
host_before_test = []
host_after_test = []
config_flow_before_test = []
config_flow_after_test = []
config_group_before_test = []
config_group_after_test = []
config_meter_before_test = []
config_meter_after_test = []
operational_flow_before_test = []
operational_flow_after_test = []
operational_group_before_test = []
operational_group_after_test = []
operational_meter_before_test = []
operational_meter_after_test = []

class ODLInfo():
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

        self.controller_result = ControllerResult("ODL")
    
    async def getSwitchInfoBeforeExec(self,loop,channel,data,strategy,odlinfo,switch_handler):
        print("get switch info before exec")
        switch_res = {}
        res = requests.get(url=topo_url,auth=auth_info)
        topo_res = res.json()
        network_topo = topo_res["network-topology"]
        topologys = network_topo["topology"]
        for topology in topologys:
            switches = topology["node"]
            for switch in switches:
                if "host" not in switch["node-id"]:
                    self.switch_list_before_test.append(switch["node-id"])
        print("switch %d %s"%(len(self.switch_list_before_test),self.switch_list_before_test))
        if len(self.switch_list_before_test) != 0:
            print("port no  hwAddr                 portName   portState    portConfig")
        for openflow_switch in  self.switch_list_before_test:
            url = "http://"+ controller_ip +":8181/restconf/operational/opendaylight-inventory:nodes/node/"+ openflow_switch
            res = requests.get(url=url,auth=auth_info)
            res = res.json()
            
            switch_res[openflow_switch] = res

            self.port_list_before_test = res["node"][0]["node-connector"]
            for port in self.port_list_before_test:
                if "flow-node-inventory:configuration" in port:
                    port_state = []
                    if port["flow-node-inventory:state"]["link-down"] == True:
                        port_state.append("LINK_DOWN")
                    if port["flow-node-inventory:state"]["live"] == True:
                        port_state.append("LIVE")
                    if port["flow-node-inventory:state"]["blocked"] == True:
                        port_state.append("BLOCKED")
                    port_config = []
                    if port["flow-node-inventory:configuration"] == "":
                        port_config.append("")
                    else:
                        port_config.append(port["flow-node-inventory:configuration"])
                else:
                    port_state = port["flow-node-inventory:state"]
                    port_config = "supported"
                print("%s        %s      %s     %s    %s"%(port["flow-node-inventory:port-number"],port["flow-node-inventory:hardware-address"],
                port["flow-node-inventory:name"],port_state,port_config))    
            
        # link related
        network_topo = topo_res["network-topology"]
        topologys = network_topo["topology"][0]
        if "links" in topologys.keys():
            links = topologys["link"]
        else:
            links = {}

        if links == {}:
            print("can not find link message")
        else:
            self.links_before_test = links_process(links)
            links_print(self.links_before_test)


        # host related
        network_topo = topo_res["network-topology"]
        topologys = network_topo["topology"][0]
        if "node" in topologys:
            node = topologys["node"]
        else:
            node = []


        self.host_before_test = host_process(node)
        if self.host_before_test == []:
            print("can not find host message")
        else:
            host_print(self.host_before_test)

        # operational flow related 
        all_operational_flows = operational_flow_aggregation(self.switch_list_before_test,switch_res)
        self.flow_before_test = operational_flow_process(all_operational_flows)
        if  len(self.flow_before_test) == 0:
            print("can not find flow message")
        else:
            operational_flow_print(self.flow_before_test)

        # operational group related 
        all_operational_groups = operational_group_aggregation(self.switch_list_before_test,switch_res)
        self.group_before_test = operational_group_process(all_operational_groups)
        if len(self.group_before_test) == 0:
            print("can not find group message")
        else:
            operational_group_print(self.group_before_test)

        # config meter related 
        all_operational_meters = config_meter_aggregation(self.switch_list_before_test,config_meter_url)
        self.meter_before_test = config_meter_process(all_operational_meters)
        if self.meter_before_test== []:
            print("can not find meter message")
        else:
            config_meter_print(self.meter_before_test)

        new_task = loop.create_task(channel.send_to_controller(data,strategy,switch_handler,odlinfo,switch_handler.controller_result_queue)) 

    async def getSwitchInfoAfterExec(self):
        print("get switch info after exec")
        switch_res = {}
        res = requests.get(url=topo_url,auth=auth_info)
        topo_res = res.json()
        network_topo = topo_res["network-topology"]

        topologys = network_topo["topology"]
        for topology in topologys:
            switches = topology["node"]
            for switch in switches:
                if "host" not in switch["node-id"]:
                    self.switch_list_after_test.append(switch["node-id"])
        print("switch %d %s"%(len(self.switch_list_after_test),self.switch_list_after_test))
        if len(self.switch_list_after_test) != 0:
            print("port no  hwAddr                 portName   portState    portConfig")
        for openflow_switch in self.switch_list_after_test:
            url = "http://"+ controller_ip +":8181/restconf/operational/opendaylight-inventory:nodes/node/"+ openflow_switch
            res = requests.get(url=url,auth=auth_info)
            res = res.json()
            switch_res[openflow_switch] = res
            
            self.port_list_after_test = res["node"][0]["node-connector"]
            for port in self.port_list_after_test:
                if "flow-node-inventory:configuration" in port:
                    port_state = []
                    if port["flow-node-inventory:state"]["link-down"] == True:
                        port_state.append("LINK_DOWN")
                    if port["flow-node-inventory:state"]["live"] == True:
                        port_state.append("LIVE")
                    if port["flow-node-inventory:state"]["blocked"] == True:
                        port_state.append("BLOCKED")
                    port_config = []
                    if port["flow-node-inventory:configuration"] == "":
                        port_config.append("")
                    else:
                        port_config.append(port["flow-node-inventory:configuration"])
                else:
                    port_state = port["flow-node-inventory:state"]
                    port_config = "{}"     
                print("%s        %s      %s     %s    %s"%(port["flow-node-inventory:port-number"],port["flow-node-inventory:hardware-address"],
                port["flow-node-inventory:name"],port_state,port_config))    
        
        # link info
        network_topo = topo_res["network-topology"]
        topologys = network_topo["topology"][0]
        if "links" in topologys.keys():
            links = topologys["link"]
        else:
            links = {}
        if links == {}:
            print("can not find link message")
        else:
            self.links_after_test = links_process(links)
            links_print(self.links_after_test)

        # host related
        network_topo = topo_res["network-topology"]
        topologys = network_topo["topology"][0]
        if "node" in topologys.keys():
            node = topologys["node"]
        else:
            node = []

        self.host_after_test = host_process(node)
        if self.host_after_test == []:
            print("can not find host message")
        else:
            host_print(self.host_after_test)

        # operational flow related 
        all_operational_flows = operational_flow_aggregation(self.switch_list_after_test,switch_res)
        self.flow_after_test = operational_flow_process(all_operational_flows)
        if self.flow_after_test== []:
            print("can not find flow message")
        else:
            operational_flow_print(self.flow_after_test)

        # operational group related 
        all_operational_groups = operational_group_aggregation(self.switch_list_after_test,switch_res)
        self.group_after_test = config_group_process(all_operational_groups)
        if self.group_after_test == []:
            print("can not find group message")
        else:
            config_group_print(self.group_after_test)

        # config meter related 
        all_operational_meters = config_meter_aggregation(self.switch_list_after_test,config_meter_url)
        self.meter_after_test = config_meter_process(all_operational_meters)
        if self.meter_after_test == []:
            print("can not find meter message")
        else:
            config_meter_print(self.meter_after_test)
    

    async def compare_before_and_after(self,odl_controller_result):
        self.controller_result.switch_change = infodifferlist(self.switch_list_before_test,self.switch_list_after_test)
        self.controller_result.port_change = infodifferdict(self.port_list_before_test,self.port_list_after_test)
        self.controller_result.host_change = infodifferdict(self.hosts_before_test,self.hosts_after_test)
        self.controller_result.link_change = infodifferdict(self.links_before_test,self.links_after_test)

        self.controller_result.flow_length_change = infodifferdict(self.flow_before_test,self.flow_after_test)
        self.controller_result.group_length_change = infodifferdict(self.group_before_test,self.group_after_test)
        self.controller_result.meter_length_change = infodifferdict(self.meter_before_test,self.meter_after_test)
        
        self.controller_result.switches_change = infodifferset(self.switches_before_test,self.switches_after_test)

        odl_controller_result.enqueue(self.controller_result)
        self.controller_result.to_str()

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
        message = "odl_appinterface"
        self.writeUTF(sock, message)
        if self.readUTF(sock) =="Hello":
            self.appinterfacestate = APPInterfaceState.HELLO

def getSwitchInfoBeforeExec():
    print("get switch info before exec")
    res = requests.get(url=topo_url,auth=auth_info)
    res = res.json()
    network_topo = res["network-topology"]
    topologys = network_topo["topology"]
    for topology in topologys:
        switches = topology["node"]
        for switch in switches:
            if "host" not in switch["node-id"]:
                switch_list_before_test.append(switch["node-id"].encode("utf-8"))
    print("switch %d %s"%(len(switch_list_before_test),switch_list_before_test))
    if len(switch_list_before_test) != 0:
        print("port no  hwAddr                 portName   portState    portConfig")
    for openflow_switch in  switch_list_before_test:
        url = "http://"+ controller_ip +":8181/restconf/operational/opendaylight-inventory:nodes/node/"+openflow_switch
        ports_res = requests.get(url=url,auth=auth_info)
        ports_res = ports_res.json()
        port_list_before_test = ports_res["node"][0]["node-connector"]
        for port in port_list_before_test:
            if "flow-node-inventory:configuration" in port:
                port_state = []
                if port["flow-node-inventory:state"]["link-down"] == True:
                    port_state.append("LINK_DOWN")
                if port["flow-node-inventory:state"]["live"] == True:
                    port_state.append("LIVE")
                if port["flow-node-inventory:state"]["blocked"] == True:
                    port_state.append("BLOCKED")
                port_config = []
                if port["flow-node-inventory:configuration"] == "":
                    port_config.append("")
                else:
                    port_config.append(port["flow-node-inventory:configuration"])
            else:
                port_state = port["flow-node-inventory:state"]
                port_config = "supported"
            print("%s        %s      %s     %s    %s"%(port["flow-node-inventory:port-number"],port["flow-node-inventory:hardware-address"],
            port["flow-node-inventory:name"],port_state,port_config))    
    
    # link info
    res = requests.get(url=link_url,auth=auth_info)
    res = res.json()
    network_topo = res["network-topology"]
    topologys = network_topo["topology"][0]
    links = topologys["link"]
    if links == {}:
        print("can not find link message")
    else:
        links_before_test = links_process(links)
        links_print(links_before_test)

    # host related
    res = requests.get(url=host_url ,auth=auth_info)
    res = res.json()

    network_topo = res["network-topology"]
    topologys = network_topo["topology"][0]
    node = topologys["node"]

    host_before_test = host_process(node)
    if host_before_test== []:
        print("can not find host message")
    else:
        host_print(host_before_test)

    # config flow related 
    all_config_flows = config_flow_aggregation(switch_list_before_test,config_flow_url)
    config_flow_before_test = config_flow_process(all_config_flows)
    if config_flow_before_test== []:
        print("can not find config flow message")
    else:
        config_flow_print(config_flow_before_test)

    # config group related 
    all_config_groups = config_group_aggregation(switch_list_before_test,config_group_url)
    config_group_before_test = config_group_process(all_config_groups)
    if config_group_before_test== []:
        print("can not find config flow message")
    else:
        config_group_print(config_group_before_test)

    # config meter related 
    all_config_meters = config_meter_aggregation(switch_list_before_test,config_meter_url)
    config_meter_before_test = config_meter_process(all_config_meters)
    if config_meter_before_test== []:
        print("can not find config meter message")
    else:
        config_meter_print(config_meter_before_test)

def getSwitchInfoAfterExec():
    print("get switch info after exec")
    res = requests.get(url=topo_url,auth=auth_info)
    res = res.json()
    network_topo = res["network-topology"]
    topologys = network_topo["topology"]
    for topology in topologys:
        switches = topology["node"]
        for switch in switches:
            if "host" not in switch["node-id"]:
                switch_list_after_test.append(switch["node-id"].encode("utf-8"))
    print("switch %d %s"%(len(switch_list_after_test),switch_list_after_test))
    if len(switch_list_after_test) != 0:
        print("port no  hwAddr                 portName   portState    portConfig")
    for openflow_switch in  switch_list_after_test:
        url = "http://"+ controller_ip +":8181/restconf/operational/opendaylight-inventory:nodes/node/"+openflow_switch
        ports_res = requests.get(url=url,auth=auth_info)
        ports_res = ports_res.json()
        port_list_after_test = ports_res["node"][0]["node-connector"]
        for port in port_list_after_test:
            if "flow-node-inventory:configuration" in port:
                port_state = []
                if port["flow-node-inventory:state"]["link-down"] == True:
                    port_state.append("LINK_DOWN")
                if port["flow-node-inventory:state"]["live"] == True:
                    port_state.append("LIVE")
                if port["flow-node-inventory:state"]["blocked"] == True:
                    port_state.append("BLOCKED")
                port_config = []
                if port["flow-node-inventory:configuration"] == "":
                    port_config.append("")
                else:
                    port_config.append(port["flow-node-inventory:configuration"])
            else:
                port_state = port["flow-node-inventory:state"]
                port_config = "{}"     
            print("%s        %s      %s     %s    %s"%(port["flow-node-inventory:port-number"],port["flow-node-inventory:hardware-address"],
            port["flow-node-inventory:name"],port_state,port_config))    
    
    # link info
    res = requests.get(url=link_url,auth=auth_info)
    res = res.json()
    network_topo = res["network-topology"]
    topologys = network_topo["topology"][0]
    links = topologys["link"]
    if links == {}:
        print("can not find link message")
    else:
        links_after_test = links_process(links)
        links_print(links_after_test)

    # host related
    res = requests.get(url=host_url ,auth=auth_info)
    res = res.json()
    network_topo = res["network-topology"]
    topologys = network_topo["topology"][0]
    node = topologys["node"]
    host_after_test = host_process(node)
    if host_after_test== []:
        print("can not find host message")
    else:
        host_print(host_after_test)

    # config flow related 
    all_config_flows = config_flow_aggregation(switch_list_after_test,config_flow_url)
    config_flow_after_test = config_flow_process(all_config_flows)
    if config_flow_after_test== []:
        print("can not find config flow message")
    else:
        config_flow_print(config_flow_after_test)

    # config group related 
    all_config_groups = config_group_aggregation(switch_list_after_test,config_group_url)
    config_group_after_test = config_group_process(all_config_groups)
    if config_group_after_test== []:
        print("can not find config flow message")
    else:
        config_group_print(config_group_after_test)

    # config meter related 
    all_config_meters = config_meter_aggregation(switch_list_after_test,config_meter_url)
    config_meter_after_test = config_meter_process(all_config_meters)
    if config_meter_after_test== []:
        print("can not find config meter message")
    else:
        config_meter_print(config_meter_after_test)

def links_process(res):
    links = [] 
    for link_from_controller in res:
        link = {}
        source_switch = link_from_controller["source"]["source-node"]
        source_port = link_from_controller["source"]["source-tp"]
        dest_switch = link_from_controller["destination"]["dest-node"]
        dest_port = link_from_controller["destination"]["dest-tp"]
        if "host" not in source_port and "host" not in dest_port:
            link["LINK_SRC_SWITCH"] = source_switch
            link["LINK_SRC_PORT"] = source_port
            link["LINK_DST_SWITCH"] = dest_switch
            link["LINK_DST_PORT"] = dest_port      
            links.append(link)
    return links


def links_print(links):
    count = len(links)
    if count == 0: 
        print("can not find link message")
    for index in range(0,count):
        print("---------------------------------------------------")
        print("LINK INFO FROM CONTROLLER : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("LINK_SRC_SWITCH = {}".format(links[index]["LINK_SRC_SWITCH"]))
        print("LINK_SRC_PORT   = {}".format(links[index]["LINK_SRC_PORT"]))
        print("LINK_DST_SWITCH = {}".format(links[index]["LINK_DST_SWITCH"]))
        print("LINK_DST_PORT   = {}".format(links[index]["LINK_DST_PORT"]))
        print("---------------------------------------------------\n")

def host_process(res):
    hosts = [] 
    for host_from_controller in res:
        host = {}
        if "host-tracker-service:id" in host_from_controller.keys():
            host["HOST_IP"] = host_from_controller["host-tracker-service:addresses"][0]["ip"]
            host["HOST_MAC"] = host_from_controller["host-tracker-service:addresses"][0]["mac"]
            # only attach port in response body so we should combinate the attach switch info
            attach_port = host_from_controller["host-tracker-service:attachment-points"][0]["tp-id"]
            attach_switch = attach_port.split(":")[0]+":"+attach_port.split(":")[1]
            host["ATTACH_SWITCH"] = attach_switch
            host["ATTACH_PORT"] = attach_port       
            hosts.append(host)
    return hosts

def host_print(hosts):
    count = len(hosts)
    if count == 0: 
        print("can not find host message")
    for index in range(0,count):
        print("---------------------------------------------------")
        print("HOST INFO FROM CONTROLLER : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("HOST_IP       = {}".format(hosts[index]["HOST_IP"]))
        print("HOST_MAC      = {}".format(hosts[index]["HOST_MAC"]))
        print("ATTACH_SWITCH = {}".format(hosts[index]["ATTACH_SWITCH"]))
        print("ATTACH_PORT   = {}".format(hosts[index]["ATTACH_PORT"]))
        print("---------------------------------------------------\n")

def config_flow_aggregation(switches,config_flow_url):
    all_flows = []
    for switch in switches:
        switch_flow_url = config_flow_url + str(switch)
        res = requests.get(url=switch_flow_url,auth=auth_info)
        if res.status_code == 404:
            continue
        res = res.json()
        node = res["node"]
        flow_entry_list = node[0]["flow-node-inventory:table"]
        for flow_from_diffrent_table in flow_entry_list:
            flows = flow_from_diffrent_table["flow"]
            for flow in flows:     
                flow["switch"] = switch
                all_flows.append(flow)
    return all_flows

def config_flow_process(res):
    flow_list = []
    for flow_from_stats in res:
        flow = {}
        flow["SWITCH"] =  flow_from_stats["switch"]
        flow["TABLE ID"] = flow_from_stats["table_id"]
        flow["PRIORITY"] = flow_from_stats["priority"]
        flow["MATCH"]= flow_from_stats["match"]
        flow["ACTIONS"]= flow_from_stats["instructions"]
        flow_list.append(flow)
    return flow_list

def config_flow_print(flows):
    count = len(flows)
    for index in range(0,count):
        print("---------------------------------------------------")
        print("FLOW INFO FROM CONTROLLER (CONFIG) : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH   = {}".format(flows[index]["SWITCH"]))
        print("TABLE ID = {}".format(flows[index]["TABLE ID"]))
        print("PRIORITY = {}".format(flows[index]["PRIORITY"]))
        print("MATCH    = {}".format(flows[index]["MATCH"]))
        print("ACTIONS  = {}".format(flows[index]["ACTIONS"]))
        print("---------------------------------------------------")
        print("")

def operational_flow_aggregation(switches,switch_res):
    all_flows = []
    for switch in switches:
        node = switch_res[switch]["node"]
        flow_entry_list = node[0]["flow-node-inventory:table"]
        for flow_from_diffrent_table in flow_entry_list:
            if flow_from_diffrent_table["opendaylight-flow-table-statistics:flow-table-statistics"]["active-flows"] == 0:
                continue
            flows = flow_from_diffrent_table["flow"]
            for flow in flows:
                flow["switch"] = switch
                all_flows.append(flow)
    return all_flows

def operational_flow_process(res):
    flow_list = []
    for flow_from_stats in res:
        flow = {}
        flow["SWITCH"] =  flow_from_stats["switch"]
        flow["TABLE ID"] = flow_from_stats["table_id"]
        flow["PRIORITY"] = flow_from_stats["priority"]
        if "match" in flow_from_stats.keys():
            flow["MATCH"]= flow_from_stats["match"]
        else:
            flow["MATCH"]= {}
        if "instructions" in flow_from_stats.keys():
            flow["ACTIONS"]= flow_from_stats["instructions"]
        else:
            flow["ACTIONS"]= {}
        flow_list.append(flow)
    return flow_list

def operational_flow_print(flows):
    count = len(flows)
    for index in range(0,count):
        print("---------------------------------------------------")
        print("FLOW INFO FROM CONTROLLER (OPERATIONAL) : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH   = {}".format(flows[index]["SWITCH"]))
        print("TABLE ID = {}".format(flows[index]["TABLE ID"]))
        print("PRIORITY = {}".format(flows[index]["PRIORITY"]))
        print("MATCH    = {}".format(flows[index]["MATCH"]))
        print("ACTIONS  = {}".format(flows[index]["ACTIONS"]))
        print("---------------------------------------------------")
        print("")

def config_group_aggregation(switches,config_group_url):
    all_groups = []
    for switch in switches:
        switch_group_url = config_group_url + str(switch)
        res = requests.get(url=switch_group_url,auth=auth_info)
        if res.status_code == 404:
            continue
        res = res.json()
        node = res["node"]
        group_entry_list = node[0]["flow-node-inventory:group"]
        for group in group_entry_list:     
            group["switch"] = switch
            all_groups.append(group)
    return all_groups

def config_group_process(res):
    group_list = []
    for group_from_stats in res:
        group = {}
        group["SWITCH"] =  group_from_stats["switch"]
        group["GROUP ID"] = group_from_stats["group-id"]
        group["GROUP TYPE"] = group_from_stats["group-type"]
        group["BUCKETS"]= group_from_stats["buckets"]
        group_list.append(group)
    return group_list

def config_group_print(groups):
    count = len(groups)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" GROUP INFO FROM CONTROLLER (CONFIG) : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH     = {}".format(groups[index]["SWITCH"]))
        print("GROUP ID   = {}".format(groups[index]["GROUP ID"]))
        print("GROUP TYPE = {}".format(groups[index]["GROUP TYPE"]))
        print("BUCKETS    = {}".format(groups[index]["BUCKETS"]))
        print("---------------------------------------------------")
        print("")   

def operational_group_aggregation(switches,switch_res):
    all_groups = []
    for switch in switches:
        node = switch_res[switch]["node"]
        switch_info = switch_res[switch]["node"][0]
        if "flow-node-inventory:group" not in switch_info.keys():
            continue
        group_entry_list = node[0]["flow-node-inventory:group"]
        for group in group_entry_list:     
            group["switch"] = switch
            all_groups.append(group)
    return all_groups

def operational_group_process(res):
    group_list = []
    for group_from_stats in res:
        group = {}
        group["SWITCH"] =  group_from_stats["switch"]
        group["GROUP ID"] = group_from_stats["group-id"]
        group["GROUP TYPE"] = group_from_stats["group-type"]
        group["BUCKETS"]= group_from_stats["buckets"]
        group_list.append(group)
    return group_list

def operational_group_print(groups):
    count = len(groups)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" GROUP INFO FROM CONTROLLER (OPERATIONAL) : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH     = {}".format(groups[index]["SWITCH"]))
        print("GROUP ID   = {}".format(groups[index]["GROUP ID"]))
        print("GROUP TYPE = {}".format(groups[index]["GROUP TYPE"]))
        print("BUCKETS    = {}".format(groups[index]["BUCKETS"]))
        print("---------------------------------------------------")
        print("")   

def config_meter_aggregation(switches,config_meter_url):
    all_meters = []
    for switch in switches:
        switch_meter_url = config_meter_url + str(switch)
        res = requests.get(url=switch_meter_url,auth=auth_info)
        if res.status_code == 404:
            continue
        res = res.json()
        node = res["node"]
        meter_entry_list = node[0]["flow-node-inventory:meter"]
        for meter in meter_entry_list:     
            meter["switch"] = switch
            all_meters.append(meter)
    return all_meters

def config_meter_process(res):
    meter_list = []
    for meter_from_controller_config in res:
        meter = {}
        meter["SWITCH"] =  meter_from_controller_config["switch"]
        meter["METER ID"] = meter_from_controller_config["meter-id"]
        meter["METER FLAGS"] = meter_from_controller_config["flags"]
        meter["METER BANDS"]= meter_from_controller_config["meter-band-headers"]["meter-band-header"]
        meter_list.append(meter)
    return meter_list

def config_meter_print(meters):
    count = len(meters)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" METER INFO FROM CONTROLLER (CONFIG) : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH      = {}".format(meters[index]["SWITCH"]))
        print("METER ID    = {}".format(meters[index]["METER ID"]))
        print("METER FLAGS = {}".format(meters[index]["METER FLAGS"]))
        print("METER BANDS = {}".format(meters[index]["METER BANDS"]))
        print("---------------------------------------------------")
        print("") 

def operational_meter_aggregation(switches,switch_res):
    all_meters = []
    for switch in switches:
        node = switch_res[switch]["node"]
        meter_entry_list = node[0]["flow-node-inventory:meter"]
        for meter in meter_entry_list:     
            meter["switch"] = switch
            all_meters.append(meter)
    return all_meters

def operational_meter_process(res):
    meter_list = []
    for meter_from_controller_config in res:
        meter = {}
        meter["SWITCH"] =  meter_from_controller_config["switch"]
        meter["METER ID"] = meter_from_controller_config["meter-id"]
        meter["METER FLAGS"] = meter_from_controller_config["flags"]
        meter["METER BANDS"]= meter_from_controller_config["meter-band-headers"]["meter-band-header"]
        meter_list.append(meter)
    return meter_list

def operational_meter_print(meters):
    count = len(meters)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" METER INFO FROM CONTROLLER (OPERATIONAL) : COUNT = {}".format(index+1))
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
        print("[AppInterface] error: "+traceback.format_exc())
    finally:
        time.sleep(5)