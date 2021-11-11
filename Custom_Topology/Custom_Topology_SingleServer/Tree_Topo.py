from time import sleep
from mininet.log import lg
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
import subprocess

class TreeCustomTopo( Topo ):
    def build( self ):
        hostName = ['S','H','I','J','K','L','M','N','O']
        hosts = []
        for h in hostName:
            hosts.append(self.addHost(h))
        switchName = ['s1','s2','s3','s4','s5','s6','s7']
        switches = []
        for s in switchName:
            switches.append(self.addSwitch(s))

        #Adding Links
        self.addLink(switches[0],switches[1], cls=TCLink , bw = 400)
        self.addLink(switches[0],switches[2], cls=TCLink , bw = 400)
        self.addLink(switches[1],switches[3], cls=TCLink , bw = 200)
        self.addLink(switches[1],switches[4], cls=TCLink , bw = 200)
        self.addLink(switches[2],switches[5], cls=TCLink , bw = 200)
        self.addLink(switches[2],switches[6], cls=TCLink , bw = 200)

        self.addLink(hosts[0],switches[0],cls=TCLink, bw = 400 )

        self.addLink(hosts[1],switches[3],cls=TCLink, bw = 100 )
        self.addLink(hosts[2],switches[3],cls=TCLink, bw = 100 )
        self.addLink(hosts[3],switches[4],cls=TCLink, bw = 100 )
        self.addLink(hosts[4],switches[4],cls=TCLink, bw = 100 )
        self.addLink(hosts[5],switches[5],cls=TCLink, bw = 100 )
        self.addLink(hosts[6],switches[5],cls=TCLink, bw = 100 )
        self.addLink(hosts[7],switches[6],cls=TCLink, bw = 100 )
        self.addLink(hosts[8],switches[6],cls=TCLink, bw = 100 )

def main():
    lg.setLogLevel('info')
    topo = TreeCustomTopo()
    net = Mininet(topo=topo)
    net.start()

    S = net.get('S')
    H = net.get('H')
    K = net.get('K')
    N = net.get('N')
    O = net.get('O')
    S.cmd('sudo rm S.txt H.txt K.txt N.txt O.txt')
    subprocess.run(["touch", "S.txt","H.txt","K.txt","N.txt","O.txt"])
    S.cmd('iperf -s |& tee -a S.txt &')
    sleep(10)
    print(H.cmd('iperf -c {} |& tee -a H.txt &'.format(S.IP())))
    print(K.cmd('iperf -c {} |& tee -a K.txt &'.format(S.IP())))
    print(N.cmd('iperf -c {} |& tee -a N.txt &'.format(S.IP())))
    print(O.cmd('iperf -c {} |& tee -a O.txt &'.format(S.IP())))

    sleep(20)
    net.stop()

if __name__ == '__main__':
    main()
