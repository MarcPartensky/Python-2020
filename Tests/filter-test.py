f = lambda n:n%2==0
l = range(10)
r = filter(f, l)
print(next(r))
