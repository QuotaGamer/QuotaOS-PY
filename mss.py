import sys, os
from system.ver import version
from users.users import users
from system.functions import clear, about
args=list(sys.argv)
if len(args) >= 3:
    print("Please only run this through the login.py")
elif len(args) == 1:
    print("Only run this through the login.py")
else:
    username=args.pop(1)
    print(f"Attempting login as: {username}")
    if username in users:
        pass
    elif username == "qlog":
        print("qLog used to log in.")
    else:
        print("Login failed.")
        exit()

def mainInterface() -> None:
    clear()
    print(f"""
  Welcome to QuotaPYOS
  Version: {version}
  
  User: {username}
1. Applications (Broken)
2. About Quota-PY OS (Broken)
3. Exit Quota-PY OS
4. Restart OS (Broken)
5. Add a user (Broken)
6. Switch users (Broken)
7. Check for updates (Broken)""")
    choice:int=input("> ")
    print(choice)
    if choice == 3:
        print("Exiting...")
        exit()
    # if choice == 2:
    #     print("About")
    #     about()
    #     print("Interface!")
    #     input()
    #mainInterface()

mainInterface()