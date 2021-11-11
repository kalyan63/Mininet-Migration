import socket
import time
import sys
import os

File_Name=sys.argv[1]
IPserver=sys.argv[2]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=12345
buffer_size=1024

#Connect to the server
s.connect((IPserver,port))
msg=s.recv(1024).decode()
print('Connected to Server at: IP={} Port={}'.format(IPserver,port))

#Saving file as specified by the client
fname="../RecFiles/"+File_Name+".txt"

start_time=time.time_ns()
with open(fname,'wb') as f:
    while True:
        line=s.recv(buffer_size)
        if(line):
            f.write(line)
        else:
            break      
end_time=time.time_ns()        
tot=(end_time-start_time)/10**9
sz=os.path.getsize(fname)

print("Time taken to download is: {}s".format((end_time-start_time)/10**9))  
print("Throughput = {}MB/s".format(sz/(tot*1024*1024)))      
s.close()