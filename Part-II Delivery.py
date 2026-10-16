x = input()
z = []
d = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}
while x != 'END':
    x = x.split()
    if int(x[-1]) < 2558:
        print(f"Error: {x} --> Invalid year")
        if (int(x[-1])%4 == 0 and int(x[-1])%100 != 0) or int(x[-1])%400 == 0:
            d[2] = 29
        else:
            d[2] = 28
    elif int(x[-2]) not in range(1,13):
        print(f"Error: {x} --> Invalid month")
    elif  d[int(x[-2])] < int(x[-3]):
        print(f"Error: {x} --> Invalid date")
    elif x[1] not in 'EQNF':
        print(f"Error: {x} --> Invalid delivery type")
    else:
        z.append(x)
    x = input()
p = []
for i in z:
    m = int(i[3])
    y = int(i[4])
    if i[1] == 'E':
        nd = int(i[2]) + 1
    elif i[1] == 'Q':
        nd = int(i[2]) + 3
    elif i[1] == 'N':
        nd = int(i[2]) + 7
    else:
        nd = int(i[2]) + 14
    if nd > d[int(i[3])]:
        m += 1
        nd -= d[int(i[3])] 
    if m == 13:
        y += 1
        m = 1
    p.append([y,m,nd,int(i[0])])
p.sort()
for e in p:
    print(f"{e[-1]}: delivered on {e[2]}/{e[1]}/{e[0]}")

        
    
    