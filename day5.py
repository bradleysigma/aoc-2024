from aoc import strgroups
p, q = ([list(map(int, j.split(s))) for j in x] for x,s in zip(strgroups(5), "|,"))
y, z = 0, 0
for t in q:
    if not any(i in t and j in t and t.index(i) > t.index(j) for i,j in p):
        y += t[len(t)//2]
    else:
        z += sorted(t, key=[i for i,j in p if j in t].count)[len(t)//2]
print(y, z)
