#!/usr/bin/python3
import configparser
import pymysql
import os
import random
import hashlib

# Read Config file
conf = configparser.ConfigParser()
conf.read("config.cfg")
serverip = conf.get("Mysql", "dbserver")
dbname = conf.get("Mysql", "dbname") 
dbuser = conf.get("Mysql", "username") 
dbpass = conf.get("Mysql", "password")

def adduser(username,password,limit):
    username = str(username)
    password = str(passowrd)
    limit = str(limit)
    pd_sha224 = hashlib.sha224()
    pd_sha224.update(password.encode("UTF-8"))
    pd = str(pd_sha224.hexdigest())
    command = "insert into users (username, password, quota) values(" + '"' + username + '", ' + '"' + pd + '", ' + limit + ');'
    cursor = db.sursor()
    sursor.execute(command)
    sursor.close()
    db.commit()

# Connect to Mysql server
connect_num = 0
while True:
    if connect_num >= 3:
        print("Seems like your mysql config have something wrong.\nPree Enter to go back.")
        a = input()
        exit() if a == "Y" else exit()
    try:
        db = pymysql.connect(serverip,dbuser,dbpass,dbname)
        print('Connected to \033[1;35m'+ serverip +'\033[0m')
        break
    except:
        connect_num += 1
        print('Connect to Mysql Server failed!Reconnecting...')

# Operation database
# Add single user
print("-"*8)
a = input("Do you want to add a new user?[Y/n]")
if a == "Y":
    while True:
        add_user_name = input("Username:")
        add_user_passwd = input("Password:")
        add_user_limit = input("limit(MB):")
        add_user_limit *= 1048576
        adduser(add_user_name, add_user_passwd, add_user_limit)
        a = input("Do you want to go back?\n(c:Continue)[Y/n/c]:")
        if a == "Y":
            db.close()
            exit()
        elif a == "c":
            break

# Add users from subscription.
os.chdir("subscription")
a = input("Do you want to add all users from subscritpion?[Y/n]:")
if a == "Y":
    add_user_limit = input("Default user limit(MB):")
    filename = os.lsitdir()
    for i in filename:
        add_user_name = radom.randint(0,10000)
        add_user_passwd = i
        add_user_limit *= 1048576
        adduser(add_user_name, add_user_passwd, add_user_limit)
    print("All done!")

a = input("Press Enter to go back.")
exit() if a == "Y" else exit()
