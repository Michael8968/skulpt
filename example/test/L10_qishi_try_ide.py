import pygame
from pygame.locals import *

pygame.init() 


screen = pygame.display.set_mode((800, 600)) 

for i in range(1000):

    screen.fill((0, 0, 200))
    hero=pygame.image.load('lesson10/1.png')
    screen.blit(hero, (600, 300))



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            pass

	

    pygame.display.update()
