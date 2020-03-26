
import random


# checking functions
def aceCheck(pCards):
    i = 0
    while i < 2:
        if 1 == pCards[i]:
            pCards.pop(i)
            pCards.append('Ace')
            if i == 0:
                pCards[0], pCards[1] = pCards[1], pCards[0]
                break
        i += 1

    if pCards[1] == 1:
        pCards.pop(1)
        pCards.append('Ace')


def bustCheck(dCards, pCards):
    dt = sum(dCards)
    pt = sum(pCards)
    if dt > 21:
        print('Dealer BUST')
        print('You Win')
        return True
    elif pt > 21:
        print('Player BUST')
        print('You Lose')
        return True


def Game():
    run = True
    while run == True:
        dCards = []
        pCards = []

        # deal cards
        dCards.append(random.randint(1, 11))
        dCards.append(random.randint(1, 11))
        pCards.append(random.randint(1, 10))
        pCards.append(random.randint(1, 10))

        print('Dealer\'s:', dCards[0])
        print('Your\'s:', pCards)

        if dCards == [11, 11]:
            dCards == [1, 11]



        pbj = False
        dbj = False

        # checks for blackjack
        if pCards == [1, 10] or pCards == [10, 1] or pCards == [1, 1]:
            pbj = True
        if dCards == [1, 10] or dCards == [10, 1] or dCards == [11, 10] or dCards == [10, 11] or dCards == [1,
                                                                                                            11] or dCards == [
            11, 1]:
            dbj = True

        if pbj and dbj:
            print('Double BlackJack')
            print('PUSH - Restart')
            Game()

        elif pbj and dbj == False:
            print('Player - BlackJack')
            print('You Win')
            break

        elif pbj == False and dbj:
            print('Dealer - BlackJack')
            print('You Lose')
            break

        # sets the players aces

        aceCheck(pCards)

        print('After')
        print(dCards)
        print(pCards)

        # asks if ace = 1 or 11
        if 'Ace' == pCards[0]:
            while True:
                try:
                    inp = int(input('Would you like your ace to be 1 or 11: '))
                except ValueError:
                    print('Please enter a number')
                else:
                    if inp == 1 or inp == 11: break

                    if inp != 1 or inp != 11:
                        print('Please enter either 1 or 11')
            i = 0
            while i < 2:
                if 'Ace' == pCards[i]:
                    pCards.pop(i)
                    pCards.append(inp)
                    if i == 0:
                        pCards[0], pCards[1] = pCards[1], pCards[0]
                        break
                i += 1

        if 'Ace' == pCards[1]:
            while True:
                try:
                    inp = int(input('Would you like your ace to be 1 or 11: '))
                except ValueError:
                    print('Please enter a number')
                else:
                    if inp == 1 or inp == 11: break

                    if inp != 1 or inp != 11:
                        print('Please enter either 1 or 11')
            i = 0
            while i < 2:
                if 'Ace' == pCards[i]:
                    pCards.pop(i)
                    pCards.append(inp)
                    if i == 0:
                        pCards[0], pCards[1] = pCards[1], pCards[0]
                        break
                i += 1

        pt = pCards[0] + pCards[1]
        print('Your Hand:', pCards)

        if pt > 21:
            print('BUST')
            print('Better luck next time')
            break
        def action():
            while True:
                try:
                    choice = int(input('1. Hit \n2. Stand \n3. Split \n'))
                except ValueError:
                    print('Please enter a number')
                else:
                    if 0 < choice < 4:
                        break
                    else:
                        print('PLease enter either 1, 2 or 3')
            return choice
        yes = True
        while yes:
            choice = action()
            # actions
            if choice == 1:
                pCards.append(random.randint(1, 10))
                print(pCards)

            elif choice == 2:
                yes = False

            else:
                if len(set(pCards)) == 1:
                    splitcards = []
                    for i in range(len(pCards)):
                        splitcards.append([pCards[i]])
                    print(splitcards)

                else:
                    print('no')
        print('Dealer\'s Hand:', dCards)
        print('Player\'s Hand:', pCards)
        pt = sum(pCards)
        dt = sum(dCards)
        if dt < pt < 21:
            print('You Win')





Game()
