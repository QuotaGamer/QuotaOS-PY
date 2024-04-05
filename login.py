from system.loginText import LOGINTEXT
from system.opts import qlog as q
from users.users import users
import os

if q == True:
    print("Quick Login (qlog) enabled.")
print(LOGINTEXT)
a:list=list(users.keys())
d:str=""
a.reverse()
for i in a: d:str=f"{i}, {d}"
d:str=d.removesuffix(", ")
print(d)