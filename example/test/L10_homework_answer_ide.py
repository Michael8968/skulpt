import pygame
from pygame.locals import *
from random import randint


pygame.init()  #初始化
screen = pygame.display.set_mode((800, 600)) #, FULLSCREEN) #设置屏幕大小

#加载机器人的图片
monster = []
for i in range(4):
    aa = pygame.image.load('lesson10/homework/'+str(i+1) + '.png')
    monster.append(aa)

#加载背景
bac = pygame.image.load('lesson10/homework/bac.png')



clock = pygame.time.Clock()
x = 700

for i in range(10000):
    x -= 3
    clock.tick(15)   #每秒15帧
    screen.blit(bac, (0, 0))    #刷新背景
    screen.blit(monster[i%4], (x, 200)) #绘制机器人到屏幕上

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()

pygame.quit()
