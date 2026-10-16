s = input()
c =[]
y = ''
sc = []
ss = 0
for i in s:
    if i == 'X':
        c.append(i)
    elif i == '/':
        y += i
        c.append(y)
        y = ''
    else:
        if len(y) == 0:
            y += i
        elif len(y) == 1:
            y += i
            c.append(y)
            y = ''
if c[9][0] == 'X':
    c[9] = s[len(''.join(c[0:9])):]
    c.pop(10)
elif c[9][1] == '/':
    c[9] = s[len(''.join(c[0:9])):]
for i in range(len(c)-1):
    if c[i] == 'X':
        if c[i+1].isdigit():
            ss += 10 + int(c[i+1][0]) + int(c[i+1][1])
        elif c[i+1] == 'X':
            if c[i+2] != 'X':
                ss += 20 + int(c[i+2][0])
            else: ss += 30
        else: ss+= 20
    elif c[i][-1] == '/':
        if c[i+1] == 'X': 
            ss += 20
        else: ss += 10 + int(c[i+1][0])
    else: ss += int(c[i][0]) + int(c[i][1])
    sc.append(ss)
    ss = 0    
if len(c[9]) == 3:
    if c[9] == 'XXX':
        ss += 30
    elif c[9][:2] == 'XX':
        ss += 20 + int(c[9][-1])
    elif c[9][0] == 'X': #might be error in case third time is / 
        ss += 10 + int(c[9][1]) + int(c[9][2])
    elif c[9][1] == '/':
        ss += 10 + int(c[9][2]) #might be error in case third time is X
else: ss += int(c[9][0]) + int(c[9][1])
sc.append(ss)
n = int(input())
if n <= 10 and n >= 1:
    print (sc[n-1])
else: print(sum(sc))
                
    
    
            
        

