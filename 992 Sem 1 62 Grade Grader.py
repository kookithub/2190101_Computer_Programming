name = input()
n = int(input())
f = open(name,'r')
inf = []
for line in f:
    x = line.split()
    if x[1] =='I':
        xx = []
        for i in x:
            if i.isdigit():
                xx.append(int(i))
            elif i == '-':
                xx.append(0)
            else: xx.append(i)
        sc = max(xx[2],xx[5]) + max(xx[3],xx[6]) + max(xx[4],xx[7]) + xx[8] + xx[9] + xx[10]
        inf.append([sc,xx[0]])
inf.sort(reverse=True)
ff = []
if n < len(inf):
    for i in range(n):
        ff.append(inf[i])
else: ff = inf
ff += ['0']
fff = []
yy = []
for i in range(len(ff)-1):
    if ff[i][0] == ff[i+1][0]:
        yy.append(ff[i])
    else:
        yy.append(ff[i])
        fff.append(yy)
        yy = []
if len(yy) != 0:
    fff.append(yy)
for e in fff:
    e = (sorted([[k[1],k[0]] for k in e]))
    for i in e:
        print(f"{i[1]} --> {i[0]}")


    

    
    