while True:
    try: item = int(input('Enter a number you would like to find'))
    except: ValueError: print('I did not understand that, try again')
    else: break
listt = [1,2,3,4,5,6,7,8,9,10]
listlength = len(listt)
lowerb = 0
upperb = listlength - 1
found = False
while found == False and lowerb <= upperb:
    midpoint = int(lowerb + (upperb - lowerb)/2)
    if listt[midpoint] == item:
        found = True
    elif listt[midpoint] < item:
        lowerb = midpoint + 1
    else:
        upperb = midpoint - 1
if found: print('item found at position', midpoint)
