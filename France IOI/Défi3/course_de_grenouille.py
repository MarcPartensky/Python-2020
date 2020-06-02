g = int(input()) #grenouilles
t = int(input()) #tours

p = [0 for i in range(g)]
tete = [0 for i in range(g)]

for i in range(t):
    if p.count(max(p))==1:
        tete[p.index(max(p))] += 1
    gi, pi = map(int, input().split(" "))
    p[gi-1] += pi

print(tete.index(max(tete))+1)
