#!/usr/bin/python3
import os
import time
import configparser

conf = configparser.ConfigParser()
conf.read('config.cfg')
mode = conf.get("Settings", "mode")
sleep_time = conf.getint("Settings", "cycle")
print('\nWelcome to Trojan Subscription Builder\n\033[1;35mversion 0.1\033[0m\n','-'*8)
while True:
    if mode == 'common':
        print("Common mode is being used.")
        os.system('python common.py')
    elif mode == 'database':
        print("Database mode is being used.")
        os.system('python database.py')
    else:
        print("Wrong config.Please check settings.")
        break
    time.sleep(sleep_time)
sys.exit()
