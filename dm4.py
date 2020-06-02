import itertools
import math

def derangements(n):
    return int(math.factorial(n)*sum([(-1)**k/math.factorial(k) for k in range(n+1)]))

for i in range(10):
    print(derangements(i))
