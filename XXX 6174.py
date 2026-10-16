n = (input())
while n != "6174":
    a = [n[0],n[1],n[2],n[3]]
    c = int(''.join(sorted(a)))
    b = int(''.join(sorted(a,reverse=True)))
    n = str(b - c)
    print(n)
    
    