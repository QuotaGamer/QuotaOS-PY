from system.loginText import LOGINTEXT
from system.opts import qlog as qopt
from users.users import users
import os

if qopt == True:
    print("Quick Login (qlog) enabled.")
print(LOGINTEXT)
b=users.keys()
a=str(b)
a=a.replace("dict_keys([", "")
a=a.replace("])", "")
a=a.replace("'", "")
a=a.replace(" ", "")
c=a.split(",")
d=[]
for name in c:
    d.append(users[name])
for entry in d:
    if entry == '':
        d.remove(entry)
a=a.replace(",", ", ")
print(f"Valid users: {a}")
#print(f"(Debug) Valid passwords: {d}")
username = input("Username> ")
if username == "guest":
    os.system("python mss.py guest")
    exit()
elif username == "qlog":
    if qopt == True:
        os.system("python mss.py qlog")
    else:
        print("Nuh uh.")
    exit()
elif username in a:
    if username == "quota":
        passwd=input("Password> ")
        if passwd == users[username]:
            os.system(f"python mss.py {username}")
            exit()