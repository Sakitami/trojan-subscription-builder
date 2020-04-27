#!/usr/bin/python3
import base64
import os
import shutil

## 模板套用函数
def alter(file,old_str,new_str):
    with open(file,'r+',encoding='utf-8') as ca:
        wc = ca.readlines()
        with open('new','w+',encoding='utf-8') as cb:
            for i in  wc:
                if old_str in i:
                    i = i.replace(old_str,new_str)
                    cb.write(i)
                else:
                    cb.write(i)
    os.remove(file);os.rename('new',file)

## Load source file
if os.path.isfile("password.txt"): # and os.path.isfile("url.txt"):
    print("Found source file,trying to load it...")
    ## Read dictionary file password.txt and url.txt
    with open('password.txt','r') as password:
    	passline = password.read().splitlines()
    print("Loaded sorce file,creating original file...")
    origin_addr = os.getcwd()
    temp_addr = os.getcwd() + '/templates/temp.yaml'
    ## Create a new directory and original files
    if os.path.isdir("subscription"):
        if os.path.isdir("subscription/clash") == False:
            os.mkdir("subscription/clash")
        shutil.copy(temp_addr, 'subscription/clash/origin.yaml')
        os.chdir("subscription/clash")
    else:
        os.mkdir("subscription")
        os.mkdir('subscription/clash')
        shutil.copy(temp_addr, 'subscription/clash/origin.yaml')
        os.chdir("subscription/clash")
    ## Determine whether to use html suffix
    continue_key = input("Press Y to Continue:")
    if continue_key == "Y":
        print("Creating original files...")
    else:
        exit()
    ## Create files
    n = 0
    for i in range(0,len(passline)):
        passline_clash = passline[n] + '-clash.yml'
        shutil.copy('origin.yaml', passline_clash)
        n += 1
    print("Created,building subscription file...")
else:
    print("No password.txt or url.txt found,please check the directory.")
    while True:
        exitkey = input('Press Enter to exit...')
        exit() if exitkey == "Y" else exit()


## Build subscription file
r = -1
print('-'*8)
for i in range(0,len(passline)):
    r += 1
    print("Creating " + passline[r] + "'s subscription file...", end='')
    passline_clash = passline[r] + '-clash.yml'
    alter(passline_clash,"{{passwd}}",passline[r])
    print('Done')
print('-'*8 + "\n" + 'All done, please check the subscription directory.')

a = input(u"Do you want to upload those to server?[Y/n]:")
if a == "Y":
    os.chdir(origin_addr)
    os.system("python ftp.py")

while True:
    print('Press Enter to exit...')
    exitkey = input()
    exit() if exitkey == "Y" else exit()
