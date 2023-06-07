#!/usr/bin/python

"""Custom topology example
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        s1 = self.addSwitch('onos-s1', dpid='1')
        s2 = self.addSwitch('onos-s2', dpid='2')
        s3 = self.addSwitch('onos-s3', dpid='3')
        s4 = self.addSwitch('onos-s4', dpid='4')
        h1 = self.addHost('onos-h1', ip='10.0.0.1')
        h2 = self.addHost('onos-h2', ip='10.0.0.2')
        h3 = self.addHost('onos-h3', ip='10.0.0.3')
        h4 = self.addHost('onos-h4', ip='10.0.0.4')

        # Add links
        # links between host and switch
        self.addLink(s1,h1)
        self.addLink(s2,h2)
        self.addLink(s3,h3)
        self.addLink(s4,h4)

        # links between switch
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s3,s4)

topos = { 'mytopo': ( lambda: MyTopo() ) }