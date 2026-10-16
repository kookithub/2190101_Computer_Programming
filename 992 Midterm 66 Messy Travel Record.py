def create_record():
    x = input()
    z = []
    while x != 'q':
        z.append(x.split())
        x = input()
    return z
def sort_list(z):
    y = [[e[0],[int(e[1].split('/')[-1]),int(e[1].split('/')[-2]),int(e[1].split('/')[0])],e[2]] for e in z]
    return sorted(y)
def create_output(s):
    s += [['','']]
    out = []
    k = []
    for i in range(len(s)-1):
        if s[i][0] == s[i+1][0]:
            k.append(s[i])
        else:
            k.append(s[i])
            out.append(k)
            k = []
    y = []
    for e in out:
        m = []
        for i in e:
            m.append(f"{i[1][-1]}/{i[1][-2]}/{i[1][-3]}:{i[-1]}")
        y.append(f"{e[0][0]} {m}")
    return y
def main():
    o = create_record()
    if len(o) == 0:
        print("No records!")
    else:
        for i in (create_output(sort_list((o)))):
            print(i)
exec(input())
#57 min
        
        
        
        
            
        
    