n = int(input())
for x in range(n):
    c = input().strip("|").split("|")
    cn = [c[0][0],c[1][0],c[2][0],c[3][0],c[4][0]]
    cs = [c[0][1],c[1][1],c[2][1],c[3][1],c[4][1]]
    for n in range(len(cn)):
        if cn[n] == "A" and n == 0:
            cn[n] = 14
        if cn[n] == "A" and n != 0:
            cn[n] = 1
        if cn[n] == "K":
            cn[n] = 13
        if cn[n] == "Q":
            cn[n] = 12
        if cn[n] == "J":
            cn[n] = 11
        if cn[n] == "X":
            cn[n] = 10
    cnn = [int (e) for e in cn]
    if (cs[0]== cs[1]==cs[2]==cs[3]==cs[4]) and (cnn[0] == cnn[1]+1 == cnn[2]+2 == cnn[3]+3 == cnn[4]+4) and sum(cnn) == 60:
        print("Royal Straight Flush")
    elif (cs[0]== cs[1]==cs[2]==cs[3]==cs[4]) and (cnn[0] == cnn[1]+1 == cnn[2]+2 == cnn[3]+3 == cnn[4]+4):
        print("Straight Flush")
    elif (cs[0]== cs[1]==cs[2]==cs[3]==cs[4]):
        print("Flush")
    elif (cnn[0] == cnn[1]+1 == cnn[2]+2 == cnn[3]+3 == cnn[4]+4):
        print("Straight")
    else:
        print("None")
        
    