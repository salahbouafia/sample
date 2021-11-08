
import requests

r = requests.get("httep://youtube.com")
print(r.status_code)
print(r.ok)
