import pygame
from pygame.locals import *
from random import randint


pygame.init()  #初始化
screen = pygame.display.set_mode((800, 600)) #, FULLSCREEN) #设置屏幕大小
clock = pygame.time.Clock()


#开始写代码的地方











#结束写代码的地方
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()

pygame.quit()
