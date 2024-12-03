print(*(lambda d,f:[sum(map(f,d)),sum(any(f(x[:n]+x[n+1:]) for n in range(len(x))) for x in d)])
 ([list(map(int,t.split())) for t in open("input2.txt")],lambda x:any(all(0<s*(k-j)<=3 for j,k in zip(x,x[1:])) for s in (1,-1))))
