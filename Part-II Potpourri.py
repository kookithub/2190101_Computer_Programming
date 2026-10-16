def convex_polygon_area(p):
    a = [i[0] for i in p] + [p[0][0]]
    b = [i[1] for i in p] + [p[0][1]]
    va,vb = 0,0
    for i in range(int(len(a)-1)):
        va += a[i]*b[i+1]
    for i in range(int(len(b)-1)):
        vb += b[i]*a[i+1]
    return abs((va-vb)/2)
def is_heterogram(s):
    for i in s.lower():
        if s.count(i) > 1 and s.isalpha():
            return False
            break
    return True
def replace_ignorecase(string, pattern, b):
    y = ''
    p = string.lower().find(pattern.lower(),0)
    q = 0
    while p != -1:
        y += string[:p] + b + string[p+len(pattern):]
        string = y
        y = ''
        q = p
        p = string.lower().find(pattern.lower(),p+len(pattern)+(len(pattern)-len(string[q:p])))
    return string
def top3(votes):
    v = sorted([[-votes[e],e] for e in votes])
    a = []
    for i in range(3):
        a.append(v[i][1])
    return a
s = "i am skibidi as fuck"
print(s.replace("fuck","skibidi"))
print(replace_ignorecase("i am skibidi as fuck","fuck","skibidi"))