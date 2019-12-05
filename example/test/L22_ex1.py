import pygame,random,sys
from pygame.locals import *



##### 任务1 人原地跑 + 地面

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("No One Die")
times = pygame.time.Clock()

################# PPT 5 任务 ##############
'''
img = []
for i in range(5):
    aa = pygame.image.load('lesson22/noOneToDie/h' + str(i+1) + '.png').convert_alpha()
    img.append(aa)

n = 0
while True:
    times.tick(30) #这一行可以给学生
    screen.fill((255,255,255))

    n += 1
    screen.blit(img[n%5], (30, 363))       # 小人图片
    pygame.draw.rect(screen, (0,0,0), (0, 420, 800, 5))   # 地上黑线

'''
################# PPT 5 任务 ##############

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update()
