# coding:utf8
import struct
import socket
import requests
from enum import Enum
import sys
import time
from socket import error as socket_error
import errno
import urllib

from RestAPP.ControllerResult import ControllerResult
from RestAPP.listcompare import infodifferdict,infodifferlist,infodifferset

controller_ip = '172.17.0.4'

devices_url = "http://" + controller_ip +":8181/onos/v1/devices"

# default cluster id = 0 , but cluster maybe 1 if new switch added
link_url = "http://" + controller_ip +":8181/onos/v1/topology/clusters/1/links"

host_url = "http://" + controller_ip +":8181/onos/v1/hosts"

flow_url = "http://" + controller_ip +":8181/onos/v1/flows"
group_url = "http://" + controller_ip +":8181/onos/v1/groups"
meter_url = "http://" + controller_ip +":8181/onos/v1/meters"

headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json'}
server_address = ('127.0.0.1', 3456)
auth_info = ('onos','rocks')

# collected info before & after test case
switch_list_before_test = []
switch_list_after_test = []
port_list_before_test = []
port_list_after_test = []
links_before_test = []
links_after_test = []
host_before_test = []
host_after_test = []
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
        message = "onos_appinterface"
        print(message)
        self.writeUTF(sock, message)
        if self.readUTF(sock) =="Hello":
            self.appinterfacestate = APPInterfaceState.HELLO

