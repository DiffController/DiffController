
"""Custom topology example

Three directly connected switches plus a host for each switch , only switch1 connect to controller:

   h1 ---switch1 --- h2

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'onos-h1',ip='10.0.0.1')
        h2 = self.addHost( 'onos-h2',ip='10.0.0.2')
        s1 = self.addSwitch('onos-s1', dpid='1')


        # Add links
        # links between host and switch
        self.addLink(s1,h1)
        self.addLink(s1,h2)


        # links between switch

        # Add controller

topos = { 'mytopo': ( lambda: MyTopo() ) }
