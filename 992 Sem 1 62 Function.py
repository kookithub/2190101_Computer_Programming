import math 
def Permutation(p):
    x = {}
    t = 1
    for e in p:
        if e in x:
            x[e] += 1
        else:
            x[e] = 1
    for i in x:
        t = t*math.factorial(x[i])
    return (int(math.factorial((len(p)))/t))
        
    
def Bids(p1, p2): 
    tp1 = 0
    tp2 = 0
    for e in p1:
        if e in p2:
            if p2[e] > p1[e]:
                tp2 += p2[e]
            elif p1[e] > p2[e]:
                tp1 += p1[e]
        else: tp1 += p1[e]
    for e in p2:
        if e not in p1:
            tp2 += p2[e]
    result = [tp1,tp2]
    return result
def AdvFind(s, p):
    i = []
    q = p.find(s)
    i.append(q)
    while q != -1:
        q = p.find(s,q+1)
        if q != -1:
            i.append(q)
    return i
        
exec(input())