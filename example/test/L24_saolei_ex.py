import pygame,random,math,sys
from pygame.locals import *
from datetime import datetime
from L24_saolei3def import open_block, get

###初始化并且加载图片
pygame.init()
screen = pygame.display.set_mode((350,450))
pygame.display.set_caption("saolei")

bac = pygame.image.load('lesson23/saolei/bac.png').convert()
times = pygame.time.Clock()



while True:
    times.tick(16)
    screen.blit(bac, (0,0))











############ 点击x或者按下esc退出游戏
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
