x = input().split()
c = []
p = 0
cf = []
for i in range(10):
    for k in range(len(x)):
        if int(x[k]) == i:
            p += 1
    c.append(p)
    p = 0
for i in range(10):
    if int(c[i]) >= (len(x)/2):
        cf.append(i)
if len(cf) != 1:
    print(-1)
else: print(cf[0])