# trojan-subscription-builder
A Mini Python Program to Build Trojan Subscription file.

---

**Attention: You need to run this program with python3.**

### Useage

To use it,just run "run.py".

For mac, you need install python3 via terminal.

```
python3 run.py
```

If the required file exists,the program will be run.

Next,the program will ask you if you want to use ".html" suffix.

```
Do you want to use .html ?[Y/n]:
```

Press "Y" will cteate xxx.html files.

Finally, you will found subscription files in "subscription" directory.

Before using it, you need to ensure that "password.txt" and "url.txt" exist in its siblings, and write them as required.

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
