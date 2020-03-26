inp = input('Enter a message to hash: ')
listv = list(inp)
hashp1 = []
for i in range(len(listv)):
    print(listv[i], ord(listv[i]))
    ascv = ord(listv[i])
    if i == len(listv)-1: res = (ascv) ** (ord(listv[0]))
    else: res = (ascv) ** (ord(listv[i+1]))
    print(res)
    hashp1.append(res)
print('length hp1', len(hashp1))
lengthChr = int(256 / len(hashp1))
hashp2 = []
str1 = ''
print('len', lengthChr)
for i in range(len(hashp1)):
    print(i)
    temporary = list(str(hashp1[i]))
    print('tempor', temporary)
    temp = temporary[:lengthChr]
    print('temp', temp)
    temp = str1.join(temp)
    print(temp)
    hashp2.append(temp)



hashp3 = []
str2 = ''
for i in range(len(hashp2)):
    dec = int(hashp2[i])
    hexa = hex(dec).replace('0x','')
    print('hex', i)
    print(hexa)
    hashp3.append(hexa)
    hashed = str2.join(hashp3)

print(hashed)

leftOver = 256 - len(hashed)
print(leftOver)

rem = ''
while leftOver > 0:
    for i in range(len(listv)):
        leftOver = 256 - len(hashed)
        if i == len(listv)-1: res = (ord(listv[0])) ** (ascv)
        else: res = ord(listv[i+1]) ** ascv
        print(res)
        rem = rem.join(str(res))
        print(rem)
        leftOver = 0
    
    
        

        
    

