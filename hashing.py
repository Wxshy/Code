import time
inp = input('Enter: ')
part1 = []

for i in range(len(inp)):
    ascv = ord(inp[i].upper())
    part1.append(ascv)

string = ''

for i in range(len(part1)):
    string += str(part1[i])


string = string.replace('0','')

 

length = 0
value = []
i = 0
string = string * 1000000




 
while length < 100:
    hashV = ord(inp[0])
    hashV = hashV ** int(string[i])
    i += int(string[i])
    hashV = hashV ** (1/int(string[i]))
    i += int(string[i])
    value.append(hashV)
    length = len(value)
 

 
 


dec = ''

for i in range(len(value)):
    dec += str(value[i])

   

dec = dec.replace('.','')


 

hexed = hex(int(dec)).replace('0x','')
finalLength = 0
i = 0
final = []


hexedfinal = hexed[:256]


print(hexedfinal)
'''
while finalLength < 256:
    final.append(hexed[i])
    hexed.pop(hexed[i])
    if finalLength > 240:i = 0
    i += hexed[i]
    
    
    
'''
time.sleep(100000)

