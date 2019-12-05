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
#green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)

# FPS controller
times = pygame.time.Clock()


direction = 'RIGHT'
block=10
snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]] 
game_over = False


def move(): 
    if direction == 'RIGHT':
        snake_pos[0] += block
    elif direction == 'LEFT':
        snake_pos[0] -= block
    elif direction == 'DOWN':
        snake_pos[1] += block
    elif direction == 'UP':
        snake_pos[1] -= block

########### ex3 以下代码与PPT 36页练习相关#########################

def gameover():
    font = pygame.font.SysFont(None, 88)
    fontimg = font.render('game over', True, red)  
    screen.blit(fontimg, (250,250))
    pygame.display.update()
    #time.sleep(5)
    #pygame.quit() #第46-47行的代码可以加上也可以不加上

########### ex3 以上代码与PPT 36页练习相关#########################
'''
def control():
    #global direction             
    if event.key == K_RIGHT or event.key == K_d:
        if direction != 'LEFT':
            direction = 'RIGHT'

    if event.key == K_LEFT or event.key == K_a:
        if direction != 'RIGHT':
            direction = 'LEFT'
        
    if event.key == K_UP or event.key == K_w:
        if direction != 'DOWN':
            direction = 'UP'
          
    if event.key == K_DOWN or event.key == K_s:
        if direction != 'UP':
            direction = 'DOWN'
 '''

#####solution2###########return##############
def control2(aa):
    if event.key == K_RIGHT or event.key == K_d:
        if aa != 'LEFT':
            aa = 'RIGHT'
            
    if event.key == K_LEFT or event.key == K_a:
        if aa != 'RIGHT':
            aa = 'LEFT'
        
    if event.key == K_UP or event.key == K_w:
        if aa != 'DOWN':
            aa = 'UP'
          
    if event.key == K_DOWN or event.key == K_s:
        if aa != 'UP':
            aa = 'DOWN'
    return aa    #一开始不写return 会有什么问题

def get_color():
    red = random.randint(1,255)
    green = random.randint(1,255)
    blue = random.randint(1,255)
    color = (red,green,blue)
    

    return color



while True:
    screen.fill(white)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        sys.exit()

    elif event.type == pygame.KEYDOWN:       
        direction = control2(direction)   
    move() 

########### ex3 以下代码与PPT 36页练习相关#########################
    '''
    if snake_pos[0] >= width or snake_pos[0] < 0:
        game_over = True
    if snake_pos[1] >= height or snake_pos[1] < 0:
        game_over = True #碰撞

    if game_over:
    	gameover()
    '''
########### ex3 以上代码与PPT 36页练习相关#########################

    snake_body.insert(0, list(snake_pos))
    snake_body.pop()   
    color=get_color()
    for pos in snake_body:
        pygame.draw.rect(screen, color, (pos[0], pos[1], block, block))


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit() 
        
    pygame.display.flip()
    times.tick(20)