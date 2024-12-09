from aoc import strdict
data = strdict(6, cpx=True)
t = min(i for i in data if data[i] == "^")
h = {i for i in data if data[i] == "#"}
d = set(data) - h

y, p, v, z = set(), t, -1, 0
while p in d:
    y.add(p)
    while p+v in h:
        v *= 1j
    p += v

for i in set(data) - set([t]):
    s, p, v = set(), t, -1
    while p in d and (p, v) not in s:
        s.add((p, v))
        while p+v in h or p+v == i:
            v *= 1j
        p += v
    z += p in d

print(len(y), z)
