import random 
class Player():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.health=100
        
    def Heal(self):
        self.health+=10
        print("You have healed,you now have",self.health," health left")
        
    def HealthCheck(self):
        print(self.name,"you have",self.health," health left")

    def attack(self):
        enemy.health -= 10


class Enemy():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.health = 100
        self.evil = 100

    def heal(self):
        self.health += 10
        print('Enemy health:', self.health)

    def attack(self):
        p1.health -= 10

    


name = input('Name: ')
age = int(input('Age: '))
p1 = Player(name, age)

enemy = Enemy('Doris', 72)

run = True
while run:
    print(p1.name, 'you go first')
    while True:
        try:
            choice = int(input('1. Attack\n2. Heal\n3. Quit\n>>> '))
        except ValueError or choice > 3 or choice <= 0:
            print('Sorry i did not understand that. Try Again.')
        else: break

    if choice == 1:
        p1.attack()
        print(enemy.health)
    elif choice == 2:
        p1.Heal()
    elif choice == 3:
        exit()

    choice = random.randint(1,2)

    print('Enemy has chosen', choice)

    if choice == 1:
        enemy.attack()
        print(p1.health)
    elif choice == 2:
        enemy.heal()

            

    if enemy.health == 0:
        print(p1.name, 'you win!')
        exit()
