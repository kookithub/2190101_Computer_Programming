def is_odd(n):
    return n%2 != 0
def has_odds(x):
    for e in x:
        if is_odd(e):
            return True
            break
    return False
def all_odds(x):
    c = 0
    for e in x:
        if is_odd(e):
            c += 1
    return c == len(x)
def no_odds(x):
    for e in x:
        if is_odd(e):
            return False
            break
    return True
def get_odds(x):
    return [(e) for e in x if e%2 != 0]
def zip_odds(a, b):
    a = get_odds(a)
    b = get_odds(b)
    c = []
    for i in range(len(a)+len(b)):
        if i < len(a):
            c.append(a[i])
        if i < len(b):
            c.append(b[i])
    return c
exec(input())