n = int(input())
h = []
a = []
for i in range(n):
    h.append(int(input()))
h += [h[0],h[1]]
for i in range(1,n+1):
    if h[i] > h[i+1] and h[i] > h[i-1]:
        if i >= n :
            a.append(i-n+1)
        else:a.append(i+1)
if len(a) == 0:
    print("ASS HOLE")
else:
    for i in sorted(a):
        print(i)