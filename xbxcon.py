import pygame

pygame.init()
win = pygame.display.set_mode((800,700))

joystick = []

run = True

for i in range(0, pygame.joystick.get_count()):
    joystick.append(pygame.joystick.Joystick(i))
    joystick[-1].init()
    print ("Detected joystick ",joystick[-1].get_name(),"'")


class Player(object):
    def __init__(self, x, y, vel, w , h):
        self.x = x
        self.y = y
        self.vel = vel
        self.w = w
        self.h = h

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x,self.y,self.w,self.h))
        pygame.display.update()

def redraw():
    p1.draw(win)
    win.fill((0,0,0))

p1 = Player(50,50,5,100,100)
while run:
    for e in pygame.event.get():
        if e.type == pygame.JOYAXISMOTION:
            print(e)
            p1.x += p1.vel * e.value
        if e.type == pygame.QUIT:
            run = False

    jc = pygame.joystick.get_count()

    for i in range(jc):
        pass


    redraw()


pygame.quit()
    
