def t2m(text,pattern):
    morse = ''
    for e in text :
        j = pattern.find('[' + e + ']')
        if j != -1:
            j += 3	
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
        else:
            return ('Invalid : ' + text)
    return morse.strip()
def m2t(m,p):
    y = ''
    for e in m.split() :
        j = p.find(']'+ e +'[')
        if j != -1:
            y += p[j-1:j] + ' '
        else:
            return ('Invalid : ' + m)
    return y
n = 'morse'
fn = open(n,'r')
cm = fn.readline().strip()
if cm == 'T2M':
    p = fn.readline().strip()
    for line in fn.readlines():
        print(t2m(line.strip(),p))
elif cm == 'M2T':
    p = fn.readline().strip()
    for line in fn.readlines():
        print(m2t(line.strip(),p))
else:
    print("Invalid code")