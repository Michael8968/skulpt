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

direction = 'RIGHT'
block=10
snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]] 
game_over = False
foodPos = [400, 50]


def move(): 
    if direction == 'RIGHT':
        snake_pos[0] += block
    elif direction == 'LEFT':
        snake_pos[0] -= block
    elif direction == 'DOWN':
        snake_pos[1] += block
    elif direction == 'UP':
        snake_pos[1] -= block


def gameover():
    font = pygame.font.SysFont(None, 88)
    fontimg = font.render('game over', True, red)  
    screen.blit(fontimg, (250,250))
    pygame.display.update()
    time.sleep(5)
    pygame.quit() 


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
    return aa   

while True:
    screen.fill(white)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    elif event.type == pygame.KEYDOWN:
        direction = control2(direction) 
    move()

############### 以下 ex 1 PPT 10 练习 食物对小蛇身体的影响 ############
    '''  
    pygame.draw.rect(screen, brown, (foodPos[0], foodPos[1], block, block))#画食物

    for pos in snake_body:
        pygame.draw.rect(screen, green, (pos[0], pos[1], block, block))
        
    snake_body.insert(0, list(snake_pos))    

    if snake_pos == foodPos:
        foodPos = [random.randrange(1, width // block) * block, random.randrange(1, height // block) * block]

    else:
        snake_body.pop()

    '''
################## 以上 ex 1 PPT 10 练习 食物对小蛇身体的影响 ############
 
    if snake_pos[0] >= width or snake_pos[0] < 0:
        game_over = True
    if snake_pos[1] >= height or snake_pos[1] < 0:
        game_over = True #碰撞
    
############## ex 1 PPT 10 练习 新增游戏规则，如果碰到自己也算游戏结束 ############
    '''   
    for body in snake_body[1:]:
        if snake_pos == body:
            game_over = True 
    '''   
############## ex 1 PPT 10 练习 新增游戏规则，如果碰到自己也算游戏结束 ############
    if game_over:
        gameover()
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit() 
        
    pygame.display.flip()
    times.tick(20)