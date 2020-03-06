#!/usr/bin/python3
import base64
import os


## Load source file
if os.path.isfile("password.txt") and os.path.isfile("url.txt"):
    print("Found source file,trying to load it...")
    ## Read dictionary file password.txt and url.txt
    with open('password.txt','r') as password:
    	passline = password.read().splitlines()
    with open('url.txt','r', encoding='UTF-8') as url:
    	urlline = url.read().splitlines()
    print("Loaded sorce file,creating original file...")
    ## Create a new directory and original files
    if os.path.isdir("subscription"):    
        os.chdir("subscription")
    else:
        os.mkdir("subscription")
        os.chdir("subscription")
    n = 0
    for i in range(0,len(passline)):
        sub_name = passline[n]
        subfile = open(sub_name, "w+")
        subfile.close
        n += 1
    print("Created,building subscription file...")
else:
    print("No password.txt or url.txt found,please check the directory")
    exit()


## Build subscription file
r = -1
for i in range(0,len(passline)):
    urlist = []
    r += 1
    num = 0
    print("Creating " + passline[r] + "'s subscription file...")
    for j in range(len(urlline)):
        trourl = "trojan://" + passline[r] + "@" + urlline[num]
        urlist.append(trourl)
        num += 1
    trojanlist = "\n".join(urlist)
    encryption = str(base64.b64encode(trojanlist.encode()), encoding = "utf-8")
    subfile = open(passline[r],"a")
    subfile.write(encryption)
    subfile.close()
