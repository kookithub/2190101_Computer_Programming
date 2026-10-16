dt = {}
for i in range(int(input())):
    y = input().split()
    dt[y[0]] = [y[1],y[2]]
for i in range(int(input())):
    y = input().split()
    a = y[0]
    s = 0
    while True:
        if a in dt:
            b = dt[a]
        else:
            print("Route Not Found")
            break
        if y[0] == b[0]:
            print("Route Not Found")
            break
        s += int(b[1])
        if b[0] == y[1]:
            print(s)
            break
        a = b[0]