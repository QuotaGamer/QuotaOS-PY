import sys, os
from colorama import Fore
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
  Welcome to QuotaOS-PY
  Version: {version}
  
  User: {username}
1. {Fore.LIGHTGREEN_EX}Applications {Fore.RED}(Broken){Fore.WHITE}
2. {Fore.CYAN}About QuotaOS{Fore.WHITE}
3. {Fore.RED}Exit{Fore.WHITE}
4. {Fore.MAGENTA}Restart {Fore.WHITE}or {Fore.MAGENTA}Switch user{Fore.WHITE}
5. Add a user {Fore.RED}(Broken){Fore.WHITE}
6. Check for updates {Fore.RED}(Broken){Fore.WHITE}
""")
    choice=int(input("> "))
    if choice == 1:
        raise NotImplementedError("I haven't made this yet, but it's next.")
    elif choice == 2:
        about()
    elif choice == 3:
        print("Goodbye!")
        exit()
    elif choice == 4:
        print("Restarting..")
        clear()
        os.system("python login.py")
        exit()
    elif choice == 5:
        raise NotImplementedError("You cannot currently make new users.")
    elif choice == 6:
        raise NotImplementedError("You cannot currently check for updates.")
    mainInterface()

mainInterface()