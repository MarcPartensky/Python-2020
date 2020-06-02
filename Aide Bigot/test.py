import zlib
import json

with open('logMain.txt', encoding='utf-8') as file:
    print(file.read()[:100])
    #t = json.loads(file.read())
    #for k, v in t.items():
    #    print(k, v)
    print(zlib.decompress(file.read()))
