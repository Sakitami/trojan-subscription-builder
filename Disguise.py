#!/usr/bin/python3
import base64
import os


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
        os.chdir("subscription")
    else:
        os.mkdir("subscription")
        os.chdir("subscription")
    n = 0
    ## Determine whether to use html suffix
    print("Do you want to use \".html\" ?", end='')
    htmlkey = input("[Y/n]:")
    if htmlkey == "Y":
        sub_name = username[n]+ '.html'
    else:
        sub_name = username[n]
    ## Create files
    for i in range(0,len(username)):
        subfile = open(sub_name, "w+")
        subfile.close
        n += 1
    print("Created,building subscription file...")
else:
    print("No password.txt or url.txt found,please check the directory.")
    while True:
        print('Press Enter to exit...')
        exitkey = input()
        exit() if exitkey == "Y" else exit()


## Build subscription file
r = -1
print('-'*8)
for i in range(0,len(username)):
    urlist = []
    r += 1
    num = 0
    print("Creating " + username[r] + "'s subscription file...", end='')
    for j in range(len(urlline)):
        trourl = "trojan://" + passline[r] + "@" + urlline[num]
        urlist.append(trourl)
        num += 1
    num = 0
    for k in range(len(urlline)):
        trourl = "trojan://" + username[r] + "@" + urlline[num]
        urlist.append(trourl)
        num += 1
    ## Use base64 encode and write into files
    trojanlist = "\r\n".join(urlist)
    encryption = str(base64.b64encode(trojanlist.encode()), encoding = "utf-8")
    ## Check the if html suffix used
    if htmlkey == "Y":
        subfile = open(username[r] + '.html',"a")
    else:
        subfile = open(username[r] , "a")
    subfile.write(encryption)
    subfile.close()
    print('Done')
print('-'*8 + "\n" + 'All done, please check the subscription directory.')

a = input(u"Do you want to upload those to server?[Y/n]:")
if a == "Y":
    os.chdir(dirname)
    os.system("python ftp.py")

while True:
    print('Press Enter to exit...')
    exitkey = input()
    exit() if exitkey == "Y" else exit()
