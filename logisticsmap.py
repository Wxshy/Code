from matplotlib import pyplot as plt 
import numpy as np

def equation(r, x):
    return r * x * (1 - x)

xlist = []
rlist = []

r = 2
for i in range(1000):
    r += 0.1
    if i == 0:
        a = equation(r,0.4)
    else:
        a = equation(r,a)
    
    if len(xlist) > 1 and a == xlist[-1]:
        break
    
    else:
        xlist.append(a)
        rlist.append(r)


print(len(xlist))

plt.plot(xlist)
plt.plot(rlist)
plt.show()
