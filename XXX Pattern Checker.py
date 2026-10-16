pattern = input()
string = input()
p = 0
c = 0
if string.find(pattern,0) != -1:
    c += 1
    p = string.find(pattern,0)
    while p != -1:
        p = string.find(pattern,p+int(len(pattern)))
        if p != -1:
            c += 1
print(c)
print(string.count(pattern))