class OnosInfo():
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

        self.controller_result = ControllerResult("ONOS")

    async def getSwitchInfoBeforeExec(self,loop,channel,data,strategy,onosinfo,switch_handler):
        print("get switch info before exec")
        res = requests.get(url=devices_url,auth=auth_info)
        res = res.json()
        devices = res["devices"]
        for device in devices:
            if device["available"] ==True and device["type"] == "SWITCH":
                self.switch_list_before_test.append(device["id"])
        print("switch %d %s"%(len(self.switch_list_before_test),self.switch_list_before_test))
        if len(self.switch_list_before_test) != 0:
            print("port no  hwAddr                 portName   adminState")
        for switch in  self.switch_list_before_test:
            url = "http://"+ controller_ip +":8181/onos/v1/devices/"+switch+"/ports"
            ports_res = requests.get(url=url,auth=auth_info)
            ports_res = ports_res.json()
            self.port_list_before_test = ports_res["ports"]
            for port in self.port_list_before_test:
                print("%s        %s      %s     %s"%(port["port"],port["annotations"]["portMac"],port["annotations"]["portName"],port["annotations"]["adminState"]))

        
        # query and print link info , and need auth info 
        res = requests.get(url=link_url,auth=auth_info)
        res = res.json()

        if 'code' in res.keys() and res['code']==404:
            print("can not find link message")
        else:
            self.links_before_test = links_process(res)
            links_print(self.links_before_test)

        # host related
        res = requests.get(url=host_url,auth=auth_info)
        res = res.json()
        res = res["hosts"]
        if res == []:
            print("can not find host message")
        else:
            self.host_before_test = host_process(res)
            host_print(self.host_before_test)

        # flow related
        res = requests.get(url=flow_url,auth=auth_info)
        res = res.json()
        self.flow_before_test = res["flows"]
        if len(self.flow_before_test) == 0:
            print("can not find flow info")
        else:
            self.flow_before_test = flow_process(self.flow_before_test,self.switch_list_before_test)
            flow_print(self.flow_before_test)

        # group related
        res = requests.get(url=group_url,auth=auth_info)
        res = res.json()
        self.group_before_test = res["groups"]
        if len(self.group_before_test) == 0:
            print("can not find group info")
        else:
            self.group_before_test = group_process(self.group_before_test,self.switch_list_before_test)
            group_print(self.group_before_test)

        # meter related
        res = requests.get(url=meter_url,auth=auth_info)
        res = res.json()
        self.meter_before_test = res["meters"]
        if len(self.meter_before_test) == 0:
            print("can not find meter info")
        else:
            self.meter_before_test = meter_process(self.meter_before_test,self.switch_list_before_test)
            meter_print(self.meter_before_test)
        
        new_task = loop.create_task(channel.send_to_controller(data,strategy,switch_handler,onosinfo,switch_handler.controller_result_queue)) 

    async def getSwitchInfoAfterExec(self):
        print("get switch info after exec")
        res = requests.get(url=devices_url,auth=auth_info)
        res = res.json()
        devices = res["devices"]
        for device in devices:
            if device["available"] ==True and device["type"] == "SWITCH":
                self.switch_list_after_test.append(device["id"])
        print("switch %d %s"%(len(self.switch_list_after_test),self.switch_list_after_test))
        if len(self.switch_list_after_test) != 0:
            print("port no  hwAddr                 portName   adminState")
        for switch in self.switch_list_after_test:
            url = "http://"+controller_ip+":8181/onos/v1/devices/"+switch+"/ports"
            ports_res = requests.get(url=url,auth=auth_info)
            ports_res = ports_res.json()
            self.port_list_after_test = ports_res["ports"]
            for port in self.port_list_after_test:
                print("%s        %s      %s     %s"%(port["port"],port["annotations"]["portMac"],port["annotations"]["portName"],port["annotations"]["adminState"]))

        # query and print link info , and need auth info
        res = requests.get(url=link_url,auth=auth_info)
        res = res.json()

        if 'code' in res.keys() and res['code']==404:
            print("can not find link message")
        else:
            self.links_after_test = links_process(res)
            links_print(self.links_after_test)

        # host related
        res = requests.get(url=host_url,auth=auth_info)
        res = res.json()
        res = res["hosts"]
        
        if res == []:
            print("can not find host message")
        else:
            self.host_after_test = host_process(res)
            host_print(self.host_after_test)

        # flow related
        res = requests.get(url=flow_url,auth=auth_info)
        res = res.json()
        self.flow_after_test = res["flows"]
        if len(self.flow_after_test) == 0:
            print("can not find flow info")
        else:
            self.flow_after_test = flow_process(self.flow_after_test,self.switch_list_after_test)
            flow_print(self.flow_after_test)

        # group related
        res = requests.get(url=group_url,auth=auth_info)
        res = res.json()
        self.group_after_test = res["groups"]
        if len(self.group_after_test) == 0:
            print("can not find group info")
        else:
            self.group_after_test = group_process(self.group_after_test,self.switch_list_after_test)
            group_print(self.group_after_test)

        # meter related
        res = requests.get(url=meter_url,auth=auth_info)
        res = res.json()
        self.meter_after_test = res["meters"]
        if len(self.meter_after_test) == 0:
            print("can not find meter info")
        else:
            self.meter_after_test = meter_process(self.meter_after_test,self.switch_list_after_test)
            meter_print(self.meter_after_test)

    async def compare_before_and_after(self,onos_controller_result):
        self.controller_result.switch_change = infodifferlist(self.switch_list_before_test,self.switch_list_after_test)
        self.controller_result.port_change = infodifferdict(self.port_list_before_test,self.port_list_after_test)
        self.controller_result.host_change = infodifferdict(self.hosts_before_test,self.hosts_after_test)
        self.controller_result.link_change = infodifferdict(self.links_before_test,self.links_after_test)
        self.controller_result.flow_length_change = infodifferdict(self.flow_before_test,self.flow_after_test)
        self.controller_result.group_length_change = infodifferdict(self.group_before_test,self.group_after_test)
        self.controller_result.meter_length_change = infodifferdict(self.meter_before_test,self.meter_after_test)
        self.controller_result.switches_change = infodifferset(self.switches_before_test,self.switches_after_test)

        onos_controller_result.enqueue(self.controller_result)
        self.controller_result.to_str()

