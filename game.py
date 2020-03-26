import pygame

pygame.init()


win = pygame.display.set_mode((800,600))
bg = pygame.image.load('C:/Users/samue/Pictures/background.png')
sship = pygame.image.load('C:/Users/samue/Pictures/spaceship.png')
ast = pygame.image.load('C:/Users/samue/Pictures/asteroid.png')
sship = pygame.transform.scale(sship,(75,75))
ast = pygame.transform.scale(ast, (75, 75))
pygame.mouse.set_visible(0)

class player(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 5 
        self.hitbox = (self.x + 20, self.y + 20, 80, 60)

    def draw(self, win):
        self.hitbox = (self.x, self.y, 80, 60)
        win.blit(sship, (self.x, self.y))
        pygame.draw.rect(win, (255,0,0),self.hitbox, 2)


class projectile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, win):
        pygame.draw.circle(win, (255,0,0), (self.x, self.y), 5)

class enemy(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = 5
        self.hitbox = (self.x, self.y +10, 75, 55)

    def draw(self, win):
        self.move()
        self.hitbox = (self.x, self.y +10, 75, 55)
        win.blit(ast, (self.x, self.y))
        pygame.draw.rect(win, (255,0,0),self.hitbox, 2)


    def move(self):
        if self.x == 800 - self.radius or self.x == 0:
            self.vel = self.vel * -1
        
        self.x += self.vel

    def hit(self):
        print('HIT')
        



def redraw(ops):
    win.blit(bg, (0,0))
    player.draw(man, win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()
    
bullets = []
run = True
man = player(325,225, 75, 75)
rx = 50
ry = 50
score = -1
ops = []
while run:
    
    pygame.time.delay(10)
    mx, my = pygame.mouse.get_pos()
    man.x = mx
    man.y = my
    click = pygame.mouse.get_pressed()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and man.x < 700:
        man.x -= man.vel
    
    elif keys[pygame.K_d] and man.x < 625:
        man.x += man.vel

    
    

    for bullet in bullets:
        if bullet.y - 5 < rock.hitbox[1] + rock.hitbox[3] and bullet.y + 5 > rock.hitbox[1]:
            if bullet.x + 5 > rock.hitbox[0] and bullet.x - 5 < rock.hitbox[0] + rock.hitbox[3]:
                rock.hit()
                score += 1
                bullets.remove(bullet)
                print('Score:',score)
                print(len(ops))

        
        if bullet.y > 0:
            bullet.y -= 5
        if bullet.y < 1:
            bullets.remove(bullet)

    if click[0]:
        clicked = True
    else: 
        clicked = False

    if clicked:
        if len(bullets) < 50:
            bullets.append(projectile(mx+37, my+10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redraw(ops)


pygame.quit()