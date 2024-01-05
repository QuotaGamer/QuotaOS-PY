import os, requests
a = requests.get("https://raw.githubusercontent.com/QuotaGamer/QuotaOS/main/ver.txt")
print(a.text)