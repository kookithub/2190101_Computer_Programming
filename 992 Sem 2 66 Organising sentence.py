n = input()
s1 = open(n,'r')
ff = s1.read().split()
s1.close()
ss = []
ff = '_'.join(ff)
p = -1
q = 0
y = ''
while len(ss) != round(len(ff)/50)+2 and ff.find('_',p+1) > 0:
    p = ff.find('_',p+1)
    if len(y + ff[q:p]) <= 50:
        y += ff[q:p]
        q = p
    else:
        ss.append(y)
        y = ff[q+1:p]
        q = p
ss.append(y)
y = ff[q+1:]
ss.append(y)

for e in ss:
    if len(e) != 0:
        print(e)

        
    