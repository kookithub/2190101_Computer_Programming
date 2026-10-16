import math
i = input().split()
if len(i) != 2:
    print("Error!")
else:
    v = float(i[0])
    angr = float(i[1])
    theta = math.radians(angr)
    g = 9.81
    hmax = ((v**2)*((math.sin(theta))**2))/(2*g)
    r = ((v**2)*(math.sin(2*theta)))/(g)
    t = (2*v*math.sin(theta))/g
    rhmax = abs(round(hmax,2))
    rr = abs(round(r,2))
    rt = abs(round(t,2))
    if len(str(rhmax)) < 4:
        rhmax = f"{str(rhmax)}{0}"
    if len(str(rr)) < 4:
        rr = f"{str(rr)}{0}"
    if len(str(rt)) < 4:
        rt = f"{str(rt)}{0}"
    print(f"{rhmax} {rr} {rt}")