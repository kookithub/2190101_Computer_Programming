n = input()
aj = input()
f1 = open(n,'r')
f = 0
m = 0
sec = []
for line in f1:
    x = line.strip('\n').split(',')
    if x[4] == aj:
        if x[1] == 'F':
            f += 1
        else: m += 1
        if x[3] not in sec:
            sec.append(x[3])
if len(sec) == 0:
    print("Not found")
elif len(sec) == 1:
    print(f"Section: {sec[0]} --> F = {f}, M = {m}")
else: print(f"Sections: {','.join(sec)} --> F = {f}, M = {m}")

    

        
