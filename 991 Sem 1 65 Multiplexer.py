def f1(a,b,c):
    p = [a,b,c]
    z = ''
    if ((a or b or c > 0) and (a or b or c < 0) and (-1000 <= a or b or c) <= 1000):
        for e in range(3):
            if p[e] > 0:
                z += str(p[e]) + ' '
        return (min(z.split()))
def f2(a,b,c):
    p = [a,b,c]
    z = ''
    if ((a or b or c > 0) and (a or b or c < 0) and (-1000 <= a or b or c) <= 1000):
        for e in range(3):
            if p[e] < 0:
                z += str(p[e]) + ' '
        return (max([int (e) for e in z.split()]))
def f3(a,b,c):
    p = [a,b,c]
    if ((a or b or c > 0) and (a or b or c < 0) and (-1000 <= a or b or c) <= 1000):
        x = str(abs(sum(p)))
        return (x[0])
def f4(a,b,c):
    p = [a,b,c]
    if ((a or b or c > 0) and (a or b or c < 0) and (-1000 <= a or b or c) <= 1000):
        x = str(abs(sum(p)))
        return (x[-1])
def main():
    s1,s2,a,b,c = [int (e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a,b,c))
    elif s1 == 0 and s2 == 1:
        print(f2(a,b,c))
    elif s1 == 1 and s2 == 0:
        print(f3(a,b,c))
    elif s1 == 1 and s2 == 1:
        print(f4(a,b,c))
    else: print("Error")