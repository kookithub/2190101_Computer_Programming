x = input().split()
y = input().split()
if (x[2] != "A" or x[3] > "C" or x[4] > "C") and (y[2] != "A" or y[3] > "C" or y[4] > "C"):
    print ("None")
elif (x[2] != "A" or x[3] > "C" or x[4] > "C"):
    print (y[0])
elif (y[2] != "A" or y[3] > "C" or y[4] > "C"):
    print (x[0])
elif x[1:] == y[1:]:
    print ("Both")    
elif x[1] > y[1]:
    print(x[0])
elif x[1] == y[1]:
    if x[2:] < y[2:]:
        print(x[0])
    else:
        print(y[0])
else:
    print(y[0])  