#!/usr/bin/python3
import os
import base64
import configparser

## Load seetings
conf = configparser.ConfigParser()
conf.read('config.cfg')
html = conf.get("Settings", "html")
autoupload = conf.get("Settings", "autoupload")

## Load source file
dirname = os.getcwd()
if os.path.isfile("password.txt") and os.path.isfile("url.txt"):
    print("Found source file,trying to load it...")
    ## Read dictionary file password.txt and url.txt
    with open('password.txt','r') as password:
    	passline = password.read().splitlines()
    with open('url.txt','r', encoding='UTF-8') as url:
    	urlline = url.read().splitlines()
    with open('username.txt','r', encoding='UTF-8') as username:
    	username = username.read().splitlines()
    print("Loaded sorce file,creating original file...")
    ## Create a new directory and original files
    if os.path.isdir("subscription"):    
        os.system("rm -rf subscription")
        os.chdir("subscription")
    else:
        os.mkdir("subscription")
        os.chdir("subscription")
    n = 0
    ## Determine whether to use html suffix
    if html == 1:
        sub_name = passline[n]+ '.html'
    else:
        sub_name = passline[n]
    ## Create files
    for i in range(0,len(passline)):
        subfile = open(sub_name, "w+")
        subfile.close
        n += 1
    print("Created,building subscription file...")
else:
    print("No password.txt or url.txt found,please check the directory.")
    exit()

## Build subscription file
r = -1
print('-'*8)
for i in range(0,len(passline)):
    urlist = []
    r += 1
    num = 0
    print("Creating " + passline[r] + "'s subscription file...", end='')
    for j in range(len(urlline)):
        trourl = "trojan://" + username[r] + ":" + passline[r] + "@" + urlline[num]
        urlist.append(trourl)
        num += 1
    ## Use base64 encode and write into files
    trojanlist = "\r\n".join(urlist)
    encryption = str(base64.b64encode(trojanlist.encode()), encoding = "utf-8")
    ## Check the if html suffix used
    if html == 1:
        subfile = open(passline[r] + '.html',"a")
    else:
        subfile = open(passline[r] , "a")
    subfile.write(encryption)
    subfile.close()
    print('Done')
print('-'*8 + "\n" + 'All done, please check the subscription directory.')

a = input(u"Do you want to upload those to server?[Y/n]:")
if autoupload == 1:
    os.chdir(dirname)
    os.system("python ftp.py")
exit()
