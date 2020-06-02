a = [*zip(range(5), range(5))]
b = [d for c in a for d in c]

print(b)