def getSwitchInfoBeforeExec():
    print("get switch info before exec")

    res = requests.get(url=devices_url,auth=auth_info)
    res = res.json()
    devices = res["devices"]
    for device in devices:
        if device["available"] ==True and device["type"] == "SWITCH":
            switch_list_before_test.append(device["id"].encode("utf-8"))
    print("switch %d %s"%(len(switch_list_before_test),switch_list_before_test))
    if len(switch_list_before_test) != 0:
        print("port no  hwAddr                 portName   adminState")
    for switch in  switch_list_before_test:
        url = "http://127.0.0.1:8181/onos/v1/devices/"+urllib.quote(switch)+"/ports"
        ports_res = requests.get(url=url,auth=auth_info)
        ports_res = ports_res.json()
        port_list_before_test = ports_res["ports"]
        for port in port_list_before_test:
            print("%s        %s      %s     %s"%(port["port"],port["annotations"]["portMac"],port["annotations"]["portName"],port["annotations"]["adminState"]))

    # query and print link info , and need auth info 
    res = requests.get(url=link_url,auth=auth_info)
    res = res.json()

    if res == {"links":[]}:
        print("can not find link message")
    else:
        links_before_test = links_process(res)
        links_print(links_before_test)

    # host related
    res = requests.get(url=host_url,auth=auth_info)
    res = res.json()
    res = res["hosts"]
    if res == []:
        print("can not find host message")
    else:
        host_before_test = host_process(res)
        host_print(host_before_test)

    # flow related
    res = requests.get(url=flow_url,auth=auth_info)
    res = res.json()
    flow_before_test = res["flows"]
    if len(flow_before_test) == 0:
        print("can not find flow info")
    else:
        flow_before_test = flow_process(flow_before_test,switch_list_before_test)
        flow_print(flow_before_test)

   # group related
    res = requests.get(url=group_url,auth=auth_info)
    res = res.json()
    group_before_test = res["groups"]
    if len(group_before_test) == 0:
        print("can not find group info")
    else:
        group_before_test = group_process(group_before_test,switch_list_before_test)
        group_print(group_before_test)

   # meter related
    res = requests.get(url=meter_url,auth=auth_info)
    res = res.json()
    meter_before_test = res["meters"]
    if len(meter_before_test) == 0:
        print("can not find group info")
    else:
        meter_before_test = meter_process(meter_before_test,switch_list_before_test)
        meter_print(meter_before_test)

def getSwitchInfoAfterExec():
    print("get switch info after exec")
    res = requests.get(url=devices_url,auth=auth_info)
    res = res.json()
    devices = res["devices"]
    for device in devices:
        if device["available"] ==True and device["type"] == "SWITCH":
            switch_list_after_test.append(device["id"].encode("utf-8"))
    print("switch %d %s"%(len(switch_list_after_test),switch_list_after_test))
    if len(switch_list_after_test) != 0:
        print("port no  hwAddr                 portName   adminState")
    for switch in  switch_list_after_test:
        url = "http://127.0.0.1:8181/onos/v1/devices/"+urllib.quote(switch)+"/ports"
        ports_res = requests.get(url=url,auth=auth_info)
        ports_res = ports_res.json()
        port_list_after_test = ports_res["ports"]
        for port in port_list_after_test:
            print("%s        %s      %s     %s"%(port["port"],port["annotations"]["portMac"],port["annotations"]["portName"],port["annotations"]["adminState"]))

    # query and print link info , and need auth info
    res = requests.get(url=link_url,auth=auth_info)
    res = res.json()

    if res == {"links":[]}:
        print("can not find link message")
    else:
        links_after_test = links_process(res)
        links_print(links_after_test)

    # host related
    res = requests.get(url=host_url,auth=auth_info)
    res = res.json()
    res = res["hosts"]
    
    if res == []:
        print("can not find host message")
    else:
        host_after_test = host_process(res)
        host_print(host_after_test)

    # flow related
    res = requests.get(url=flow_url,auth=auth_info)
    res = res.json()
    flow_after_test = res["flows"]

    if len(flow_after_test) == 0:
        print("can not find flow info")
    else:
        flow_after_test = flow_process(flow_after_test,switch_list_after_test)
        flow_print(flow_after_test)

   # group related
    res = requests.get(url=group_url,auth=auth_info)
    res = res.json()
    group_after_test = res["groups"]

    if len(group_after_test) == 0:
        print("can not find group info")
    else:
        group_after_test = group_process(group_after_test,switch_list_after_test)
        group_print(group_after_test)

   # meter related
    res = requests.get(url=meter_url,auth=auth_info)
    res = res.json()
    meter_after_test = res["meters"]

    if len(meter_after_test) == 0:
        print("can not find group info")
    else:
        meter_after_test = meter_process(meter_after_test,switch_list_after_test)
        meter_print(meter_after_test)

