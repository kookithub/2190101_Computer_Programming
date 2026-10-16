def show(d):
    for e in d:
        print(e)
def search(m, keyword, power):
    d = []
    for n in range(5):
        y = ''
        for p in (range(3)) :
            y += str(m[n][p]) + ' '
        y = y.split()
        y += '-'
        if (keyword in y and power in y):
            d.append(m[n])
    return d

m1 = ["green giant", "sacrifice a monster: draw a card", 5]
m2 = ["blue giant", "tap: draw a card, then discard a card" , 3]
m3 = ["blue drake", "discard a card: return to hand", 1]
m4 = ["green drake", "sacrifice a land: destroy target giant", 3]
m5 = ["black wurm", "sacrifice a permanent: destroy target permanent", 3]
m = [m1,m2,m3,m4,m5]
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
exec(input())