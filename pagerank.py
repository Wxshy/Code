import matplotlib.pyplot as plt
ia = 1
ib = 1
ic = 1
idd =1

ta = 2
tb = 1
tc = 1
td = 1

x = []

ap = [1]
bp = [1]
cp = [1]
dp = [1]

def calc(iv, con):
    return (iv * 0.85) / con

for i in range(100):
    x.append(i)
    av = []
    bv = []
    cv = []
    dv = []

    av.append(calc(ic, tc))
    
    bv.append(calc(ia, ta))

    cv.append(calc(ia, ta))
    cv.append(calc(ib, tb))
    cv.append(calc(idd, td))
    
    ia = sum(av) + 0.15
    ib = sum(bv) + 0.15
    ic = sum(cv) + 0.15
    idd = sum(dv) + 0.15

    ap.append(ia)
    bp.append(ib)
    cp.append(ic)
    dp.append(idd)

print(ia,ib,ic,idd)

plt.plot(ap)
plt.plot(bp)
plt.plot(cp)
plt.plot(dp)

plt.show()

    



    

