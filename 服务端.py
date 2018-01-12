#服务端
import socket
import time

server=socket.socket()

server.bind(('127.0.0.1',8888))#绑定端口
server.listen(5)#监听

conn,address=server.accept()#内容，地址  等待数据接收
#print(address,conn)

#data=conn.recv(1024)
#print(data)
#print(str(len_long,encoding='utf-8'))

data=b''
while True:
    finish_time=time.ctime()
    response=conn.recv(1024)
    data+=response
    if len(response) <1024:
        break
print(len(data))

with open('hi.gif','wb') as f:
    f.write(data)

conn.send(bytes('done',encoding='utf-8'))

'''
or not int(finish_time.split(':')[2].split(' ')[0])-int(start_time.split(':')[2].split(' ')[0])>=10
'''
