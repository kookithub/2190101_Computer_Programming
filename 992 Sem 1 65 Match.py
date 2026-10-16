def match(word,pat,inc,exc):
    p = 0
    c = 0
    q = 0
    incl = []
    if len(word) == len(pat):
        p += 1
    for e in range(len(pat)):
        if pat[e] == '?' and len(word) == len(pat):
            c += 1
            incl.append(word[e])
        elif len(word) == len(pat) and pat[e] == word[e]:
            c += 1
        else: break
    if c == len(word):
        p += 1
    for i in incl:
        if i in exc:
            q += 1
    if q == 0:
        p += 1
    for e in inc:
        if e in incl:
            incl.remove(e)
        else:
            p = 0
    print( p == 3 )
exec(input())
#match("MACMA","M?C??","MAA","")
#30 min        