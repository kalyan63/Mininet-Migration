## Results for question 1:

File used for download is: 

    > File name     : WarAndPeace.txt 
    > size          : 3.2 MB

1. **Single Topology:**
    > 
        |                               |   Host h2     |   Host h3     |   Host h4     |
        |_______________________________|_______________|_______________|_______________|
        |   Download Time (in seconds)  |   0.0725      |   0.09037     |   0.0749      |
        |   Throughput (in MB/s)        |   44.17       |   35.44       |   42.72       |

    > **Out put from the Terminal after running all host concurently**

    > !['Single Image'](q1_a.png)

    > Here we can see similar Download Time, but Host h3 has lower bandwidth than the other two. The main reason for this is concurrent download by all the host. Here I would first invoke the client of h2 and then h3 and h4. Since it takes time for my python code to run one client after the other so h3 will always be in a race condition with h2 and h4 since its being invoked in the middle. 

    > Since its concurrent download the server bandwidth is equal to sum of the above bandwidths.

2. **Linear Topology (Bandwidth):**
    > 
        |      Bandwidth (in Mb)        |   10          |   100         |   1000 (1 Gb)     |      
        |_______________________________|_______________|_______________|___________________|
        |   Download Time (in seconds)  |   2.99        |   0.47        |   0.0589          |     
        |   Throughput (in MB/s)        |   1.069       |   6.809       |   54.289          |

    > **Sample output from the terminal :**

    > !['Bandwidth'](q1_b.png)

    > Here we can see that as bandwidth increases the Throughput also increases. From above table we can say that throughput is linaerly related to bandwidth. 

    > Here 1Gb provides the best Throughput just as expected.

3. **Linear Topology (Delay):**
    >
        |        Delay (in ms)          |   1 ms        |   2 ms        |   5 ms        |   10 ms       |
        |_______________________________|_______________|_______________|_______________|_______________|
        |   Download Time (in seconds)  |   0.0992      |   0.21        |   0.467       |   1.112       |    
        |   Throughput (in MB/s)        |   32.268      |   15.185      |   6.846       |   2.879       |

    > **Sample output from the terminal :**

    > !['Delay'](q1_c.png)

    > We know that as delay increases the download time increases, Since packet takes longer time to travel through the network. 

    > Here Throughput is inversly proportional to delay, so lesser the delay better is the throughput. 

4. **Linear Topology (Loss):**
    >
        |       Loss (in %)             |   1% loss     |   2% loss     |   5% loss     |
        |_______________________________|_______________|_______________|_______________|
        |   Download Time (in seconds)  |   0.0564      |   0.345       |   6.257       |
        |   Throughput (in MB/s)        |   56.715      |   9.263       |   0.5119      |

    > **Sample output from the terminal :**

    > !['Delay'](q1_d.png)

    > Here we can see almost an exponential drop in throughput as loss increases in the network. This is because tcp is a relaiable data transfer layer and would wait till all the packets reach the destination. Hence as loss increases Download time increases. 

    > We also know in some implementation the whole window is dropped if there is packet loss. So any loss would severly impact the performance of tcp. 

5. **Linear Topology (hop):**
    >
        |   Hops (no of switchs)        |   2       |   4       |   6       |   8       |   10      |   
        |_______________________________|___________|___________|___________|___________|___________|
        |   Download Time (in seconds)  |   0.089   |   0.139   | Connection| Connection| Connection|
        |   Throughput  (in MB/s)       |   35.6    |   22.99   |   Error   |   Error   |   Error   |

    > **Sample output from the terminal :**

    > !['Delay'](q1_e_1.png)

    > !['Delay'](q1_e_2.png)

    > Here we can see that for more than 6 switchs the tcp connection is not established.

    > So if the network has huge RTT the tcp connection is not established, since there would always be a timeout before the packet returns. Hence it very important to set a proper timeout in tcp connection.  