def links_process(res):
    link = {}
    links = [] 
    for link_from_controller in res["links"]:
        link["LINK_SRC_SWITCH"] = link_from_controller["src"]["device"]
        link["LINK_SRC_PORT"] = link_from_controller["src"]["port"]
        link["LINK_DST_SWITCH"] = link_from_controller["dst"]["device"]
        link["LINK_DST_PORT"] = link_from_controller["dst"]["port"]        
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
        host["HOST_IP"] = host_from_controller["ipAddresses"][0]
        host["HOST_MAC"] = host_from_controller["mac"]
        host["ATTACH_SWITCH"] = host_from_controller["locations"][0]["elementId"]
        host["ATTACH_PORT"] = host_from_controller["locations"][0]["port"]        
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

def flow_process(res,switch_list):
    flow_list = []
    for flow_from_stats in res:
        flow = {}
        if flow_from_stats["deviceId"] in switch_list:
            flow["SWITCH"] =  flow_from_stats["deviceId"]
            flow["TABLE ID"] = flow_from_stats["tableId"]
            flow["PRIORITY"] = flow_from_stats["priority"]
            flow["MATCH"]= flow_from_stats["selector"]["criteria"]
            flow["ACTIONS"]= flow_from_stats["treatment"]["instructions"]
            flow_list.append(flow)
    return flow_list

def flow_print(flows):
    count = len(flows)
    for index in range(0,count):
        print("---------------------------------------------------")
        print("FLOW INFO FROM CONTROLLER : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH   = {}".format(flows[index]["SWITCH"]))
        print("TABLE ID = {}".format(flows[index]["TABLE ID"]))
        print("PRIORITY = {}".format(flows[index]["PRIORITY"]))
        print("MATCH    = {}".format(flows[index]["MATCH"]))
        print("ACTIONS  = {}".format(flows[index]["ACTIONS"]))
        print("---------------------------------------------------")
        print("")

def group_process(res,switch_list):
    group_list = []
    for group_from_stats in res:
        if group_from_stats["deviceId"] in switch_list:
            group = {}
            group["SWITCH"] =  group_from_stats["deviceId"]
            group["GROUP ID"] = group_from_stats["id"]
            group["GROUP TYPE"] = group_from_stats["type"]
            group["BUCKETS"]= group_from_stats["buckets"]
            group_list.append(group)
    return group_list

def group_print(groups):
    count = len(groups)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" GROUP INFO FROM CONTROLLER : COUNT = {}".format(index+1))
        print("---------------------------------------------------")
        print("SWITCH     = {}".format(groups[index]["SWITCH"]))
        print("GROUP ID   = {}".format(groups[index]["GROUP ID"]))
        print("GROUP TYPE = {}".format(groups[index]["GROUP TYPE"]))
        print("BUCKETS    = {}".format(groups[index]["BUCKETS"]))
        print("---------------------------------------------------")
        print("")   

def meter_process(res,switch_list):
    meter_list = []
    for meter_from_stats in res:
        meter = {}
        if meter_from_stats["deviceId"] in switch_list:
            meter["SWITCH"] =  meter_from_stats["deviceId"]
            meter["METER ID"] = meter_from_stats["id"] 
            if meter_from_stats["burst"] == "true":
                meter["METER FLAGS"] = [meter_from_stats["unit"],"BURST"]
            else:
                meter["METER FLAGS"] = [meter_from_stats["unit"]]
            meter["METER BANDS"]= meter_from_stats["bands"]
            meter_list.append(meter)
    return meter_list

def meter_print(meters):
    count = len(meters)
    for index in range(0,count):
        print("---------------------------------------------------")
        print(" METER INFO FROM CONTROLLER : COUNT = {}".format(index+1))
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