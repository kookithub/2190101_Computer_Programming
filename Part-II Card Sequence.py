c = {'A':1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,'T':10,'J':11,'Q':12,'K':13}
s = {'C':1,'D':2,'H':3,'S':4}
x = input()
z = []
for i in range(int(len(x)-2)):
    if i%2 == 0:
        if x[i] != x[i+2]:
            p =(c[x[i]] - c[x[i+2]])
        else:p = (s[x[i+1]] - s[x[i+3]])
        if p > 0:
            z.append('+'+str(p))
        else:
            z.append(str(p))
print(''.join(z))
#18 min