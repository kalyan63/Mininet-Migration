import socket
import sys
from threading import Thread
from time import sleep

class ServerThread(Thread):
    def __init__(self,conn):
        Thread.__init__(self)
        self.conn=conn

    def run(self):
        self.conn.send("The Connection is Set".encode())
        file_name="../SendFiles/WarAndPeace.txt"
        with open(file_name,'rb') as file:
            data=file.read(buffer_size)
            while(data):
                self.conn.send(data)
                data=file.read(buffer_size)       
        self.conn.close()      
        print('Done Sending File')  

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=12345
buffer_size=1024
IP_server=sys.argv[1]

s.bind((IP_server,port))
Threads=[]

print('Server listning at port: {}'.format(port))

while True:
    s.listen(5)
    c,addr=s.accept()
    print('Connected with : {}'.format(addr))
    newThread=ServerThread(c)
    newThread.start()
    Threads.append(newThread)
    
for t in Threads:
    t.join()
print("Done serving")
