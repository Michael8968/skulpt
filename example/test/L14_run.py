import pygame,sys
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("racegame")
bac = pygame.image.load('lesson14/run/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (800,600))
img = []
for i in range(16):
    aa = pygame.image.load('lesson14/run/' + str(i+1) + '.png').convert_alpha()
    aa = pygame.transform.smoothscale(aa, (50, 75))
    img.append(aa)
 #################################################
 #课程上需要完成的部分
aaa =
bbb =
ccc =
ddd =
##################################################
clock = pygame.time.Clock()
startRun = False
while True:
    clock.tick(30)   #每秒30帧
    screen.blit(bac, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            startRun = True

    screen.blit(img[2], (0, 370))
    screen.blit(img[5], (0, 415))
    screen.blit(img[9], (0, 460))
    screen.blit(img[13], (0, 505))

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    #if startRun:
        #break
    pygame.display.update()

i = 0
times = pygame.time.Clock()

aspeed = 10
bspeed = 5
cspeed = 6
dspeed = 8

while True:
    clock.tick(30)   #每秒30帧
    i += 1
    times.tick(14)
    screen.blit(bac, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(aaa[i%4], (0 + aspeed*i, 370))
    screen.blit(bbb[i%4], (0 + bspeed*i, 415))
    screen.blit(ccc[i%4], (0 + cspeed*i, 460))
    screen.blit(ddd[i%4], (0 + dspeed*i, 505))

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
