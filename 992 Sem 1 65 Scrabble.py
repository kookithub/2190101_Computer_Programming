def countpoint(x):
    l = (['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], ['D', 'G'], ['B', 'C', 'M', 'P'], ['F', 'H', 'V', 'W', 'Y'], ['K'], ['J', 'X'], ['Q', 'Z'])
    c = 0
    for a in x:
        for i in range(5):
            if a in l[i]:
                c += i + 1
        if a in l[5]:
            c += 8
        if a in l[6]:
            c += 10
    return (c)

def memory(y):
    m = []
    for i in y:
        r = []
        r.append(countpoint(i))
        r.append(i)
        m.append(r)
    return m

word = input().split() + ['']
f = memory(word)
f.sort(reverse=True)
kk = []
ss = []
for k in range(len(f)-1):
    if f[k][0] == f[k+1][0]:
        ss.append(f[k])
    else:
        ss.append(f[k])
        z = [[e[1],e[0]] for e in ss]
        kk.append(sorted(z))
        ss = []
nn = []
for p in kk:
    for q in p:
        nn.append(q)
aa = [[e[0],str(e[1])] for e in nn]
for ss in aa:
    print(' '.join(ss))


    
    