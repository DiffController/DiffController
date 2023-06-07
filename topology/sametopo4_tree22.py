
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
        h1 = self.addHost( 'odl-h1',ip='10.0.0.1')
        h2 = self.addHost( 'odl-h2',ip='10.0.0.2')
        h3 = self.addHost( 'odl-h3',ip='10.0.0.3')
        h4 = self.addHost( 'odl-h4',ip='10.0.0.4')
        s1 = self.addSwitch('odl-s1', dpid='1')
        s2 = self.addSwitch('odl-s2', dpid='2')
        s3 = self.addSwitch('odl-s3', dpid='3')


        # Add links
        # links between host and switchs
        self.addLink(s2,h1)
        self.addLink(s2,h2)
        self.addLink(s3,h3)
        self.addLink(s3,h4)


        # links between switch
        self.addLink(s1,s2)
        self.addLink(s1,s3)


        # Add controller

topos = { 'mytopo': ( lambda: MyTopo() ) }
