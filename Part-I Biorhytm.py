import math
bd,bm,by,d,m,y = [int(e) for e in input().split()]
by -= 543
y -= 543
diy = 365
n = [int (e) for e in [31,28,31,30,31,30,31,31,30,31,30,31]]
if (by%4 == 0 and by%100 != 0) or by%400 == 0:
    diy = 366
    n[1] = 29
doy = sum(n[:bm-1])+ bd
fp = diy - doy
n[1] = 28
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
    n[1] = 29
lp = sum(n[:m-1]) + d
doyib = (y-by-1)*365 +((y-by-1)//4)
t = fp + doyib + lp
phy = round(math.sin(2*math.pi*t/23),2)
emo = round(math.sin(2*math.pi*t/28),2)
intel = round(math.sin(2*math.pi*t/33),2)
print (t,phy,emo,intel)