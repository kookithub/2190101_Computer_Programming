x = input()
y = input()
d = {}
b = {}
for e in x.lower():
    if e not in d and e.isalpha():
        fs = x.lower().count(e)
        ss = y.lower().count(e)
        if fs - ss > 0:
            d[e] = fs-ss
for e in y.lower():
    if e not in b and e.isalpha():
        fs = y.lower().count(e)
        ss = x.lower().count(e)
        if fs - ss > 0:
            b[e] = fs-ss  

print(x)
if len(d) == 0:
    print("- None")
else:
    for i in d:
        if d[i] > 1:
            print(f"- remove {d[i]} {i}'s")
        else:
            print(f"- remove {d[i]} {i}")
print(y)
if len(b) == 0:
    print("- None")
else:
    for i in b:
        if b[i] > 1:
            print(f"- remove {b[i]} {i}'s")
        else:
            print(f"- remove {b[i]} {i}")
            