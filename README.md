## Mininet Migration:

1. **Installation**:

    > **Installation in Ubuntu:** 

        > Step 1: sudo apt-get install mininet

        > Step 2: sudo mn -c

        > Step 3: sudo apt-get install git

        > Step 4: git clone git://github.com/mininet/mininet

        > Step 5: cd mininet

        > Step 6: git tag # list available versions

        > Step 7: git checkout -b [version]

        > Step 8: cd ..

        > Step 9: mininet/util/install.sh -a

        > Step 10: sudo mn

2. **Files**:

    >**Files required for question 1:** 

        > Mininet_Topology
            > MininetTopology
                > Single_Topo.py
                > Linear_Bandwidth.py
                > Linear_Delay.py
                > Linear_Loss.py
                > Linear_hop.py
            > RecFiles
            > SendFiles
                > WarAndPeace.py
            > TCP_SC
                > tcp_client.py
                > tcp_server.py

    > **Files required for question 2:**

        > Custom_Topology
            > Custom_Topology_SingleServer
                > Tree_Topo.py
            > Custom_Topology_ThreeServers
                > Tree_Topo_Scale.py

3. **Details about the files**

    > MininetTopology folder contains all the Topology required for question 1, which includes Single switch and Linear connections. 

    > TCP_SC folder contains tcp host and server program to download the files. Tcp server and clients takes IP as input system arguments which is necessary to connect to differnt servers while creating network using mininet.

    > Tcp server is made concurrent to handle request from multiple clients simultaniously. 

    > Custom_Topology folder conatins files to make custom Tree topology for 2nd question and use iperf to find out the network bandwidth of client and server.

4. **How to run**

    > cd to the required directory where code for mininet networks is present(ex: Linear_hop.py) and run those code.

    > Run using the cmd: 

        > sudo -E python3 Linear_hop.py