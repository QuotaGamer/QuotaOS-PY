import rsa, os, json

j:dict=json.load(open("users/users.json", "r"))
print(j)

# passwd = input("Original: ")