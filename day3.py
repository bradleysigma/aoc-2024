from re import split, findall
d = open("input3.txt").read().strip()
s = split("(do\(\)|don\'t\(\))", "do()" + d)
t = " ".join(j for i,j in zip(s[1::2], s[2::2]) if i == "do()")
print(*[sum(int(i)*int(j) for i,j in findall("mul\((\d+),(\d+)\)", x)) for x in (d, t)])
