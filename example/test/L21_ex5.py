import pygame
import sys
import time
import random
from pygame.locals import * 
#######################################
# 拓展环节：按下enter后游戏重启

###############################
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
blue = (0, 0, 255)

# FPS controller
times = pygame.time.Clock()


direction = 'RIGHT'
direction2 = 'RIGHT'
block=10

snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]]


snake_pos2=[100,350]
snake_body2=[[100,350],[90,350],[80,350]]



game_over = False
foodPos = [400, 200]
score = 0
score2 = 0 

winner = '' 


def showScore(a,b):
    SFont = pygame.font.Font(None, 32)
    Ssurf = SFont.render("Score{1}p  :  {0}".format(a,b), True, black)  
    if b == 1:
        screen.blit(Ssurf, (250,10))
    elif b == 2:
        screen.blit(Ssurf, (450,10)) 


def move(a,b): 
    if a == 'RIGHT':
        b[0] += block
    if a == 'LEFT':
        b[0] -= block
    if a == 'DOWN':
        b[1] += block
    if a == 'UP':
        b[1] -= block  


################### 以下是拓展环节需要修改的代码 ################
'''
def gameover():
    font = pygame.font.SysFont(None, 88)
    fontimg = font.render('game over', True, red)  
    screen.blit(fontimg, (250,250))  
    fontimg2 = font.render('press return to restart', True, brown)
    screen.blit(fontimg2, (100,350))

    #显示胜利者   
    if winner:
        fontimg3 = font.render('winner is ' + winner, True, red)
        screen.blit(fontimg3, (250,450))
    else:
        if score > score2:
            fontimg3 = font.render('winner is 1p', True, red)
            screen.blit(fontimg3, (250,450)) 
        elif score < score2:
            fontimg3 = font.render('winner is 2p', True, red)
            screen.blit(fontimg3, (250,450))
        elif score == score2:
            fontimg3 = font.render('no winner', True, red)
            screen.blit(fontimg3, (250,450))   
'''
################### 以上是拓展环节需要修改的代码 ################

def logic():
    if snake_pos[0] >= width or snake_pos[0] < 0:
        return True, '2p'
    if snake_pos[1] >= height or snake_pos[1] < 0:
        return True, '2p'
    if snake_pos2[0] >= width or snake_pos2[0] < 0:
        return True, '1p'
    if snake_pos2[1] >= height or snake_pos2[1] < 0:
        return True, '1p'    
      
    # Self hit 撞到自己
    for block in snake_body[1:]:
        if snake_pos == block:
            return True, '2p'  
        if snake_pos2 == block:
            return True, '1p'
    
    for block in snake_body2[1:]:
        if snake_pos == block:
            return True, '2p'  
        if snake_pos2 == block:
            return True, '1p'
    
    if snake_pos == snake_pos2:
        if score > score2:
            return True, '1p'
        elif score < score2:
            return True, '2p'
        elif score == score2:
            return True, 'none'      
    return False, '' 



def control2(aa):
    if event.key == K_RIGHT:
        if aa != 'LEFT':
            aa = 'RIGHT'
            
    if event.key == K_LEFT:
        if aa != 'RIGHT':
            aa = 'LEFT'
        
    if event.key == K_UP:
        if aa != 'DOWN':
            aa = 'UP'
          
    if event.key == K_DOWN:
        if aa != 'UP':
            aa = 'DOWN'
    return aa  



def control_2p(aa):
    if event.key == K_d:
        if aa != 'LEFT':
            aa = 'RIGHT'
            
    if event.key == K_a:
        if aa != 'RIGHT':
            aa = 'LEFT'
        
    if event.key == K_w:
        if aa != 'DOWN':
            aa = 'UP'
          
    if event.key == K_s:
        if aa != 'UP':
            aa = 'DOWN'
    return aa  


def motion(score, foodPos, snake_body, snake_pos, color):
    snake_body.insert(0, list(snake_pos))
    if snake_pos == foodPos:
        foodPos = [random.randrange(1, width // block) * block, random.randrange(1, height // block) * block]
        score += 1
    else:
        snake_body.pop()
    pygame.draw.rect(screen, brown, (foodPos[0], foodPos[1], block, block))
    
    for pos in snake_body:
        pygame.draw.rect(screen, color, (pos[0], pos[1], block, block)) 

    return score, foodPos 

  

while True:
    screen.fill(white)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
   

    elif event.type == pygame.KEYDOWN:       
        direction = control2(direction)
        direction2 = control_2p(direction2)
    

    move(direction,snake_pos)   
    move(direction2,snake_pos2) 

    score, foodPos = motion(score, foodPos, snake_body, snake_pos, green)
    score2, foodPos = motion(score2, foodPos, snake_body2, snake_pos2, blue)

    
    game_over, winner = logic()

    showScore(score,1)
    showScore(score2,2)
    
################### 以下是拓展部分————代码 ####################

    if game_over:
        gameover()
        while True:            
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    snake_pos = [100, 50]
                    snake_body = [[100, 50], [90, 50], [80, 50]]
                    snake_pos2 = [100, 350]
                    snake_body2 = [[100, 350], [90, 350], [80, 350]]
                    foodPos = [400, 200]
                    direction = 'RIGHT'
                    direction2 = 'RIGHT'
                    score = 0
                    score2 = 0
                    game_over = False   
                    winner = ''
                    break
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            pygame.display.flip()
  
################### 以上是拓展部分————代码 ####################  

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit() 
        
    pygame.display.flip()
    times.tick(20)