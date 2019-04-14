#!/usr/bin/python
# -*- coding:utf-8 -*
import time
import threading
import socket
from DataBase import * 
from TcpManager import tcplink

def main():
    dbCreatTable()
    userInsert('admin','admin','123','m')
    petInsert('cat-Persian',0,0,'admin')
    bagInsert('admin','cat_water',50)
    bagInsert('admin','cat_cookie',15)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('219.224.167.250', 9999))
    s.listen(5)
    print('Waiting for connection...')
    
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
if __name__ == '__main__':
    main()

