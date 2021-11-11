from time import sleep
from mininet.log import lg
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
import subprocess

class LinearTestTopo( Topo ):
    def build( self,loss):

        h1=self.addHost('h1')
        h2=self.addHost('h2')
        s1=self.addSwitch('s1')

        self.addLink(h1,s1,cls=TCLink,bw=1000,loss=loss)
        self.addLink(h2,s1,cls=TCLink,bw=1000,loss=loss)

def main(loss):
    lg.setLogLevel( 'info')
    topo = LinearTestTopo(loss)
    net = Mininet(topo=topo)
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    print("Starting transfer for loss: ",loss)
    subprocess.run(["touch", "h2.txt"])
    p1 = h1.popen('python3 ../TCP_SC/tcp_server.py {} & '.format(h1.IP()))
    print("Starting transfer for loss: ",loss)
    h2.cmd('python3 ../TCP_SC/tcp_client.py {} {} |& tee -a h2.txt &'.format('Qd_h2',h1.IP()))

    sleep(10)
    print("h2 Client side Text:---")
    with open('h2.txt', 'r') as fin:
        print(fin.read())
    h1.cmd('sudo rm h2.txt')    
    p1.terminate()
    net.stop()

if __name__ == '__main__':
    # 1 %, 2 % and 5% loss respectively for each iteration 
    losses = [1,2,5]
    for loss in losses:
        main(loss)
    