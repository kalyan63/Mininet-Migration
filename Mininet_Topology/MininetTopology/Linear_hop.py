from time import sleep
from mininet.log import lg
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
import subprocess

class LinearTestTopo( Topo ):
    def build( self, N):
        h1=self.addHost('h1')
        h2=self.addHost('h2')
        switches = [self.addSwitch('s%s'%s) for s in range( 1, N+1) ]

        for i in range(N-1):
            self.addLink(switches[i],switches[i+1],cls=TCLink,bw=1000)

        self.addLink(h1,switches[0],cls=TCLink,bw=1000)
        self.addLink(h2,switches[N-1],cls=TCLink,bw=1000)

def main(hop):
    lg.setLogLevel( 'info')
    topo = LinearTestTopo(hop)    
    net = Mininet(topo=topo)   
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
 
    subprocess.run(["touch", "h2.txt"])
    p1 = h1.popen('python3 ../TCP_SC/tcp_server.py {} & '.format(h1.IP()))
    print("Starting transfer for hop: ",hop)
    h2.cmd('python3 ../TCP_SC/tcp_client.py {} {} |& tee -a h2.txt &'.format('Qe_h2',h1.IP()))

    sleep(5)
    print("h2 Client side Text:---")
    with open('h2.txt', 'r') as fin:
        print(fin.read())
    h1.cmd('sudo rm h2.txt')    
    p1.terminate()
    net.stop()

if __name__ == '__main__':
    #Varying hops
    hops = [2,4,6,8,10]
    for hop in hops:
        main(hop)
