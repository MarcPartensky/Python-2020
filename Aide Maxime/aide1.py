"""
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
"""


from sys import stdin
d = dict([next(stdin).rstrip().split(' ') for i in range(int(next(stdin).rstrip()))])
print("\n".join([cle.rstrip() if cle.rstrip()  in d  else "Not Found" for cle in stdin]))


n = int(input())
d = {}

for i in range(n):
    key, value = input().split(' ')
    d[key] = value

while True:
    try:
        key = input()
        if key in d:
            print("{}={}".format(key, d[key]))
        else:
            print("Not Found")
    except:
        break
