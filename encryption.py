from cryptography.fernet import Fernet
import rsa

passwd = input("Original: ")
rsaPub, rsaPriv = rsa.newkeys(512)
key = Fernet.generate_key()

fernet = Fernet(key)
encMessage = fernet.encrypt(passwd.encode())
with open('s.aof', 'a') as f:
    f.write(encMessage)
decMessage = fernet.decrypt(encMessage).decode()
if decMessage == passwd:
    print("Password is secured.")