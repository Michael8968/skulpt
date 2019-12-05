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


direction = 'RIGHT'# 这一行代码与PPT 21 写出小球运动方向代码相关
block=10
snake_pos=[100,50]
snake_body=[[100,50],[90,50],[80,50]] 

##### 以下是 ex2 里对应 PPT 22 把运动方向改成函数的练习##############
'''
def move(): 
    if direction == 'RIGHT':
        snake_pos[0] += block
    elif direction == 'LEFT':
        snake_pos[0] -= block
    elif direction == 'DOWN':
        snake_pos[1] += block
    elif direction == 'UP':
        snake_pos[1] -= block
'''
#### 以上是 ex2 里对应 PPT 21 把运动方向改成函数的练习##############

##### 以下是 ex2 里对应 PPT 29 函数作用域的相关代码##############
'''
def control():
    #global direction             #一开始不写这个语句，会有什么问题 为什么其他变量，比如event.key,K_RIGHT 不用写global，涉及到函数内变量的规则，上面注释
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
##### 以上是 ex2 里对应 PPT 29 函数作用域的相关代码##############

##### 以下是 ex2 里对应 PPT 25 有返回值函数的相关代码##############
'''
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
'''
##### 以上是 ex2 里对应 PPT 25 有返回值函数的相关代码##############

while True:
    screen.fill(white)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        sys.exit()

    #elif event.type == pygame.KEYDOWN:       
        #direction = control2(direction) # 这两行与PPT 22 按键操纵小蛇运动代码改成函数有关      

    #move()# 这一行代码与PPT 22 把运动方向改成函数的练习有关                  
    
######################ex 2 以下的练习与PPT 21修正按键控制小蛇方向的代码有关,学生进行练习的老师，老师把
######################从第102-118行的代码取消标注状态，但是要删掉其中#标注的4行，让学生自己写#####  

    '''
    if event.type == pygame.KEYDOWN:
        
        if event.key == K_RIGHT or event.key == K_d:
            #if direction != 'LEFT':
                direction = 'RIGHT'

        elif event.key == K_LEFT or event.key == K_a:
            #if direction != 'RIGHT':
                direction = 'LEFT'
        
        elif event.key == K_UP or event.key == K_w:
            #if direction != 'DOWN':
                direction = 'UP'
          
        elif event.key == K_DOWN or event.key == K_s:
            #if direction != 'UP':
                direction = 'DOWN'  
    '''
#####################ex 2 以上的练习与PPT 21修正按键控制小蛇方向的代码有关####################
    '''
    if direction == 'RIGHT':
        snake_pos[0] += block
    elif direction == 'LEFT':
        snake_pos[0] -= block
    elif direction == 'DOWN':
        snake_pos[1] += block
    elif direction == 'UP':
        snake_pos[1] -= block 
    '''  # 上面8行代码与PPT 21的 修改小球运动代码 练习相关


 ######################以下代码不用动######################  


    snake_body.insert(0, list(snake_pos))
    snake_body.pop()   
    
    for pos in snake_body:
        pygame.draw.rect(screen, green, (pos[0], pos[1], block, block))


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit() 
        
    pygame.display.flip()
    times.tick(20)