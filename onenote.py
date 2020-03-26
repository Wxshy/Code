def queue():
    choice = int(input('1. Add \n2. Pop \n3. Print'))

    queue = []
    if choice == 1:
        while True:
            inp = input('>>> ')
            if inp == '4':
                break
            queue.insert(0,inp)
            print(queue)

    if choice == 2:
        popc = input('Enter the item: ')
        del(queue[queue.index(popc)])
    
    elif choice == 3:            
        for i in range (len(queue)):
            print(queue[i])


def stack():
    stack = []
    while True
