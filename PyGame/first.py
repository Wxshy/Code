import pygame
#initialize window
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption('Sam First')

x = 50
y = 50
w = 5
h = 5
vel = 5
colour = [(255,0,0),(0,255,0),(0,0,255)]
ci = 0
current = colour[ci]
def draw(current):
    pygame.draw.rect(win, current, (pos[0],pos[1],w,h))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(ci)
    if click[2] == 1:
        if ci == len(colour)-1:
            ci = 0
        ci += 1
        current = colour[ci]
    if click[0] == 1:
        draw(current)
        

    
    
        
        

    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= vel
    
    if keys[pygame.K_s]:
        y += vel

    if keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_d]:
        x += vel
    '''

        
    
    


pygame.quit()