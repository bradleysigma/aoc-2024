d = [i+j*1j for i,j in [map(int, k.split(",")) for k in open("input18.txt")]]
u, v, g, y = -len(d)+2048, len(d), 70+70j, None
while v-u > 1 or print(y, f"{int(d[u].real)},{int(d[u].imag)}"):
    c, f = set(d[:(t := (u+v)//2)]), {0+0j: 0}
    while g not in f and (x := min(set(f)-c, key=f.get, default=None)) is not c.add(x):
        f |= {i: min(f[x]+1, f.get(i, 999)) for i in {x+1, x-1, x+1j, x-1j}-c if all(0<=j.real<=70 for j in [i, -1j*i])}
    (u, v), y = (u, t) if x is None else (t, v), f[g] if t == 1024 else y
