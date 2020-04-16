#!/usr/bin/python3
import os

dirname = os.getcwd()
print('-'*8 + '\nWelcome to Trojan Subscription Builder\n\033[1;35mversion 0.0.3\033[0m\n' + '-'*8)
print('By')
print(''' ____        _    _ _                  _ 
/ ___|  __ _| | _(_) |_ __ _ _ __ ___ (_)
\___ \ / _` | |/ / | __/ _` | '_ ` _ \| |
 ___) | (_| |   <| | || (_| | | | | | | |
|____/ \__,_|_|\_\_|\__\__,_|_| |_| |_|_|'''+'\n'+'-'*8)
print('Which mode do you want to use?\n1.common\n2.Trojan-Panel(with mysql database)\n3.Add a user to mysql database\n4.exit')
while True:
    a = input(u'Choose one:')
    if a == "1":
        os.chdir(dirname)
        os.system("python common.py")
    elif a == "2":
        os.chdir(dirname)
        os.system("python database.py")
    elif a == "3":
        os.chdir(dirname)
        os.system("python dbconnect.py")
    elif a == "4":
        sys.exit()
    else:
        print("Invalid input, please try again")
