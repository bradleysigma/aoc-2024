from aoc import strdict, adjt, diag
data = strdict(4)
print(sum(all(data.get((i+u*k, j+v*k)) == c for k, c in enumerate("XMAS")) for u, v in adjt for i,j in data),
      sum(sum(all(data.get((i+u*k, j+v*k)) == c for k, c in enumerate("MAS", -1)) for u, v in diag) == 2 for i,j in data))
