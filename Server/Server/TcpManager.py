import time
import threading
import socket
import json, types,string
from DataBase import * 
import datetime

nutrition_table = {'cat_water':2,'cat_cookie':10,'fish':3}

def tcplink(sock, addr):
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (nowTime)
    print(' Accept new connection from %s:%s...' % addr)
    #sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(0.1)
        if not data or data.decode('utf-8') == 'exit':
            break
        jdata = json.loads(data)
        if(jdata[0]['OP']=='login'):
            print("login")
            username = jdata[0]['username']
            result = userQuery(username)
            if result == None:
                msg = [{'code':2,'password':"None"}]
            else:
                msg = [{'code':1,'password':"%s"%(result[2])}]
            jmsg = json.dumps(msg)
            sock.send(jmsg.encode('utf-8'))
        elif(jdata[0]['OP']=='register'):
            print("register")
            username = jdata[0]['username']
            nickname = jdata[0]['nickname']
            password = jdata[0]['password']
            sex = jdata[0]['sex']
            res = userQuery(username)
            if res == None:
                userInsert(username,nickname,password,sex)
                msg = [{'code':3,'msg':"success"}]
                jmsg = json.dumps(msg)
                sock.send(jmsg.encode('utf-8'))
            else:
                msg = [{'code':4,'msg':"fail"}]
                jmsg = json.dumps(msg)
                sock.send(jmsg.encode('utf-8'))
        elif(jdata[0]['OP']=='feed'):
            print("feed")
            pet_id = jdata[0]['pet_id']
            bag_id = jdata[0]['bag_id']
            food_type = jdata[0]['food_type']
            number = jdata[0]['number']
            bagUse(number,bag_id)
            nutri = nutrition_table[food_type]*number
            petFeed(nutri,pet_id)
            res = petQueryById(pet_id)
            msg = [{'code':12,'healthy':res[0][2],'happiness':res[0][3]}]
            jmsg = json.dumps(msg)
            sock.send(jmsg.encode('utf-8'))
        elif(jdata[0]['OP']=='add_food'):
            print("add_food")
            bag_id = jdata[0]['bag_id']
            number = jdata[0]['number']
            bagUse(number*-1,bag_id)
        elif(jdata[0]['OP']=='store_food'):
            print("store_food")
            username = jdata[0]['username']
            food_type = jdata[0]['food_type']
            number = jdata[0]['number']
            bagInsert(username,food_type,number)
        elif(jdata[0]['OP']=='get_pet'):
            print("get_pet")
            username = jdata[0]['username']
            pet = petQuery(username)
            if(pet==None):
                 msg = [{'code':50}]
                 jmsg = json.dumps(msg)
                 sock.send(jmsg.encode('utf-8'))
            else:
                msg = [{'code':51,'pet_id':pet[0][0],'pet_type':"%s"%(pet[0][1]),'healthy':pet[0][2],'happiness':pet[0][3],'master':"%s"%(pet[0][4])}]
                jmsg = json.dumps(msg)
            sock.send(jmsg.encode('utf-8'))
        elif(jdata[0]['OP']=='get_bag'):
            print("get_bag")
            username = jdata[0]['username']
            bag = bagQuery(username)
            if(bag==None):
                 msg = [{'code':52}]
                 jmsg = json.dumps(msg)
                 sock.send(jmsg.encode('utf-8'))
            else:
                msg = []
                for i in range(len(bag)):
                    tem_msg = {'code':53,'bag_id':bag[i][0],'username':"%s"%(bag[i][1]),'food_type':"%s"%(bag[i][2]),'number':bag[i][3]}
                    msg.append(tem_msg)
                jmsg = json.dumps(msg)
                sock.send(jmsg.encode('utf-8'))
        #print('Hello, %s!' % data.decode('utf-8')).encode('utf-8')
    sock.send(b'Close!')
    sock.close()
    print('Connection from %s:%s closed.' % addr)