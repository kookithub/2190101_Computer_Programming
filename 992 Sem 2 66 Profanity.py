def rpw(bw):
    kk = ''
    for e in bw:
        if e.lower() in ['a','e','i','o','u']:
            kk += '*'
        else: kk += e
    return kk
def lo(ss,ow):
    k = ''
    q = 0
    p = ss.lower().find(ow,q)
    while p != -1:
        p = ss.lower().find(ow,q)
        k += ss[q:p]
        k += rpw(ss[p:p+len(ow)])
        q = p + len(ow)
        if p == -1:
            k += s[-1]
    return k
    
kw = input().lower().split()
s = input()
aa = s
for e in kw:
    aa = (lo(aa,e))
print(aa)
#1 hr 26 min 
        