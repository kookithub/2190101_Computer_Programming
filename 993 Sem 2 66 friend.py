def read_friends():
    dat = []
    N = int(input())
    for i in range(N):
        dat.append(tuple(input().strip().split()))
    return dat
def count_friends(data, names):
    f = {}
    fp = [e[0] for e in data]
    sp = [e[1] for e in data]    
    for e in range(len(fp)):
        if fp[e] in f:
            f[fp[e]].append(sp[e])
        else:
            f[fp[e]] = [sp[e]]
    for e in range(len(sp)):
        if sp[e] in f:
            f[sp[e]].append(fp[e])
        else:
            f[sp[e]] = [fp[e]]        
    for k in f:
        f[k] = list(set(f[k]))
    c = 0
    z = []
    for n in names:
        if n not in f:
            z.append((n,0))
        else:
            z.append((n,len(f[n])))
    return sorted(z)
exec(input().strip())