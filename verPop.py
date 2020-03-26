import matplotlib.pyplot as plt

def equation(x, r):
    ans = []
    for i in range(100):
        if len(ans) == 0:
            ans.append(r * x * (1 - x))
        else:
            x = ans[(len(ans)-1)]
            ans.append(r * x * (1 - x))
    return ans

x = []
for i in range(100):
    x.append(i)

y = equation(0.4, 1.3)


plt.plot(x,y)
plt.show()