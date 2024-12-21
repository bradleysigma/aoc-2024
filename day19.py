p, q = [i.split("\n") for i in open("input19.txt").read().strip().split("\n\n")]
p, y, z, i = set(p[0].split(", ")), set(), 0, -1
while (i:=i+1) < len(q) and (r := {q[i]: 1}) or print(len(y), z):
    while r and (k := r.pop(j := max(r, key=len))):
        y, z = (y|{i}, z+k) if j == "" else (y, z)
        r.update({j[n:]: r.get(j[n:], 0) + k for n in range(1, len(j)+1) if j[:n] in p})
