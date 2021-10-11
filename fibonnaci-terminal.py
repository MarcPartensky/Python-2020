#!/usr/bin/env python


def fibo(n, un1=1, un0=1):
    if n <= 1:
        return un0
    else:
        return fibo(n - 1, un1 + un0, un1)


print(fibo(8))
print(fibo(1))
