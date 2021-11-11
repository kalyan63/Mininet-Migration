from time import sleep
from mininet.log import lg
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
import subprocess

class LinearTestTopo( Topo ):
    def build(self, delay):
        h1=self.addHost('h1')
        h2=self.addHost('h2')
        s1=self.addSwitch('s1')

        self.addLink(h1,s1,cls=TCLink,bw=1000,delay=str(delay)+'ms')
        self.addLink(h2,s1,cls=TCLink,bw=1000,delay=str(delay)+'ms')

def main(delay):
    lg.setLogLevel( 'info')
    topo = LinearTestTopo(delay)
    net = Mininet(topo=topo)
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    
    subprocess.run(["touch", "h2.txt"])
    p1 = h1.popen('python3 ../TCP_SC/tcp_server.py {} & '.format(h1.IP()))
    print("Starting transfer for delay: ",delay)  
    h2.cmd('python3 ../TCP_SC/tcp_client.py {} {} |& tee -a h2.txt &'.format('Qc_h2',h1.IP()))

    sleep(10)
    print("h2 Client side Text:---")
    with open('h2.txt', 'r') as fin:
        print(fin.read())
    h1.cmd('sudo rm h2.txt')    
    p1.terminate()
    net.stop()

if __name__ == '__main__':
    # Varying Delay
    delays = [1,2,5,10]
    for delay in delays:
        main(delay)