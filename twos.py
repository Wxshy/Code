num = int(input('Enter a negative number -'))

binary = bin(num)
print(num, binary)

binary = list(binary)
print(binary)
binary.pop(0)
binary.pop(0)
print(binary)
inverted = []
for i in binary:
    if binary[int(i)] == '0':
        inverted.append(0)
    else:
        inverted.append(1)

last = len(inverted) - 1
print(inverted[last])
print(inverted)

if inverted[last] == 0:
    inverted.pop(last)
    print(inverted)
    inverted.insert(last, 1)
    print(inverted)

    
else:
    listt = inverted.sort(reverse=True)
    print(listt)

        

print(inverted)
