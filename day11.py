from aoc import intlist
from collections import Counter
y = [Counter(intlist(11, d=" "))] + [Counter() for j in range(75)]
y = [Counter(map(int, "125 17".split()))] + [Counter() for j in range(75)]

for j, k in zip(y, y[1:]):
    for i in j:
        if i == 0:
            k[1] += j[i]
        elif len(t:=str(i))%2 == 0:
            k[int(t[len(t)//2:])] += j[i]
            k[int(t[:len(t)//2])] += j[i]
        else:
            k[i*2024] += j[i]

print(y[25].total(), y[75].total())

p = intlist(11, d=" ")
from time import time
z = time()
for i in range(25):
    q = []
    for j in p:
        if j == 0:
            q.append(1)
        elif len(t:=str(j))%2 == 0:
            q.append(int(t[len(t)//2:]))
            q.append(int(t[:len(t)//2]))
        else:
            q.append(j*2024)
    p = q
