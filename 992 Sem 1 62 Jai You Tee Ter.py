x = input().split()
y,z,yy,zz = '','','',''
for i in range(len(x[0])):
    if x[0][i] in 'aeiou':
        yy += x[0][i:]
        break
    y += x[0][i]
for i in range(len(x[-1])):
    if x[-1][i] in 'aeiou':
        zz += x[-1][i:]
        break
    z += x[-1][i]
x[0] = y+zz
x[-1] = z+yy
print(' '.join(x))
    
        