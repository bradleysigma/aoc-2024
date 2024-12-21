from aoc import strlist, vec
data, r, z, f = strlist(14), vec([101, 103]), 0, lambda x: [(j+100*k)%r for j,k in zip(*x)]
p, v = ([vec(map(int, i.split(" ")[j].split("=")[1].split(","))) for i in data] for j in (0,1))
y = [[t < r//2, t < r//2+1, t < r//vec([1,2]), t < r//vec([2,1]), t > r//2, 1].index(1) for t in f((p, v))]
while (z:=z+1) and len(set(p:=[(i+j)%r for i,j in zip(p,v)])) != len(p): pass
print(y.count(0)*y.count(2)*y.count(3)*y.count(4), z)
print("\n".join("".join("#" if vec([i,j]) in set(p) else " " for i in range(101)) for j in range(103)))
