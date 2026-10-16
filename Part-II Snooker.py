sc ={'R':1, 'Y':2,'G':3, 'W':4, 'B':5, 'P':6, 'K':7, 'X':0,'1':0,'2':0}
x = input()
p1 = 0
p2 = 0
while x[1] != 'K':
    s = 0
    for i in x:
        s += sc[i]
    if x[0] == '1':
        p1 += s
    else:
        p2 += s
    x = input()
if x[0] == '1':
    p1 += 7
else:
    p2 += 7
print(p1,p2)
if p1 > p2:
    print("Player 1 wins")
elif p2 > p1:
    print("Player 2 wins")
else: print("Tie")