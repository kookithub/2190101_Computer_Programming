n = int(input())
inf = []
for i in range(n):
    inf.append(input().split())
u = [int(e[0]) for e in inf]
c = [int(e[1]) for e in inf]
start = int(input())
ans = [(start)]
ener = 0
for i in range(n-1):
    if c[start]%2 == 0:
        q = 1
    else: q = 0
    z = ([e for e in c if c.index(e) not in ans and e%2 == q])
    nxt = z[z.index(min([e%151 for e in z]))]
    ss = c.index(nxt)
    ans.append(ss)
    ener += u[ss]%151
    start = ss
    
print(' '.join([str(e) for e in ans]))
print((ener))