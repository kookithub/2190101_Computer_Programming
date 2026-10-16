i = input().split(',')
b = 0
r = 0
bf = 0
dwf = 0
for e in i:
    if e[6] == 'B':
        b += 1
    if e[6] == 'R' and e[-1] != '*':
        r += 1
        for ee in i:
            if e[:6] == ee[:6]:
                if e[-1] != '*' and int(e[7:])-int(ee[7:]) > 0:
                    bf += 1
                    dwf += int(e[7:])-int(ee[7:])
                    break
p = print
p(b);p(r);p(b-r);p(bf);p(dwf*2)
                    
                    
                


