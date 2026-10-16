n1 = input()
n2 = input()
f1 = open(n1,'r')
s1 = f1.read()
f1.close()
f2 = open(n2,'r')
s2 = f2.read()
f2.close()
ss = [s2]
for e in s1.lower().split():
    y = ''
    if ss[-1].lower().find(e) > 0:
        pos = ss[-1].lower().find(e)
        y += ss[-1][:pos]
        y += f"<{e}>" +ss[-1][pos:pos+len(e)] + '</>'
        y += ss[-1][pos+len(e):]
        ss.append(y)
print(ss[-1])
