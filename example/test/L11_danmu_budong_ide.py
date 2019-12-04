import pygame
from pygame.locals import *
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600)) 

font = pygame.font.SysFont('Arial', 30)
str1 = '666社会社会大吉大利今晚吃鸡嘤嘤嘤'
str2=font.render(str1, True, (200,200,0))
print(type(str2))
bac = pygame.image.load('lesson11/bac1.png')
dd=0

for i in range(5000):
    time.sleep(0.03)
    screen.blit(bac, (0, 0))
    screen.blit(str2, (800-dd, 300))
    dd+=2    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()       
   
    pygame.display.update()
