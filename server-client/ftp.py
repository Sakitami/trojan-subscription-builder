#!/usr/bin/python3
import configparser
from ftplib import FTP
import time
import tarfile
import os

# Load FTp Mode
conf = configparser.ConfigParser()
conf.read("config.cfg")
serverip = conf.get("FTP", "server") 
port = conf.getint("FTP", "port") 
username = conf.get("FTP", "user") 
password = conf.get("FTP", "password")
dirname = conf.get("FTP", "dir")
list_file = os.listdir("subscription")
print("Load config success! \nConnecting to the server...")

# Connect to Server
try:
    ftp = FTP()
    ftp.connect(serverip,port)
    ftp.login(username,password)
    bufsize = 1024
    print("Connected to the server!")
    try:
        ftp.cwd(dirname)
        print("Changed to the working directory:"+ dirname)
    except:
        print("Cheange the work directory failed.Use default settings.\n"+ '-'*8)
except:
    print("Connect failed!")
    a = input("Press Enter to go back.")
    exit()

# Delete Files
failed1 = success1 = 0
del_files = ftp.nlst()
print("Start deleteing files...")
print(del_files)
for i in del_files:
    try:
        ftp.delete(i)
        success1 += 1
    except:
        failed1 += 1
failed1 = str(failed1)
success1 = str(success1)
print("All Done,deleted ", success1, " files, ", failed1, " files not be deleted.\n", '-'*8)

# Upload Files
print("Start uploading files...")
os.chdir("subscription")
failed2 = success2 = 0
for i in list_file:
    try:
        fp = open(i,'rb')
        ftp.storbinary('STOR ' + i, fp,bufsize)
        success2 += 1
    except:
        failed2 += 1
failed2 = str(failed2)
success2 = str(success2)
print("All Done,upload ", success2, " files, ", failed2, " files not be uploaded.")

fp.close()
ftp.quit()
exit()
