# encoding=utf-8
import networkx as nx

def topo_file_build(filename,switches,hosts,switch2switchlinks,switch2hostlinks,controller_type):
    f = open(filename,'wb')
    # build annotation
    f.write(b"#!/usr/bin/python\n\n")
    f.write(b"\"\"\"Custom topology example\n")
    f.write(b"Adding the 'topos' dict with a key/value pair to generate our newly defined\n")
    f.write(b"topology enables one to pass in '--topo=mytopo' from the command line.\n")
    f.write(b"\"\"\"\n\n")

    # build import
    f.write(b"from mininet.topo import Topo\n")

    f.write(b"\n")

    # build topo class
    f.write(b"class MyTopo( Topo ):\n")
    f.write(b"    \"Simple topology example.\"\n")
    f.write(b"\n")

    f.write(b"    def build( self ):\n")
    f.write(b"        \"Create custom topo.\"\n")
    f.write(b"\n")
    
    # Add hosts and switches
    f.write(b"        # Add hosts and switches\n")
    dpid = 1
    for switch in switches:
        write_switch(f,switch,controller_type,dpid)
        dpid = dpid + 1
    
    ip = 1
    for host in hosts:
        write_host(f,host,controller_type,ip)
        ip = ip + 1

    # links between host and switch
    f.write(b"\n")
    f.write(b"        # Add links\n")
    f.write(b"        # links between host and switch\n")
    for link in switch2hostlinks:
        write_link_host_switch(f,link)

    # links between switch
    f.write(b"\n")
    f.write(b"        # links between switch\n")         
    for link in switch2switchlinks:
        write_link_between_switch(f,link)

    # build file end 
    f.write(b"\n")
    f.write(b"topos = { 'mytopo': ( lambda: MyTopo() ) }")

def ReadDotFile (path):
    # read .dot (pydot)
    topo = nx.drawing.nx_pydot.read_dot(path)
    topo = nx.Graph(topo)
    return topo

def DrawTopo (topo, filename):
    topograph = nx.drawing.nx_agraph.to_agraph(topo)
    topograph.layout('dot')
    topograph.draw(filename)

def topoprocess(topo) :
    switches = []
    hosts = []
    switch2hostlink = []
    switch2switchlink = []
    for node in topo.nodes():
        if "s" in node :
            switches.append(node)
        elif "h" in node :
            hosts.append(node)
    
    for edges in topo.edges():
        if edges[0] in switches and edges[1] in switches:
            switch2switchlink.append(edges)
        elif edges[0] in switches and edges[1] in hosts:
            switch2hostlink.append(edges)
        elif edges[1] in switches and edges[0] in hosts:
            switch2hostlink.append(edges)

    return switches,hosts,switch2hostlink,switch2switchlink

def write_switch(f,switch,controller_type,dpid):
    dpid = str(dpid)
    switch_command = "        "+switch+" = self.addSwitch('"+controller_type+"-"+switch+"', dpid='"+dpid+"')\n"
    switch_command = bytes(switch_command, encoding = "utf-8")
    f.write(switch_command)

def write_host(f,host,controller_type,ip):
    ip_base = "10.0.0."
    ip = ip_base + str(ip)
    host_command = "        "+host+" = self.addHost('"+controller_type+"-"+host+"', ip='"+ip+"')\n"
    host_command = bytes(host_command, encoding = "utf-8")
    f.write(host_command)

def write_link_between_switch(f,link):
    link_command = "        self.addLink("+link[0]+","+link[1]+")\n"
    link_command = bytes(link_command, encoding = "utf-8")
    f.write(link_command)

def write_link_host_switch(f,link):
    link_command = "        self.addLink("+link[0]+","+link[1]+")\n"
    link_command = bytes(link_command, encoding = "utf-8")
    f.write(link_command)

if __name__ == '__main__':
    switches = []
    hosts = []
    switch2hostlinks = []
    switch2switchlinks = []
    controller_type_list = ["ryu","fl","onos","odl"]
    topo = ReadDotFile("networktopo.dot")
    switches,hosts,switch2hostlinks,switch2switchlinks = topoprocess(topo)

    for controller_type in controller_type_list:
        output_filename = controller_type+"_same_topo.py"
        topo_file_build(output_filename,switches,hosts,switch2switchlinks,switch2hostlinks,controller_type)
    

