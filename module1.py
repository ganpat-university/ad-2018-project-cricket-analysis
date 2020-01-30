import socket
import sys
UDP_IP = "192.168.43.159"
UDP_PORT_NO = 50000
#target = "www.google.com"
ServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#ServerSock.connect((target,8968))
ServerSock.bind((UDP_IP,UDP_PORT_NO))
i=0
splitData=[]

while(i<100):
    data, addr = ServerSock.recvfrom(1024) 
    newData = data.decode().split(",")
    newData[5]=newData[5][:-2]
    splitData.append(newData)
    print(data)
    i=i+1
