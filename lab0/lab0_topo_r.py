
#!/usr/bin/env python Sonet

from mininet.topo import Topo # Base class for creating custom network topologies.
from mininet.net import Mininet #  Main class to create and manage the network.
from mininet.node import OVSBridge # Class representing an OpenFlow switch using Open vSwitch.
from mininet.link import TCLink # Class for creating links with traffic control (tc) support.
from mininet.cli import CLI #Class for providing an interactive command-line interface.
from mininet.log import setLogLevel #Function to set the log level for Mininet's output.

class CustomTopoLab0(Topo):
    """Custom topology as shown in Figure 1 of the PDF."""
    
    def build(self):
        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        
        # Add switches (OVSBridge type)
        s1 = self.addSwitch('s1', cls=OVSBridge)
        s2 = self.addSwitch('s2', cls=OVSBridge)
        
        # Add links with specified properties
        # Links e1-e4: 15 Mbps, 10 ms
        self.addLink(h1, s1, bw=15, delay='10ms', cls=TCLink)  # e1
        self.addLink(h2, s1, bw=15, delay='10ms', cls=TCLink)  # e2
        self.addLink(h3, s2, bw=15, delay='10ms', cls=TCLink)  # e3
        self.addLink(h4, s2, bw=15, delay='10ms', cls=TCLink)  # e4
        
        # Link e5: 20 Mbps, 45 ms
        self.addLink(s1, s2, bw=20, delay='45ms', cls=TCLink)  # e5

def run_network():
    """Create and run the network with the custom topology."""
    # Set log level
    setLogLevel('info')
    
    # Create topology
    topo = CustomTopoLab0()
    
    # Create and start network
    net = Mininet(topo=topo, link=TCLink, switch=OVSBridge)
    net.start()
    
    # Run basic connectivity test
    print("Testing network connectivity...")
    net.pingAll()
    
    # Drop into CLI
    print("Network is ready. Type 'exit' to stop the network.")
    CLI(net)
    
    # Stop network
    net.stop()

if __name__ == '__main__':
    run_network()

# -*- coding: utf-8 -*- DeepS
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomTopo(Topo):
    def build(self):
        # Add hosts with IP addresses 10.0.0.1 to 10.0.0.4
        # 24 bits for network, last 8 bits for host 
        # 255.255.255.0 subnet mask 
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        
        # Add Open vSwitch switches
        s1 = self.addSwitch('s1', cls=OVSBridge)
        s2 = self.addSwitch('s2', cls=OVSBridge)
        
        # Add links between hosts and switches (e1-e4)
        self.addLink(h1, s1, bw=15, delay='10ms', cls=TCLink)
        self.addLink(h2, s1, bw=15, delay='10ms', cls=TCLink)
        self.addLink(h3, s2, bw=15, delay='10ms', cls=TCLink)
        self.addLink(h4, s2, bw=15, delay='10ms', cls=TCLink)
        
        # Add link between switches (e5)
        self.addLink(s1, s2, bw=20, delay='45ms', cls=TCLink)

if __name__ == '__main__':
    setLogLevel('info')  # Enable Mininet logging
    topo = CustomTopo()  # Instantiate the topology
    net = Mininet(topo=topo, link=TCLink)  # Use TCLink for all links
    net.start()          # Start the network
    CLI(net)             # Launch Mininet CLI for manual testing
    net.stop()           # Stop the network after exiting CLI
    
    #!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSSwitch
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections

class BridgeTopo(Topo):
    "Custom bridge topology as per Figure 1."

    def build(self):
        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        # Add switches (OVSBridge type)
        s1 = self.addSwitch('s1', cls=OVSSwitch)
        s2 = self.addSwitch('s2', cls=OVSSwitch)

        # Add links with specified bandwidth and delay
        # e1: h1-s1, e2: h2-s1, e3: h3-s2, e4: h4-s2 (15 Mbps, 10 ms)
        self.addLink(h1, s1, cls=TCLink, bw=15, delay='10ms')
        self.addLink(h2, s1, cls=TCLink, bw=15, delay='10ms')
        self.addLink(h3, s2, cls=TCLink, bw=15, delay='10ms')
        self.addLink(h4, s2, cls=TCLink, bw=15, delay='10ms')
        # e5: s1-s2 (20 Mbps, 45 ms)
        self.addLink(s1, s2, cls=TCLink, bw=20, delay='45ms')

def run():
    "Instantiate and test the custom topology."
    topo = BridgeTopo()
    net = Mininet(topo=topo, link=TCLink, switch=OVSSwitch)
    net.start()
    info("*** Dumping host connections\n")
    dumpNodeConnections(net.hosts)
    info("*** Testing network connectivity\n")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
