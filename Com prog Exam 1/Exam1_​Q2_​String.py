x = input().split()
for i in range(4):
    x[i] = x[i].lower()
    x[i] = x[i][-1::-1]
    x[i] = x[i].capitalize()
z = ' '.join(x)
print (z)