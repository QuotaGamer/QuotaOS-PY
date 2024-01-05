import os
from system.about import ABOUTTEXT

def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def about() -> None:
    clear()
    print(ABOUTTEXT)
    input("Press enter to exit.")