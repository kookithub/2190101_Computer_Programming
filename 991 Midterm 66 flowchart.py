def f1(l,x):
        j = 0
        maxindex = 0
        minindex = 0
        while j != len(l):
            if l[j]*x < (l[minindex])*x:
                minindex = j
            if (l[j])*x > (l[maxindex])*x:
                maxindex = j
            j += 1
        a = l[minindex]
        b = l[maxindex]
        print(a,b)