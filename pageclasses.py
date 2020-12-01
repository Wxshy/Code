'''
class page():
    def __init__(self, name, value, conTo):
        self.name = name
        self.value = value
        self.conTo = conTo


a = page('a', 1, ['c'])
b = page('a', 1, ['a'])

print(b.conTo[0].value)

'''

connections = {
    'c':'a',
    'a':'b',
    'abd':'c',
}

ivalues = {
    'a':1,
    'b':1,
    'c':1,
    'd':1
}


pages = ['a','b','c','d']

def calc(iv, con):
    return (iv * 0.85) / con

for item in connections:
    temp = []
    tempv = []
    print(connections[item])
    print(ivalues[connections[item]])
    if len(item) > 1:
        for i in range(len(item)):
            temp.append(item[i])
        for i in temp:
            print(calc(ivalues[i], len(temp)))
            tempv.append(calc(ivalues[i], len(temp)))
    else:
        for value in ivalues:
            counter = 0
            for i in range(len(connections)):
                if connections[item] in connections:
                    print('y')
            print(0.15 + (calc(ivalues[value], 1)))

    print(temp)
    print(sum(tempv))

        
