from time import sleep
from mininet.log import lg
from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
import subprocess
def main():
    lg.setLogLevel('info')

    topo = SingleSwitchTopo(4)
    net = Mininet(topo=topo)
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    subprocess.run(["touch", "h2.txt","h3.txt","h4.txt","h1.txt"])
    p1 = h1.popen('python3 ../TCP_SC/tcp_server.py {} |& tee -a h1.txt &'.format(h1.IP()))

    print(h2.cmd('python3 ../TCP_SC/tcp_client.py {} {} |& tee -a h2.txt &'.format('Qa_h2',h1.IP())))
    print(h3.cmd('python3 ../TCP_SC/tcp_client.py {} {} |& tee -a h3.txt &'.format('Qa_h3',h1.IP())))
    print(h4.cmd('python3 ../TCP_SC/tcp_client.py {} {} |& tee -a h4.txt &'.format('Qa_h4',h1.IP())))

    sleep(5)
    p1.terminate()

    print("Server side Text:---")
    with open('h1.txt', 'r') as fin:
        print(fin.read())
    print("h2 Client side Text:---")
    with open('h2.txt', 'r') as fin:
        print(fin.read())
    print("h3 Client side Text:---")
    with open('h3.txt', 'r') as fin:
        print(fin.read())
    print("h4 Client side Text:---")
    with open('h4.txt', 'r') as fin:
        print(fin.read())

    h4.cmd('sudo rm h1.txt h2.txt h3.txt h4.txt')
    net.stop()

if __name__ == '__main__':
    main()
