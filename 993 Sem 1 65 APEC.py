al = []
en = {}

y = input().split()
while y[0] != 'End':
    if y[0] == "Ally":
        al.append(y[1:])
    if y[0] == "Enemy":
        if y[1] not in en:
            en[y[1]] = [y[2]]
        else:
            en[y[1]].append(y[2])
        if y[2] not in en:
            en[y[2]] = [y[1]]
        else:
            en[y[2]].append(y[1])
    if y[0] == "Table":
        country = y[1:]
        s = True
        for i in range(len(country)):
            if country[i] in en and country[i-1] in en[country[i]]:
                print("No")
                s = False
                break
            else:
                for k in al:
                    if country[i] in k and s:
                        for a in k:
                            if (a in en and country[i-1] in en[a]):
                                print("No")
                                s = False
                                break
                    if country[i-1] in k and s:
                        for a in k:
                            if country[i] in en and a in en[country[i]]:
                                print("No")
                                s = False
                                break
        if s:
            print("Okay")                                    
    y = input().split()

                    
                    