import itertools as it


print(list(it.permutations(range(1,4))))


def match(a,b):
    for i in range(len(a)):
        if a[i]!=b[i] and a[i]!=0:
            return False
    return True

print(match([0,2,0],[1,2,3]))
