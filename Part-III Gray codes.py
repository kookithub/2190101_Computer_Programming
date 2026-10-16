def gray(x):
    y = x[-1::-1]
    x = [f"0{str(e)}" for e in x]
    y = [f"1{str(e)}" for e in y]
    z = x+y
    return z
z = ['0','1']

n = int(input())
k = int(input())
if n != int(abs(n)) and k < 1:
    print("Invalid n and k")
elif n != int(abs(n)):
    print("Invalid n")
elif k < 1:
    print("Invalid k")
else:
    for i in range(n):
        z = gray(z)
p = []
for e in range(len(z)//k+1):
    y = []
    for i in range(k):
        y.append(z[i*(e+1)])
    p.append(y)
for e in p:
    
    print(','.join(e))
      
    
print(z)