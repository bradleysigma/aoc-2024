from aoc import strlist
data = strlist(1)
p,q = map(sorted, zip(*[map(int, i.split()) for i in data]))
print(sum(abs(i-j) for i,j in zip(p,q)), sum(i*q.count(i) for i in p))
