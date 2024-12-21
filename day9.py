from aoc import read
data = list(map(int, read(9)))
b, g, x = data[::2], data[1::2]+[0], list(range(len(data+[0])//2))
i, j, t, y = -1, len(b)-1, 0, 0
while (k:=0)*(i:=i+1) or i<=j:
    y, t, b[i] = y + x[i]*(b[i]*(t-1) + b[i]*(b[i]+1)//2), t+b[i], 0
    while k < g[i] and (d := min(g[i] - k, b[j])):
        y += x[j]*(d*(t-1) + d*(d+1)//2)
        t, b[j], j, k = t+d, b[j]-d, j-(b[j]==d), k+d

b, v, t, z = data[::2], [[i] for i in range(len(data+[0])//2)], 0, 0
for j in range(len(b)-1, -1, -1):
    if (i := min((k for k in range(j) if b[j] <= g[k]), default=None)) is None: continue
    v[i], v[j] = v[i] + [j], [k for k in v[j] if k!=j]
    g[i], g[j-1] = g[i] - (i!=j-1) * b[j], g[j-1] + (i!=j-1) * b[j]

for i, h in zip(v, g):
    z += sum(j*(b[j]*(t+sum(b[i[k]] for k in range(g))-1) + b[j]*(b[j]+1)//2) for g,j in enumerate(i))
    t += sum(b[j] for j in i) + h

print(y, z)
