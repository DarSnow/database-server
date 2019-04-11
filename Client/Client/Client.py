# -*- coding:utf-8 -*
import socket
import json



msg1 = [{'OP':"login", 'username':"admin"}] #登录
msg2 = [{'OP':"register",'username':"Lee",'nickname':"mee",'password':"123123",'sex':"M"}] #注册
msg3 = [{'OP':"feed",'pet_id':1,'bag_id':1,'food_type':"cat_water",'number':5}] #喂养
msg4 = [{'OP':"add_food",'bag_id':1,'number':10}] #添加食物
msg5 = [{'OP':"store_food",'username':"admin",'food_type':"fish",'number':10}] #存放食物
msg6 = [{'OP':"get_pet",'username':"admin"}] #查询宠物
msg7 = [{'OP':"get_bag",'username':"admin"}] #查询背包

jmsg1 = json.dumps(msg1)
jmsg2 = json.dumps(msg2)
jmsg3 = json.dumps(msg3)
jmsg4 = json.dumps(msg4)
jmsg5 = json.dumps(msg5)
jmsg6 = json.dumps(msg6)
jmsg7 = json.dumps(msg7)

#注册
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('219.224.167.250', 9999))
print(s.recv(1024).decode('utf-8'))
s.sendall(jmsg2.encode('utf-8'))
s.send(b'exit')
s.recv(1024)
s.close()
#登录
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('219.224.167.250', 9999))
print(s.recv(1024).decode('utf-8'))
s.sendall(jmsg1.encode('utf-8'))
rev = s.recv(1024)
print(rev)
s.send(b'exit')
s.recv(1024)
s.close()
#喂养
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('219.224.167.250', 9999))
print(s.recv(1024).decode('utf-8'))
s.sendall(jmsg3.encode('utf-8'))
s.send(b'exit')
s.recv(1024)
s.close()
#查询宠物
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('219.224.167.250', 9999))
print(s.recv(1024).decode('utf-8'))
s.sendall(jmsg6.encode('utf-8'))
print(s.recv(1024))
s.send(b'exit')
s.recv(1024)
s.close()
#查询背包
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('219.224.167.250', 9999))
print(s.recv(1024).decode('utf-8'))
s.sendall(jmsg7.encode('utf-8'))
while True:
    data = s.recv(1024)
    print(data)
    jdata = json.loads(data)
    print(jdata)
    if(jdata[0]['have_msg']==0):
        break

s.send(b'exit')
print(s.recv(1024))
s.close()

