# n = int(input())
# l = list(map(int, input().split(' ')))
import numpy as np
# l = list(map(lambda x:int(3*x+1), np.random.rand(1000)))
l = [2, 1]
print(l)
o = 0
u, d, t = 0, 0, 0

for e in l:
    if e == 4:
        o+=1
    elif e==3:
        if u:
            u-=1
            o+=1
        else:
            t += 1
    elif e==2:
        if d:
            d-=1
            o+=1
        elif u//2:
            u-=2
            o+=1
        else:
            d += 1
    else:
        if t:
            t-=1
            o+=1
        elif d and u:
            d-=1
            u-=1
            o+=1
        elif u//3:
            u-=d
            o+=1
        else:
            u+=1

print((3*u+2*d+t)//6)
print(u, t, d)
print(o+t+d+u-int(u==d==1))
