import sys
import functools as ft
import itertools as it

a = """1 3
2 5
5 8
3 6
2 5
3 8
3 6
3 8"""


# manteaux = []
# n = int(sys.stdin.readline())
# for i in range(n):
#     manteaux.append(sys.stdin.readline().split(" "))

import itertools


n = 8
manteaux = [[*map(int,m.split(" "))] for m in a.split("\n")]
manteaux.sort()

g = [[a[0], sorted(a[1],key=lambda m:m[1], reverse=True)] for a in it.groupby(manteaux, key=lambda m:m[0])]
g = [gi for gn in g for gi in gn[1]]

# include = lambda g1,g2: g1[0]>=g2[0] and g1[1]<=g2[1]

# print(g)

a = 0
for i,gi in enumerate(g):
    b = 0
    for j,gj in enumerate(g[i+1:]):
        if gi[0]>gj[0] or gi[1]<gj[1]:
            break
        b += 1
    if b>a:
        a = b
print(a)

# a = 0
# for gn in g:
#     for gi in gn[1]:
#         gm = gi
#         print(gi)
