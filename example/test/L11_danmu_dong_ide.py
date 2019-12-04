import pygame
from pygame.locals import *
import random
import time


pygame.init()
bac = pygame.image.load('lesson11/bac1.png')
screen = pygame.display.set_mode((800, 600)) 
dd=0
bac = []

font = pygame.font.Font('simhei.ttf', 40)
str1 = '666社会社会大吉大利今晚吃鸡嘤嘤嘤'
str2=font.render(str1, True, (200,200,0))
print(type(str2))

for i in range(7):
    aa = pygame.image.load('lesson11/bac' + str(i+1) + '.png')
    bac.append(aa)

num = 0
flag=0
nn=1

for i in range(10000):
    time.sleep(0.03)
    if flag <= 60:
        flag += 1
    else:
        flag = 0
        num += 1
    if num == 7:
        num = 0
    screen.blit(bac[num], (0,0)) 
    screen.blit(str2, (800-dd, 300))
    dd+=1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()       
   
    pygame.display.update()


