from mininet.topo import Topo

class MyTopo( Topo ) :
    def __init__( self ) :
        Topo.__init__( self )
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        serv0 = self.addHost( 'sv0' )
        serv1 = self.addHost( 'sv1' )
        switch0 = self.addSwitch( 's0' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        snort = self.addHost( 'snort' )
        self.addLink(host1,switch1)
        self.addLink(host2,switch1)
        self.addLink(host3,switch1)
        self.addLink(host4,switch1)
        self.addLink(serv0,switch2)
        self.addLink(serv1,switch2)
        self.addLink(switch1,switch0)
        self.addLink(switch2,switch0)
        self.addLink(switch0,snort)

topos = { 'mytopo': (lambda: MyTopo() ) }


