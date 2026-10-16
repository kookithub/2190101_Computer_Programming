f = {}
while True:
    y = input().split()
    if len(y) == 1:break
    f[y[0]] = y[1:]
y = input().split()
h = set()
for e in y:
    if e in f:
        for k in f[e]:
            h.add(k)
p = {}
for e in f:
    p[e] = 0
for i in f.items():
    c = 0
    for j in list(h):
        for k in i[1]:
            if j == k:
                p[i[0]] += 1
z = {}
for e in p:
    if e not in y:
        z[e] = p[e]
l = z.items()
k = max(list(z.values()))
ans = []
for e in l:
    if e[1] == k and k != 0:
        ans.append(e[0])
if len(ans) == 0:
    print("No suggested clip")
else:
    print(' '.join(sorted(ans)))

        
    
         

            
            
