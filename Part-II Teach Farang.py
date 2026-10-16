d = {0:'soon',
    1:'neung',
    2:'song',
    3:'sam',
    4:'si',
    5:'ha',
    6:'hok',
    7:'chet',
    8:'paet',
    9:'kao',
    10:'sip',
    991:'et',
    20:'yi',
    100:'roi',
    1000:'pun',
}

def to_Thai( N ):
    n = str(N)
    out = ""
    if N < 11:
        return d[N]   
    if N >= 1000: 
        out += d[int(n[-4])] + ' pun '
        N %= 1000
    if N >= 100: 
        out += d[int(n[-3])] + ' roi ' 
        N %= 100
    if N >= 10:
        if N > 29:
            out += d[int(n[-2])]
        elif N > 19:
            out += 'yi'
        out += ' sip '
        N %= 10
    if N == 1:
        out += 'et'
    if N > 1:
        out += d[N]
    return out