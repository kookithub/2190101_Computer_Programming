def Mult_Const(p, k):
    x = dict(p)
    for e in x:
        x[e] = x[e]*k
    return x
def Mult_Mono(p, k):
    p = Mult_Const(p,(list(k.values())[0]))
    pp = {}
    for e in p:
        pp[e+(list(k.keys()))[0]] = p[e]
    return pp
def Add_Poly(p1, p2):
    pp = {}
    for e in p1:
        if e in p2:
            pp[e] = p1[e] + p2[e]
        else:
            pp[e] = p1[e]
    for e in p2:
        if e not in pp:
            pp[e] = p2[e]
    ppp = {}
    for e in pp:
        if pp[e] != 0:
            ppp[e] = pp[e]
    
    return ppp
def Mult_Poly(p1, p2):
    x = []
    for e in p2:
        x.append(Mult_Mono(p1,{e:p2[e]}))
    z = Add_Poly(x[0],x[1])    
    return z
k1 = 7
k2 = -5 
p1 = {3: 5}   
p2 = {5: 3, 3: -1, 0: 5} 
p3 = {3: 1, 2: 2, 1: 5, 0: -5}
p4 = {7: 2, 5: -7}  #
p5 = {2: 7, 0: 9}
exec(input())