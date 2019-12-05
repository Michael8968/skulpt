#展示函数的好处，在不同的文件之间可以直接调用

import pygame
from pygame.locals import *
from random import randint
from L19_picture import sun,snow,bridge


pygame.init()  #初始化
screen = pygame.display.set_mode((800, 600)) #, FULLSCREEN) #设置屏幕大小

#加载马的图片
horse = []
for i in range(8):
    aa = pygame.image.load('lesson19/horse/' + str(i+1) + '.png')
    aa = pygame.transform.smoothscale(aa, (120,90))
    horse.append(aa)

num = 0
#加载背景
bac = pygame.image.load('lesson19/horse/' + 'bac.png')
bac = pygame.transform.smoothscale(bac, (800,600))



clock = pygame.time.Clock()
x = 700
snowy = 0
for i in range(10000):
    snowy += 2
    if snowy == 700:
        snowy = 0
    x -= 2
    if x == 0:
        x = 700

    screen.blit(bac, (0, 0))    #刷新背景
    screen.blit(horse[i%8], (x, 225)) #绘制马到屏幕上
    screen.blit(horse[i%8], (x+50, 240))
    #sun(screen)
    #bridge(screen)
    #snow(screen,700 -x)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    clock.tick(30)   #每秒30帧
    pygame.display.update()

pygame.quit()
