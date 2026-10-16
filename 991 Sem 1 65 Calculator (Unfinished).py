#This code is not working and it is wrong , just make a new one instead
st = input()
stp = st.split("-")
summer = 0

if stp[0] == '':
    z = stp.pop(0)
    if stp[0].isdigit():
        summer = int('-'+stp[0])
        z = stp.pop(0)
    else:
        v = stp[0].split('+')
        summer = int('-'+v[0])
        stp[0] = stp[0][len(v[0])+1:]
elif (st[0]) == '-':
    summer = int('-'+stp[0])
    z = stp.pop(0)
elif stp[0].isdigit():
    summer = int(stp[0])
    z = stp.pop(0)
for i in range (len(stp)):
    if stp[i].isdigit():
        summer -= int(stp[i])
    else:
        y = [int (e) for e in stp[i].split('+')]
        
        summer -= int(y[0])
        yy = y.pop(0)
        summer += sum(y)
print(summer)

"""
for i in range(len(stp)-1):
    if not stp[i+1].isdigit():
        x = stp[i+1]
        z = [int (e) for e in x.split("+")]
        y = stp.pop(i+1)
        summer += sum(z)
for i in range(len(stp)-1):
    summer -= int(stp[i+1])
print(summer)
"""