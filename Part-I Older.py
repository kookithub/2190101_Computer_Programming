f = input().split()
s = input().split()
mon = ["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in range(12):
    if f[1] == mon[i]:
        f[1] = i+1
    if s[1] == mon[i]:
        s[1] = i+1
f[2] = f[2][:len(f[2])-1]
s[2] = s[2][:len(s[2])-1]
ff = [int (e) for e in [f[3],f[1],f[2]]]
ss = [int (e) for e in [s[3],s[1],s[2]]]
if ff < ss:
    print(f[0])
elif ff == ss:
    print(f[0]+' '+s[0])
else: print(s[0])

""" USELESS AS FUCK VERY INEFFICIENT
if int(f[-1]) < int(s[-1]):
    print(f[0])
elif int(f[-1]) == int(s[-1]):
    if int(f[1]) < int(s[1]):
        print(f[0])
    elif int(f[1]) == int(s[1]):
        if int(f[2]) < int(s[2]):
            print(f[0])
        elif int(f[2]) == int(s[2]):
            print(f[0]+' '+s[0])
        else:print(s[0])       
    else:print(s[0]) 
else: print(s[0])
"""   