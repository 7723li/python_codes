#客户端
import socket
import time
        
client=socket.socket()
client.connect(('127.0.0.1',8888))#(id,port)

#client.send(bytes('hello',encoding='utf-8'))

with open(r'C:\Users\Administrator\Desktop\station_name.txt','rb') as f:
    #client.send(bytes(str(f.read()),encoding='utf-8'))
    d=f.read()
    a=len(d)
    b,c=int(a/1024),a%1024
    for i in range(1,b+1):
        client.send(d[(i-1)*1024:(i*1024)])
    client.send(d[b*1024:b*1024+c])
    
data=client.recv(1024)
print(str(data,encoding='utf-8'))

client.close()
