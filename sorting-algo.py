
import random
import time


def mergeSort():
    listt = []

    print('List Type')
    while True:
        try:
            select = int(input('1. Random \n2. Almost Sorted \n3. Custom \n4. Reverse \n>>> '))
        except ValueError:
            print('I did not understand that :(\nPlease enter either 1, 2, 3 or 4')

        if select == 1:
            length = int(input('Length: '))
            for i in range(length):
                listt.append(i+1)
            print(listt)
            random.shuffle(listt)
            break

        elif select == 2:
            length = int(input('Length: '))
            for i in range(length):
                listt.append(i+1)
            listt[0], listt[1] = listt[1], listt[0]
            break

        elif select == 3:
            inp = None
            print('Please input your numbers\nPress \'s\' to stop')
            while True:
                inp = input('>>> ')
                if inp == 's':
                    break
                listt.append(inp)
                for i in range(len(listt)):
                    listt[i] = int(listt[i])
            print(listt)
            break

        elif select == 4:
            length = int(input('Length: '))
            for i in range(length):
                listt.append(i+1)
            listt.sort(reverse=True)           
            break
    
    start = time.perf_counter()
    mid = len(listt)//2
    left = listt[:mid]
    right = listt[mid:]
    print(left,right)


    for i in range(len(left)):
        if left[i] > left[i+1]:
            left[i], left[i+1] = left[i+1], listt[i]
        else: break

    a, b, c = 0, 0, 0
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            listt[c] = left[a]
            a += 1
        else:
            listt[c] = right[b]
            b += 1
        c += 1
    
    print(listt)










def quickSort():
    pass

def bubbleSort():
    listt = []

    print('List Type')
    while True:
        try:
            select = int(input('1. Random \n2. Almost Sorted \n3. Custom \n4. Reverse \n>>> '))
        except ValueError:
            print('I did not understand that :(\nPlease enter either 1, 2, 3 or 4')

        if select == 1:
            length = int(input('Length: '))
            for i in range(length):
                listt.append(i+1)
            print(listt)
            random.shuffle(listt)
            break

        elif select == 2:
            length = int(input('Length: '))
            for i in range(length):
                listt.append(i+1)
            listt[0], listt[1] = listt[1], listt[0]
            break

        elif select == 3:
            inp = None
            print('Please input your numbers\nPress \'s\' to stop')
            while True:
                inp = input('>>> ')
                if inp == 's':
                    break
                listt.append(inp)
                for i in range(len(listt)):
                    listt[i] = int(listt[i])
            print(listt)
            break

        elif select == 4:
            length = int(input('Length: '))
            for i in range(length):
                listt.append(i+1)
            listt.sort(reverse=True)           
            break
    
    start = time.perf_counter()
    n = len(listt)
    flag = True
    while n != 1 or (flag):
        flag = False
        for c in range(n-1):
            if listt[c] > listt[c+1]:
                listt[c], listt[c+1] = listt[c+1], listt[c]
        n -= 1
    end = time.perf_counter()

    print('COMPLETE: ' + str(listt))
    print('Time Taken: ' + str((end-start)) + 's')


def insertionSort():
    pass

def h2h():
    pass

def menu():
    print('Sorting Algorithm Race')
    while True:
        try:
            choice = int(input('1. Head-2-Head \n2. One Algorithm \n3. All Algorithms \n4. Exit \n>>> '))
        except ValueError:
            print('I did not understand that :( \nPlease enter either 1,2,3 or 4')
            continue
        if choice == 1:
            h2h()
            break
        
        elif choice == 2:
            print('Please choose which algorithm you would like to use')
            while True:
                try:
                    inp = int(input('1. Bubble \n2. Insertion \n3. Merge \n4. Quick \n>>> '))
                except ValueError:
                    print('I did not understand that :( \nPlease enter either 1,2,3 or 4')
            
                if inp == 1:
                    bubbleSort()
                    break
                elif inp == 2:
                    insertionSort()
                    break
                elif inp == 3:
                    mergeSort()
                    break
                elif inp == 4:
                    quickSort()
                    break
                else:
                    print('Please enter a number between 1 and 4')
            break


menu()

        