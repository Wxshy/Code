import random
class Account():
    def __init__(self, fname, sname, number, balance):
        self.__fname = fname
        self.__sname = sname
        self.__number = number
        self.__balance = balance

    def cbalance(self):
        print('Balance: ¥', acc.__balance)

    def deposit(self):
        amount = int(input('DEPOSIT AMOUNT: ¥'))
        self.__balance = str(int(self.__balance) + amount)
        print('Balance: ¥', acc.__balance)

    def withdraw(self):
        amount = int(input('WITHDRAW AMOUNT: ¥'))
        self.__balance -= amount
        print('Balance: ¥', acc.__balance)





def menuP():
    while True:
        try:
            menu = int(input('--WASH BUILDING SOCIETY-- \n1. Create Account \n2. Access account \n3. Quit \n>>> '))
        except ValueError or choice > 3 or choice <=0:
            print('I did not understand that please enter 1,2 or 3')
        else: 
            break

    return menu
    


while True:
    menu = menuP()
    if menu == 1:
        name1 = input('First Name: ')
        name2 = input('Last Name: ')
        anum = random.randint(1000,9999)
        acc = Account(name1, name2, anum, '0')
        print(('Here are your account details: \nFirstname: {} \nLastname: {} \nAccount Number: {}').format(name1, name2, anum))
        f = open('C:/Users/samue/Documents/Code/bd.txt', 'w')
        f.write(name1 + ' ' + name2 + ' ' + str(anum) + ' ' + '0' + '\n')
        f.close()
        print('ACCOUNT CREATED')
        

    if menu == 2:
        valid = False
        f = open('C:/Users/samue/Documents/Code/bd.txt', 'r')

        while True:
            f = open('C:/Users/samue/Documents/Code/bd.txt', 'r')
            print('--LOGIN--')
            ln = input('LastName: ')
            an = input('Account Number: ')
            for lines in f.readlines():
                lines = lines.split()
                if ln == lines[1] and an == lines[2]:
                    print('VALID')
                    valid = True
                    while True:
                        try:
                            choice = int(input('--WASH BUILDING SOCIETY-- \n1. Check Balance \n2. Deposit \n3. Withdraw \n4. Quit \n>>> '))
                        except ValueError or choice > 4 or choice <=0:
                            print('I did not understand that please enter 1,2 or 3')
                        else: 
                            break
                    acc = Account(lines[0], lines[1], lines[2], lines[3])
                    if choice == 1:
                        acc.cbalance()

                    elif choice == 2:
                        acc.deposit()

                    elif choice == 3:
                        acc.withdraw
                    else:
                        exit()
                    f.close()
                else:
                    print('PLease enter the correct details')
        

    if menu == 3:
        exit()


    