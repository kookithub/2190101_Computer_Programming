cmd = input()
n = int(input())
if cmd == '90':
    km = []
    for i in range(n):
        x = input().strip()
        st = ''
        for z in x:
            st += (z + ' ')
        st = st.split()
        km.append(st)
    for i in range(len(km)-1):
        if len(km[i]) != len(km[i+1]):
            print("Invalid size")
            break
        else:
            for i in range(len(km[0])):
                z =[]
                for k in range(len(km)):
                    z.insert(0,km[k][i])
                print (''.join(z))
if cmd == '180':
    km = []
    for i in range(n):
        x = input().strip()
        st = ''
        for z in x:
            st += (z + ' ')
        st = st.split()
        km.append(st)
    for i in range(len(km)-1):
        if len(km[i]) != len(km[i+1]):
            print("Invalid size")
            break
        else:
            y = []
            for i in range(len(km[0])):
                z =[]
                for k in range(len(km)):
                    z.insert(0,km[k][i])
                y.append(z)
            for i in range(len(y[0])):
                z =[]
                for k in range(len(y)):
                    z.insert(0,y[k][i])
                print (''.join(z))
if cmd == 'flip':
    for i in range(n):
        x = input().strip()
        print(x[-1::-1])

        

    
        
    
            
        


