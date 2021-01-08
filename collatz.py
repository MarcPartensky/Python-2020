#!/usr/bin/env python
import itertools as it; collatz = lambda n:len(list(it.takewhile(lambda n:n>1, (n:=(n//2 if n%2==0 else 3*n+1) for a in it.repeat(1)))))+1
print(collatz(10))
