n = int(input())
v = list()
for i in range(n):
    x = input().split()
    v.append(x)
c = input().split()
   
    
if c[0] == 'show' :
    for i in range(n):
        print(' '.join(v[i]))
elif c[0] == 'max' :
    mx = []
    for i in range(n):
        mx.append(v[i][int(c[1])])
    cc = 0
    for i in range(n):
        if max(mx) == v[i][int(c[1])]:
            cc += 1
    if cc == 1:
        print(v[mx.index(max(mx))][0],max(mx))
    else:
        v = sorted(v)
        print(v[mx.index(max(mx))][0],max(mx))
elif c[0] == 'avg' :
    mx = []
    for i in range(n):
        mx.append(v[i][int(c[1])])
    mx = [float(e) for e in mx]
    print(round(sum(mx)/len(mx), 4))
elif c[0] == 'get' :
    mx = []
    for i in range(n):
        mx.append(v[i][0])
    if not c[1] in mx:
        print(f"{c[1]} not found")
    else:
        print(' '.join(v[mx.index(c[1])]))
elif c[0] == 'sort' :
    t = [(e[int(c[1])],e[0]) for e in v]
    t = sorted(t)
    ans = []
    for i in range(n):
        for k in range(n):
            if t[i][1] in v[k]:
                ans.append(v[k][0])
                break
    print(' '.join(ans))
    