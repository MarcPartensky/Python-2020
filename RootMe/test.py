import requests

for i in range(10):
    r = requests.get('http://challenge01.root-me.org/web-serveur/ch14/')
    print(r.text)

