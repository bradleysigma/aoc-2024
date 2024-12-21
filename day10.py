from aoc import intgrid
data, y, z = intgrid(10, cpx=True), 0, 0
for i in [set([(j,)]) for j in data if data[j] == 0]:
    for j in range(9):
        i = {t + (k + t[-1],) for t in i for k in [1, -1, 1j, -1j] if data.get(t[-1] + k) == j+1}
    y, z = y + len(set(t[-1] for t in i)), z + len(i)
print(y, z)
