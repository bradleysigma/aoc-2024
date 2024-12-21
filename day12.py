from aoc import strdict
data = strdict(12, cpx=True)
y, z = 0, 0

for i, t in data.items():
    if t is None: continue
    p, q = set([i]), set()
    while len(q) < len(p):
        q = p
        p = {j+k for k in [1, -1,1j, -1j, 0] for j in q if data.get(j+k) == t}
    data.update({j: None for j in p})
    r = {(j, k) for k in [1, -1, 1j, -1j] for j in p if j+k not in p}
    y += len(p) * sum(j+k not in p for k in [1, -1, 1j, -1j] for j in p)
    z += len(p) * sum((j+k*1j, k) not in r for j, k in r)

print(y, z)
