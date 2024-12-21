data = {i+j*1j: k[i] for j, k in enumerate(open("input20.txt")) for i in range(len(k.strip()))}
x, g = [min(i for i in data if data[i] == j) for j in "SE"]
d, b, p, y, z = {i for i in data if data[i] != "#"}, -1, {g: 0}, 0, 0
while (r:=d-set(p)) and (b:=b+1)>=0:
    p.update({i+v: b+1 for i in [j for j in p if p[j] == b] for v in [1, -1, 1j, -1j] if i+v in r})
for i, n in p.items():
    for j, w in ((k, m-n-100) for k, m in p.items() if m-n>=0):
        y += w >= abs((i-j).real) + abs((i-j).imag) <= 2
        z += w >= abs((i-j).real) + abs((i-j).imag) <= 20
print(y,z)
