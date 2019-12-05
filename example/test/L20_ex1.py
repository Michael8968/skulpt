import pygame
import sys
import time
import random
from pygame.locals import * 


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Change")
# Colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)

# FPS controller
times = pygame.time.Clock()



################ ex1  需要学生完成的部分 #####################
'''
block=10
snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]] #初始状态
'''
################# ex1 需要学生完成的部分#########################
while True:
    screen.fill(white)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

################ ex1 需要学生完成的部分 #####################
    '''
    snake_pos[0] += block

    snake_body.insert(0, list(snake_pos))# 新知识点1
    snake_body.pop()#新知识点2    
    
    for pos in snake_body:
        pygame.draw.rect(screen, green, (pos[0], pos[1], block, block))
    '''

################ ex1 需要学生完成的部分 #############################
   
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit() 
        
    pygame.display.flip()
    times.tick(20)
