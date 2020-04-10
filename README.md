# trojan-subscription-builder
A Mini Python Program to Build Trojan Subscription file.

---

### Useage

**Attention: You need to run this program with python3.**

To use it,just run "run.py".

For mac, you need install python3 via terminal.Then use python3 to run it.

```
python3 run.py
```

If the required file exists,the program will be run.

Next, just follow the prompts.

Compared to "common","database" will use "username.txt".

---

## Common and Database mode

```
Do you want to use .html ?[Y/n]:
```

Press "Y" will create xxx.html files.

Finally, you will found subscription files in "subscription" directory.

Before using it, you need to ensure that "password.txt" and "url.txt" exist in its siblings, and write them as required.

---

## Add a user to mysql database

With this mode, you can add new trojan password.

---

### password.txt

This file need be filled with your trojan password,fill in one password per line.

Just like this:

```
password
```
or
```
password1
password2
password3
.
.
.
```

Each password will generate a separate file instead of being in the same file.


### url.txt

The same as password.txt,this file need be filled with your trojan address,fill in one address per line.

Example:

```
url:443
```

or

```
url1:443#UK-10Gbps
url2:443
.
.
.
```

---

If Use Trojan-Panel,you can run "database.py",before run it ,you should create a new file named "username.txt",format sits the same as them.

Before using it, you need to ensure that "password.txt","url.txt","config.cfg" and "ftp.py" exist in its siblings, and write them as required.

### config.cfg

```
[FTP]

server = 127.0.0.1
port = 21
user = users
password = password
dir = /path/to/sub/dir

[Mysql]

dbserver = 0.0.0.0
dbname = trojan
username = trojan
password = password 
```
