
a,b,c = [int(e) for e in input().split()]
nisit = {}
g = {}
for i in range(a):
    y = input().split()
    nisit[y[0]] = y[1]
for i in range(b):
    y = input().split()
    g[y[0]] = y[1:]
for i in range(c):
    w = input().split()
    s = set()
    x = set()
    for p,e in enumerate(w):
        for k in g[e]:
            if p == 0:
                s.add(nisit[k])
            else:
                x.add(nisit[k])
        if p!= 0:
            s =  x&s
            x = set()
    if len(s) == 0:
        print("None")
    else:
        print(' '.join(list(s)))



"""
8 3 2
Luffy faculty_a
Nami faculty_a
Sanji faculty_b
Zoro faculty_c
Robin faculty_c
Chopper faculty_a
Brook faculty_c
Franky faculty_b
Eren Nami Chopper Brook
Anya Sanji Luffy
Yaiba Franky
Eren Anya
Anya Eren Yaiba"""