import pygame,random,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("wuziqi")

#####加载各种图片
bac = pygame.image.load('lesson24/wuziqi/bac.jpg').convert_alpha()
bac = pygame.transform.smoothscale(bac, (800,800))

bacc = pygame.image.load('lesson24/wuziqi/bacc.png').convert_alpha()

white = pygame.image.load('lesson24/wuziqi/white.png').convert_alpha()
new_white = pygame.image.load('lesson24/wuziqi/new_white.png').convert_alpha()
black = pygame.image.load('lesson24/wuziqi/black.png').convert_alpha()
new_black = pygame.image.load('lesson24/wuziqi/new_black.png').convert_alpha()
times = pygame.time.Clock()

while True:
    times.tick(16)
    screen.fill((255,255,255))











######### 点击x或者按下esc退出游戏
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
