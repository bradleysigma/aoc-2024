d = {i+j*1j: k[i] for j,k in enumerate(open("input16.txt")) for i in range(len(k))}
(x, g), t = [min(i for i in d if d[i] == c) for c in "SE"], 0
d, p, y, z = {i for i in d if d[i] != "#"}, {0: [(x, 1, [x])]}, {}, set()
while t <= min(y.get((g,k), 10**9) for k in [1,1j,-1,-1j]):
    x, v, r = p[t:=min(p)].pop()
    if x == g: z = set(r) if t < min(y.get((g,k), 10**9) for k in [1,1j,-1,-1j]) else z.union(r)
    y[x,v], p = t, {i:j for i,j in p.items() if j}
    for u, c in [(-1j*v, 1001), (v, 1), (1j*v, 1001)]:
        if x+u in d and y.get((x+u, u), 10**9) > t+c:
            p.setdefault(t+c, []).append((x+u, u, r+[x+u]))
print(min(y.get((g,k), 10**9) for k in [1,1j,-1,-1j]), len(z))
