from aoc import strlist
from math import log10, ceil
data = strlist(7)

y, z = 0, 0
for i, *j in map(lambda x: map(int, x.replace(": ", " ").split(" ")), data):
    u, v = [j[0]], [j[0]]
    for t in j[1:]:
        u = filter(i.__ge__, [e for k in u for e in (k+t, k*t)])
        v = filter(i.__ge__, [e for k in v for e in (k+t, k*t, k*10**ceil(log10(t+1))+t)])
    y += i * (i in u)
    z += i * (i in v)
print(y, z)
