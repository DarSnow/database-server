# -*- coding:utf-8 -*
import pymysql

#创建所有表
def dbCreatTable():
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    cursor.execute("drop table if exists pet")
    cursor.execute("drop table if exists bag")
    cursor.execute("drop table if exists user")
    #user
    sql_user = """create table IF NOT EXISTS user(
          username VARCHAR(25) not null default '',
          nickname VARCHAR(15),
          password VARCHAR(40),
          sex VARCHAR(1),
          PRIMARY KEY (`username`))"""
    cursor.execute(sql_user)
    #pet
    sql_pet = """create table IF NOT EXISTS pet(
          pet_id INT NOT NULL AUTO_INCREMENT,
          pet_type VARCHAR(15),
          healthy INT,
          happiness INT,
          master VARCHAR(25),
          FOREIGN KEY (`master`) REFERENCES `user` (`username`),
          PRIMARY KEY (`pet_id`))"""
    cursor.execute(sql_pet)
    #bag
    sql_bag = """create table IF NOT EXISTS bag(
          bag_id INT NOT NULL AUTO_INCREMENT,
          username VARCHAR(25),
          food_type VARCHAR(15),
          number INT,
          FOREIGN KEY (`username`) REFERENCES `user` (`username`),
          PRIMARY KEY (`bag_id`))"""
    cursor.execute(sql_bag)
    cnn.close()
#插入用户
def userInsert(usernam,nicknam,pssword,sex):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "INSERT INTO user(username,nickname,password,sex) values('%s','%s','%s','%s')" % (usernam,nicknam,pssword,sex)
    try:
     cursor.execute(sql)
     cnn.commit()
    except:
      print("user insert fail!")
      cnn.rollback()
    cnn.close()
#插入宠物
def petInsert(pet_type,healthy,happiness,master):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "INSERT INTO pet(pet_type,healthy,happiness,master) values('%s','%d','%d','%s')" % (pet_type,healthy,happiness,master)
    try:
     cursor.execute(sql)
     cnn.commit()
    except:
     print("pet insert fail!")
     cnn.rollback()
    cnn.close()
#插入背包
def bagInsert(username,food_type,number):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "INSERT INTO bag(username,food_type,number) values('%s','%s','%d')" % (username,food_type,number)
    try:
     cursor.execute(sql)
     cnn.commit()
    except:
     print("bag insert fail!")
     cnn.rollback()
    cnn.close()
#查询用户
def userQuery(username):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "SELECT * FROM user WHERE username = '%s'" % (username)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            nickname = row[1]
            password = row[2]
            sex = row[3]
            #打印
            #print('nickname = %s, password = %s, sex = %s' % (nickname,password,sex))
            return (username,nickname,password,sex) #只有一个
    except:
        print("Error: unable to fetch data")
    cnn.close()   
#查询宠物
def petQuery(username):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "SELECT * FROM pet WHERE master = '%s'" % (username)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for row in result:
            pet_id = row[0]
            pet_type = row[1]
            healthy = row[2]
            happiness = row[3]
            master = row[4]
            list1 = [pet_id,pet_type,healthy,happiness,master]
            res.append(list1)
            #打印
            #print('pet_id = %d, pet_type = %s, health = %d, happiness = %d, master = %s' % (pet_id,pet_type,healthy,happiness,master))
        return res
    except:
        print("Error: unable to petQuery")
    cnn.close()   
#查询背包
def bagQuery(username):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "SELECT * FROM bag WHERE username = '%s'" % (username)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for row in result:
            bag_id = row[0]
            usname = row[1]
            food_type = row[2]
            number = row[3]

            list1 = [bag_id,usname,food_type,number]
            res.append(list1)
        return res
    except:
        print("Error: unable to bagQuery")
    cnn.close()   
#更新用户
def userUpdate(info,username):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "UPDATE user SET nickname = '%s',password ='%s',sex = '%s' WHERE username = '%s'" % (info[0],info[1],info[2],username)
    try:
        cursor.execute(sql)
        cnn.commit()
    except:
        print("Error: unable to update user")
        cnn.rollback()
    cnn.close()   
#更新宠物
def petUpdate(info,pet_id):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "UPDATE pet SET pet_type = '%s',healthy ='%d',happiness = '%d' WHERE pet_id = '%d'" % (info[0],info[1],info[2],pet_id)
    try:
        cursor.execute(sql)
        cnn.commit()
    except:
        print("Error: unable to update pet")
        cnn.rollback()
    cnn.close()  
#更新背包
def bagUpdate(info,bag_id):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "UPDATE bag SET food_type = '%s',number ='%d' WHERE bag_id = '%d'" % (info[0],info[1],bag_id)
    try:
        cursor.execute(sql)
        cnn.commit()
    except:
        print("Error: unable to update bag")
        cnn.rollback()
    cnn.close()  
#喂养宠物
def petFeed(nutrition,pet_id):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "UPDATE pet SET healthy =healthy+'%d',happiness = happiness+'%d' WHERE pet_id = '%d'" % (nutrition,nutrition/2,pet_id)
    try:
        cursor.execute(sql)
        cnn.commit()
    except:
        print("Error: unable to update pet")
        cnn.rollback()
    cnn.close()  
#使用背包
def bagUse(number,bag_id):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "UPDATE bag SET number =number-'%d' WHERE bag_id = '%d'" % (number,bag_id)
    try:
        cursor.execute(sql)
        cnn.commit()
    except:
        print("Error: unable to update bag")
        cnn.rollback()
    cnn.close()  
#通过宠物id查询宠物
def petQueryById(pet_id):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "SELECT * FROM pet WHERE pet_id = '%d'" % (pet_id)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for row in result:
            pet_id = row[0]
            pet_type = row[1]
            healthy = row[2]
            happiness = row[3]
            master = row[4]
            list1 = [pet_id,pet_type,healthy,happiness,master]
            res.append(list1)
            #打印
            #print('pet_id = %d, pet_type = %s, health = %d, happiness = %d, master = %s' % (pet_id,pet_type,healthy,happiness,master))
        return res
    except:
        print("Error: unable to fetch data")
    cnn.close()   
#通过背包id查询背包
def bagQueryById(bag_id):
    cnn = pymysql.connect("localhost","root","tongyi1520","catgame")
    cursor = cnn.cursor()
    sql = "SELECT * FROM pet WHERE bag_id = '%d'" % (bag_id)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        res = []
        for row in result:
            pet_id = row[0]
            pet_type = row[1]
            healthy = row[2]
            happiness = row[3]
            master = row[4]
            list1 = [pet_id,pet_type,healthy,happiness,master]
            res.append(list1)
            #打印
            #print('pet_id = %d, pet_type = %s, health = %d, happiness = %d, master = %s' % (pet_id,pet_type,healthy,happiness,master))
        return res
    except:
        print("Error: unable to fetch data")
    cnn.close()   

#Test db operator
#dbCreatTable()
#userInsert('admin','admin','123','m')
#petInsert('cat-Angora',100,100,'admin')
#petInsert('cat-Persian',120,90,'admin')
#bagInsert('admin','cat_food',16)
#userQuery('admin')
#res = petQuery('admin')
#print(res)
#userUpdate(['ad','345','f'],'admin')
#petUpdate(['dot-happ',49,50],1)
#bagUpdate(['coca',200],1)