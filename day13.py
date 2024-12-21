from aoc import strgroups
from sympy import linsolve, symbols
data, (pa, pb), y, z = strgroups(13), symbols("pa pb"), 0, 0
for a, b, g in data:
    _, ax, _, ay = a.replace(",","+").split("+")
    _, bx, _, by = b.replace(",","+").split("+")
    _, gx, _, gy = g.replace(",","=").split("=")
    ax, ay, bx, by, gx, gy = map(int, [ax, ay, bx, by, gx, gy])
    (sa, sb), = linsolve([ax*pa+bx*pb-gx, ay*pa+by*pb-gy], (pa, pb))
    y += 3*sa + sb if sa == int(sa) and sb == int(sb) else 0
    (sa, sb), = linsolve([ax*pa+bx*pb-gx-10**13, ay*pa+by*pb-gy-10**13], (pa, pb))
    z += 3*sa + sb if sa == int(sa) and sb == int(sb) else 0
print(y, z)

print(*[sum((3*(q*(x+n)-p*(y+n))+(i*(y+n)-j*(x+n)))//(i*q-j*p) for (i, j, p, q, x, y) in [map(int, t.translate({10: 43, 44: 43, 61: 43}).split("+")[1::2]) for t in open("input13.txt").read().split("\n\n")] if not ((q*(x+n)-p*(y+n))%(i*q-j*p) or (i*(y+n)-j*(x+n))%(i*q-j*p))) for n in [0, 10**13]])
