import pygame
import pygameMenu

pygame.init()

win = pygame.display.set_mode((800,600))


run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    


pygame.quit()