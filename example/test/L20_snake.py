
import pygame
import sys
import time
import random
from pygame.locals import *
# Pygame Init
pygame.init()

# Play Surface
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

# Game settings
delta = 10

snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
snakePos2 = [100, 350]
snakeBody2 = [[100, 350], [90, 350], [80, 350]]

foodPos = [400, 200]
#snakePos = [delta*4, delta*3]
#snakeBody = [[delta*4, delta*3], [delta*3, delta*3], [delta*2, delta*3]]
#foodPos = [delta*10, delta*3]
foodSpawn = True
direction = 'RIGHT'
direction2 = 'RIGHT'
score = 0
score2 = 0
gameover = False
winner = ''

# Show Score
def showScore(a,b):
    SFont = pygame.font.Font(None, 32)
    Ssurf = SFont.render("Score{1}p  :  {0}".format(a,b), True, black)
    if b == 1:
        screen.blit(Ssurf, (250,10))
    elif b == 2:
        screen.blit(Ssurf, (450,10))

def showEnd():
    font = pygame.font.SysFont(None, 88)
    fontimg = font.render('game over', True, red)
    screen.blit(fontimg, (250,250))
    fontimg2 = font.render('press return to restart', True, brown)
    screen.blit(fontimg2, (100,350))
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

def control_1p(aa):
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

def move(a,b):
    if a == 'RIGHT':
        b[0] += delta
    if a == 'LEFT':
        b[0] -= delta
    if a == 'DOWN':
        b[1] += delta
    if a == 'UP':
        b[1] -= delta

def is_game_over():
    if snakePos[0] >= width or snakePos[0] < 0:
        return True, '2p'
    if snakePos[1] >= height or snakePos[1] < 0:
        return True, '2p'
    if snakePos2[0] >= width or snakePos2[0] < 0:
        return True, '1p'
    if snakePos2[1] >= height or snakePos2[1] < 0:
        return True, '1p'

    # Self hit
    for block in snakeBody[1:]:
        if snakePos == block:
            return True, '2p'
        if snakePos2 == block:
            return True, '1p'

    for block in snakeBody2[1:]:
        if snakePos == block:
            return True, '2p'
        if snakePos2 == block:
            return True, '1p'

    if snakePos == snakePos2:
        return True, ''
    return False, ''


def is_game_over2():
    a = False
    b = ''
    if snakePos[0] >= width or snakePos[0] < 0:
        a = True
        b = '2p'
    if snakePos[1] >= height or snakePos[1] < 0:
        a = True
        b = '2p'
    if snakePos2[0] >= width or snakePos2[0] < 0:
        a = True
        b = '1p'
    if snakePos2[1] >= height or snakePos2[1] < 0:
        a = True
        b = '1p'
    # Self hit
    for block in snakeBody[1:]:
        if snakePos == block:
            a = True
            b = '2p'
        if snakePos2 == block:
            a = True
            b = '1p'
    for block in snakeBody2[1:]:
        if snakePos == block:
            a = True
            b = '2p'
        if snakePos2 == block:
            a = True
            b = '1p'
    if snakePos == snakePos2:
        a = True
    return a, b

def motion(score, foodSpawn, snakeBody, snakePos, color):
    snakeBody.insert(0, list(snakePos))
    if snakePos == foodPos:
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()

    for pos in snakeBody:
        pygame.draw.rect(screen, color, (pos[0], pos[1], delta, delta))
    return score, foodSpawn



while True:
    screen.fill(white)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        direction = control_1p(direction)
        direction2 = control_2p(direction2)

    move(direction,snakePos)
    move(direction2,snakePos2)

    score, foodSpawn = motion(score, foodSpawn, snakeBody, snakePos, green)
    score2, foodSpawn = motion(score2, foodSpawn, snakeBody2, snakePos2, blue)


    gameover, winner = is_game_over()
    #如果不想上面的写法，则改写函数后调用如下
    #gameover, winner = is_game_over2()


    if foodSpawn == False:
        foodPos = [random.randrange(1, width // delta) * delta, random.randrange(1, height // delta) * delta]
        foodSpawn = True
    pygame.draw.rect(screen, brown, (foodPos[0], foodPos[1], delta, delta))

    showScore(score,1)
    showScore(score2,2)

    if gameover:
        showEnd()
        while True:
            times.tick(10)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    snakePos = [100, 50]
                    snakeBody = [[100, 50], [90, 50], [80, 50]]
                    snakePos2 = [100, 350]
                    snakeBody2 = [[100, 350], [90, 350], [80, 350]]
                    foodPos = [400, 200]
                    foodSpawn = True
                    direction = 'RIGHT'
                    direction2 = 'RIGHT'
                    score = 0
                    score2 = 0
                    gameover = False
                    winner = ''
                    break
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    times.tick(30)
