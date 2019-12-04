import pygame
from pygame.locals import *

pygame.init()  #初始化
screen = pygame.display.set_mode((800, 600)) #, FULLSCREEN) #设置屏幕大小
clock = pygame.time.Clock()



#加载马的图片
horse = []
for i in range(8):
    aa = pygame.image.load('lesson11/homework/'+str(i+1) + '.png')
    horse.append(aa)


#加载背景
bac = []
for i in range(7):
    aa = pygame.image.load('lesson11/homework/bac' + str(i+1) + '.png')
    bac.append(aa)


x = 700
num = 0
flag=0

for i in range(10000):
    x -= 5
    if flag <= 30:
        flag += 1
    else:
        flag = 0
        num += 1
    if num == 7:
        num = 0
    clock.tick(30)   #每秒30帧
    screen.blit(bac[num], (0, 0))    #刷新背景
    screen.blit(horse[i%8], (x, 230)) #绘制马到屏幕上



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()

pygame.quit()
