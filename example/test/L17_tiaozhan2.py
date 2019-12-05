import pygame,random,math,sys

from pygame.locals import *

######################################挑战2part1（学生完成部分）
'''
matrix=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

ccc = []
for ii in range(8):
    image = pygame.image.load('image/'+str(ii+1)+'.png')
    image = pygame.transform.smoothscale(image,(100,100))
    ccc.append(image)

hi = [1,2,3,4,5,6,7,8]

for i in range(16):
    matrix[i]=hi[random.randint(0,7)]

print(matrix)
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
################################################################## #挑战2part2（学生完成部分）
    '''
    d=0
    for i in range(4):
        for j in range(4):
            screen.blit(ccc[matrix[d]-1], (50 + 100*i,50 + 100*j))
            d+=1
   '''
###########################################

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    clock.tick(30)   #每秒30帧
    pygame.display.update()
    
