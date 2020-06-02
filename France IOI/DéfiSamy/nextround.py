import sys
n, k = list(map(int, sys.stdin.readline().split(' ')))
l = list(map(int, sys.stdin.readline().split(' ')))

m = l[k-1]

for i,e in enumerate(l):
    if e<m or e==0:
        i-=1
        break

print(i+1)
