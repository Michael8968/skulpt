import pygame,random,math,sys

from pygame.locals import *

######################################挑战1part1（学生完成部分）
'''
ccc = []
for ii in range(8):
    image = pygame.image.load('image/'+str(ii+1)+'.png')
    image = pygame.transform.smoothscale(image,(100,100))
    ccc.append(image)

a=random.randint(0,7)
'''
#########################

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("jiyi")

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((100,100,100))
    #time.tick(15)
################################################################## #挑战1part2（学生完成部分）
    ''' 
    for i in range(4):
        for j in range(4):
            screen.blit(ccc[a], (50 + 100*i,50 + 100*j))
    '''
    
###########################################

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    clock.tick(30)   #每秒30帧
    pygame.display.update()
    
