d, t, y, q = list(open("input17.txt")), 0, [], {0}
(a, b, c), p = (int(i.split(" ")[-1]) for i in d[:3]), list(map(int, d[-1].split(" ")[-1].split(",")))
for i in p[::-1]: q = {k for j in q for k in [(j<<3)+n for n in range(8)] if (k%8^p[3]^k>>(k%8^p[3])^p[7])%8 == i}
while t < len(p) and ((r := [0, 1, 2, 3, a, b, c, None][p[t+1]]) or 1) or print(",".join(map(str, y)), min(q)):
    a, b, c = {0: a>>r}.get(p[t], a), {1: b^p[t+1], 2: r%8, 4: b^c, 6: a>>r}.get(p[t], b), {7: a>>r}.get(p[t], c)
    y, t = y + ([r%8] if p[t] == 5 else []), (p[t+1] if p[t] == 3 and a else t+2)
