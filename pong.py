import pygame

pygame.init()

win = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Pong')

class player(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 5
        self.hitboxt = (self.x, self.y, 25, 37)
        self.hitboxb = (self.x, self.y + 60, 25, 37)

    def draw(self, win):
        self.hitboxt = (self.x, self.y, 25, 37)
        self.hitboxb = (self.x, self.y + 63, 25, 37)
        pygame.draw.rect(win, (255,255,255),(self.x, self.y, self.w, self.h))
        pygame.draw.rect(win, (255,0,0), self.hitboxt, 2)
        pygame.draw.rect(win, (255,0,0), self.hitboxb, 2)


class ballClass(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.hitbox = (self.x, self.y, 25, 25)
        self.mUp = False
        self.mDown = False
        self.mR = False
        self.mL = False

    def draw(self, win):
        self.move()
        self.hitbox = (self.x, self.y, 25, 25)
        pygame.draw.rect(win, (255,255,255),(self.x, self.y, 25,25))
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.x > 975:
            self.mR = False
            self.mL = True
        elif self.x < 0:
            self.mR = True
            self.mL = False
        if self.y < 1:
            self.mUp = False
            self.mDown = True
        elif self.y > 775:
            self.mUp = True
            self.mDown = False
        print(self.mUp, self.mDown, self.y)

        if self.mR:
            self.x += self.vel[0]
        if self.mL:
            self.x -= self.vel[0]
        if self.mUp:
            self.y -= self.vel[1]
        if self.mDown:
            self.y += self.vel[1]

def redraw():
    win.fill((0,0,0))
    p1.draw(win)
    ball.draw(win)
    pygame.display.update()
    



p1 = player(940, 10, 25, 100)
ball = ballClass(475, 375, [8,8])
ball.mR = True
run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if p1.y > 0:
            p1.y -= p1.vel

    if keys[pygame.K_DOWN]:
        if p1.y < 700:
            p1.y += p1.vel

    redraw()


pygame.quit()
