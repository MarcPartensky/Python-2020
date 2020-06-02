# n = int(input())
# l = list(map(int, input().split(' ')))
#
# s = sum(l)
#
# if s%3!=0:
#     print(0)
# else:
#     if s==0:
#          c = l.count(0)
#          if c<2:
#              print(0)
#          else:
#             print(c-1)
#     else:
#         print(l.count(0)+1)

def countZero(n, l=3):
    if l==1: return 1
    return sum([countZero(n-i, l-1) for i in range(1,n)])

print(countZero(1000))
