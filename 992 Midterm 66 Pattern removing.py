def remove_patterns(s): # 16 min
    s = s.split(',')
    z = s[0]
    for i in range(1,len(s)):
        for e in range(z.count(s[i])):
            z = z[:z.find(s[i])]+ z[z.find(s[i])+len(s[i]):]
    return z 
def check_coverage(s): # 1 hr 51 min
    s = s.split(',')
    z = s[0]
    q = z
    indice = []
    for i in range(1,len(s)):
        for e in range(z.count(s[i])):
            z = z[:z.find(s[i])]+ z[z.find(s[i])+len(s[i]):]
    for e in range(1,len(s)):
        if z in s[e]:
            z = ''
    if len(z) == 0:
        return ("Covered")
    else:
        for e in z:
            qq = q.find(e)
            if len(indice) != 0 and qq < min(indice):
                qq = q.find(e,min(indice))
            indice.append(qq)
        indices = []
        q = 1
        p = 0
        i = 1
        while q != len(indice)+1:
            if indice[p]+i in indice:
                q += 1
                i += 1
            else:
                indices.append(f"{indice[p]}-{indice[q-1]}")
                p = q
                q += 1
                i = 1
        return ','.join(indices)
print(check_coverage("ABCD1234,ABCDE,12345")) 
 
#print(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,GHIJKLMN,OPQRSTUV,WXYZ,0123456789"))
#print(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,EFGHIJKLMN,OPQRSTUV,WXYZ,0123456789"))
"""print(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,HIJKLMN,OPQRSTUV,WXYZ,0123456789"))
print(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFG,ABCDEF,GHIJKLMN,OPQRSTUV,WXYZ,23456789"))
print(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,GHIJKLMN,OPQRSTUV,WXYZ,0126789"))

print(check_coverage("abcdefghijklmnopqrstuvwxyz,abc,def,xyz,lmn,pqrs"))  
# Expected output: "Uncovered positions: 6-10 14 19-22"""
