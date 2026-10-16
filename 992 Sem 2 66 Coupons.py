n = int(input())
cp = []
for i in range(n):
    x = input().split()
    for k in range(3):
        cp.append(x)
cpa = sorted([[int(e[1]),e[0]] for e in cp],reverse=True)
pts = int(input())
c = [e[1] for e in cpa]
p = [e[0] for e in cpa]
s = 0
b = pts
use = []
if pts < p[-1]:
    print(f"> {pts} {s} {pts-s}")
    print("No coupon")
else:
    while b >= min(p):
        for i in p:
            if b >= i:
                s += p[(p.index(i))]
                use.append(c[(p.index(i))])
                b = pts - s 
    print(f"> {pts} {s} {b}")
use = sorted(use) + ['']
ans = []
c = 1
for i in range(len(use)-1):
    if use[i] == use[i+1]:
        c += 1
    else:
        ans.append([use[i],c])
        c = 1

for i in ans:
    print(i[0],i[1])
# 1 hr 3 min