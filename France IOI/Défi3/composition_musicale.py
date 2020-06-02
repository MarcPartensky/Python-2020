l = list(input())
# l = list("baaabbacddc")
o = []
for c in l:
    if len(o)>0:
        if c==o[-1]:
            del o[-1]
            continue
    o.append(c)
print("".join(o))





morceau = list(input())
condition = True

while condition:
    n = len(morceau)
    for i in range(n - 1):
        if morceau[i] == morceau[i + 1]:
            del morceau[i]
            del morceau[i + 1]
        else:
            condition = False

print("".join(morceau))
