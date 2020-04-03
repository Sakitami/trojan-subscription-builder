#!/usr/bin/python3
import configparser
import pymysql

# Read Config file
conf = configparser.ConfigParser()
conf.read("config.cfg")
serverip = conf.get("Mysql", "dbserver")
dbname = conf.get("Mysql", "dbname") 
dbuser = conf.get("Mysql", "username") 
dbpass = conf.get("Mysql", "password")
testt = conf.get("Mysql", "test")

# Connect to Mysql server
while True:
    try:
        db = pymysql.connect(serverip,dbuser,dbpass,dbname)
        print('Connected to \033[1;35m'+ serverip +'\033[0m')
        break
    except:
        print('Connect to Mysql Server failed!Reconnecting...')