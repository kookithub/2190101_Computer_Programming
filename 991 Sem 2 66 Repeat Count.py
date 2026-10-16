p = input()
n = int(input())
for x in range(n):
    t = input()
    z = 1
    k = 0
    while k < (len(t)-len(p)+ 1):
        if p == t[k:k+len(p)] and p == t[k+len(p):k+(2*len(p))] :
            k += len(p)
            z += 1
            
        else:k += 1
    if z == 1:
        print(0)
    else:print(z)