p, d = [i.split("\n") for i in open("input15.txt").read().split("\n\n")]
q = ["".join(j+{"O": "-", "@": "."}.get(j, j) for j in i) for i in p]
p, q = ({i+j*1j: k[j][i] for j in range(len(k)) for i in range(len(k[j]))} for k in [p,q])
u, v = (min(i for i in k if k[i] == "@") for k in [p,q])

for i in map({"^": -1j, "<": -1, ">": 1, "v": 1j}.get, "".join(d)):
    if p[u+i*(n:=next(j for j in range(1, 50) if p[u+i*j] != "O"))] != "#":
        p, u = p|{u+i*j+i: p[u+i*j] for j in range(n)}, u+i

    if i.real or (e:={v}) and (m:={}):
        if q[v+i*(n:=next(j for j in range(1, 100, 2) if q[v+i*j] not in "O-"))] != "#":
            q, v = q|{v+i*j+i: q[v+i*j] for j in range(n)}, v+i
    while i.imag and not (b := all(q[j+i] == "." for j in e)) and not any(q[j+i] == "#" for j in e):
        e = set.union(*[{"O": {j+i, j+i+1}, "-": {j+i, j+i-1}}.get(q[j+i], set()) for j in e])
        m.update({j: q[j] for j in e})
    if i.imag and b:
        q, v = q|{j: "." for j in m} | {j+i: m[j] for j in m}, v+i

print(*[int(sum(100*i.imag+i.real for i in k if k[i] == "O")) for k in (p,q)])
