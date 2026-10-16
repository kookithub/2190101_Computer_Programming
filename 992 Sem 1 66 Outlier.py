x = sorted([int (e) for e in input().split()])
ax = len(x)
i = int
if ax%2 == 0:
    lq1 = x[:i(ax/2)]
    lq3 = x[i(ax/2):]
else:
    lq1 = x[:i(ax/2-0.5)]
    lq3 = x[i(ax/2-0.5)+1:]
if len(lq1)%2 != 0:
    q1 = lq1[i((len(lq1)-1)/2)]
    q3 = lq3[i((len(lq1)-1)/2)]
else:
    q1 = ((lq1[i(len(lq1)/2-1)]) + (lq1[i(len(lq1)/2)]))/2
    q3 = ((lq3[i(len(lq1)/2-1)]) + (lq3[i(len(lq1)/2)]))/2
L = q1-(1.5*(q3-q1))
U = q3+(1.5*(q3-q1))
print(f"L = {L} U = {U}")
z = []
for e in lq1:
    if e < L:
        z.append(str(e))
for e in lq3:
    if e > U:
        z.append(str(e))
if len(z) == 0:
    print("Not Found")
else: print(' '.join(z))
#40 min     

    