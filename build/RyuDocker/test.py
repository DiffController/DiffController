import json
import sys

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller import dpset
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.app.wsgi import ControllerBase
from ryu.app.wsgi import Response
from ryu.app.wsgi import route
from ryu.app.wsgi import WSGIApplication
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib import dpid as dpid_lib
from ryu.topology.api import get_switch, get_link, get_host

simple_switch_test_instance_name = 'test'
switch_and_port_url = '/collectswithes/switcheslist/json'
hosts_url =  '/hosts/json'

class ExampleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    
    _CONTEXTS = {
        'dpset':dpset.DPSet,
        'wsgi': WSGIApplication
    }
    
    def __init__(self, *args, **kwargs):
        super(ExampleSwitch13, self).__init__(*args, **kwargs)
        # initialize mac address table.
        self.mac_to_port = {}
        self.dpset = kwargs['dpset']
        wsgi = kwargs['wsgi']
        wsgi.register(SimpleSwitchController,
                      {simple_switch_test_instance_name: self})

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # install the table-miss flow entry.
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)
        
        role_req = parser.OFPRoleRequest(datapath, ofproto.OFPCR_ROLE_NOCHANGE, 0x05)
        datapath.send_msg(role_req)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # construct flow_mod message and send it.
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # get Datapath ID to identify OpenFlow switches.
        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})

        # analyse the received packets using the packet library.
        pkt = packet.Packet(msg.data)
        eth_pkt = pkt.get_protocol(ethernet.ethernet)
        dst = eth_pkt.dst
        src = eth_pkt.src

        # get the received port number from packet_in message.
        in_port = msg.match['in_port']

        self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

        # learn a mac address to avoid FLOOD next time.
        self.mac_to_port[dpid][src] = in_port

        # if the destination mac address is already learned,
        # decide which port to output the packet, otherwise FLOOD.
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        # construct action list.
        actions = [parser.OFPActionOutput(out_port)]

        # install a flow to avoid packet_in next time.
        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)

        # construct packet_out message and send it.
        out = parser.OFPPacketOut(datapath=datapath,
                                  buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=in_port, actions=actions,
                                  data=msg.data)
        datapath.send_msg(out)

    @set_ev_cls(ofp_event.EventOFPPortDescStatsReply, MAIN_DISPATCHER)
    def port_desc_statics(self,ev):
        dpid = 1
        dp = self.dpset.get(dpid)
        # print(self.dpset.get_all())
        for i in self.dpset.get_all():
            self.logger.info(str(i[1].__dict__))
        if dp is None:
            self.logger.info('No such datapath:dpid = %d',dpid)
        else:
            self.logger.info(dp.__dict__['ports'])   
    
    @set_ev_cls(ofp_event.EventOFPPortStatus, MAIN_DISPATCHER)
    def port_status_change(self,ev):
        dpid = 1
        dp = self.dpset.get(dpid)
        for i in self.dpset.get_all():
            self.logger.info(str(i[1].__dict__))
        if dp is None:
            self.logger.info('No such datapath:dpid = %d',dpid)
        else:
            self.logger.info(dp.__dict__['ports'])

class SimpleSwitchController(ControllerBase):
    
    def __init__(self, req, link, data, **config):
        super(SimpleSwitchController,self).__init__(req, link, data, **config)
        self.simple_switch_app = data[simple_switch_test_instance_name]

    @route('collectswitchinfo',switch_and_port_url, methods=['GET'],)
    def get_switches_info(self,req,**kwargs):
        print("received http request")
        response_switch_info = {}
        for dpinstance in self.simple_switch_app.dpset.get_all():  
            dpid = dpinstance[0]
            response_port_list = []
            for port in self.simple_switch_app.dpset.get_ports(dpid):
                response_port_list.append(port.to_jsondict()['OFPPort'])
            response_switch_info[dpid] = response_port_list

        body = json.dumps(response_switch_info)
        return Response(content_type='application/json', body=body)

    @route('collecthostinfo',hosts_url, methods=['GET'],)
    def get_hosts_info(self,req,**kwargs):
        host_list = []
        for dpinstance in self.simple_switch_app.dpset.get_all():
            dpid = dpinstance[0]
            hosts = get_host(self.simple_switch_app,dpid)
            self.simple_switch_app.logger.info("hosts:{}".format(hosts))
            for host in hosts:
                attach_host = {}
                attach_host["mac"] = host.__dict__["mac"]
                if host.__dict__["ipv4"] == []:
                    attach_host["ipv4"] = []
                else:
                     attach_host["ipv4"] = host.__dict__["ipv4"]
                attach_point_obj = host.__dict__["port"]
                attachment = attach_point_obj.__dict__
                attach_host["dpid"] = attachment["dpid"]
                attach_host["port_no"] = attachment["port_no"]
                host_list.append(attach_host)
        body = json.dumps(host_list)
        return Response(content_type='application/json', body=body)
