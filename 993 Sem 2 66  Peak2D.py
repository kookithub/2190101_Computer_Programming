def read_data():
    dat = []
    R = int(input())
    for r in range(R):
        dat.append([int(e) for e in input().strip().split()])
    return dat
def count_peak(data):
    c = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            k = data[i][j]
            u = k > data[i-1][j]
            d = k > data[i+1][j]
            l = k > data[i][j-1]
            r = k > data[i][j+1]
            if u and d and l and r:
                c += 1
    return c
exec(input().strip())