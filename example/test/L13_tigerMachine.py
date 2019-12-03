import pygame,random,math,sys

from pygame.locals import *
from datetime import datetime, date, time


pygame.init()
screen = pygame.display.set_mode((800,300))
pygame.display.set_caption("Tiger Machine")
'''
img = []
for i in range(4):
    aa = pygame.image.load('tu/g' + str(i+1) + '.png').convert_alpha()
    img.append(aa)
'''
y = -900.0
y2 = -900.0
y3 = -900.0

#pic = img[random.randint(0,3)]
pic = pygame.image.load('lesson13/tu/tu4.png').convert_alpha()
times = pygame.time.Clock()

game = False
finish = False

while True:
    #print(game)
    times.tick(300)
    if game:
        current_time = pygame.time.get_ticks()//1000
        #print(current_time - start_time)
        if y < 0.0:
            if current_time - start_time <= roll_time - 4:
                y += 8
            elif current_time - start_time <= roll_time - 3:
                y += 5
            elif current_time - start_time <= roll_time - 2:
                y += 2
            elif current_time - start_time <= roll_time - 1:
                y += 1
            if current_time - start_time >= roll_time:
                '''
                if y == -1200:
                    y = -1200
                    #game = False
                elif y < -900 and y > -1200:
                    y += 0.5
                '''
                if y == -900.0:
                    y == -900.0
                    #game = False
                elif y < -600.0 and y > -900.0:
                    y += 0.5
                elif y == -600.0:
                    y == -600.0
                    #game = False
                elif y < -300.0 and y > -600.0:
                    y += 0.5
                elif y == -300.0:
                    y == -300.0
                    #game = False
                elif y < 0.0 and y > -300.0:
                    y += 0.5
        else:
            y = -900.0

        if y2 < 0.0:
            if current_time - start_time <= roll_time2 - 5:
                y2 += 8
            elif current_time - start_time <= roll_time2 - 3:
                y2 += 5
            elif current_time - start_time <= roll_time2 - 2:
                y2 += 2
            elif current_time - start_time <= roll_time2 - 1:
                y2 += 1
            if current_time - start_time >= roll_time2:
                '''
                if y2 == -1200:
                    y2 = -1200
                    #game = False
                elif y2 < -900 and y2 > -1200:
                    y2 += 0.5
                '''
                if y2 == -900.0:
                    y2 == -900.0
                    #game = False
                elif y2 < -600.0 and y2 > -900.0:
                    y2 += 0.5
                elif y2 == -600.0:
                    y2 == -600.0
                    #game = False
                elif y2 < -300.0 and y2 > -600.0:
                    y2 += 0.5
                elif y2 == -300.0:
                    y2 == -300.0
                    #game = False
                elif y2 < 0.0 and y2 > -300.0:
                    y2 += 0.5
        else:
            y2 = -900.0

        if y3 < 0.0:
            if current_time - start_time <= roll_time3 - 5:
                y3 += 8
            elif current_time - start_time <= roll_time3 - 3:
                y3 += 5
            elif current_time - start_time <= roll_time3 - 2:
                y3 += 2
            elif current_time - start_time <= roll_time3 - 1:
                y3 += 1
            if current_time - start_time >= roll_time3:
                '''
                if y3 == -1200:
                    y3 = -1200
                    game = False
                elif y3 < -900 and y3 > -1200:
                    y3 += 0.5
                '''
                if y3 == -900.0:
                    y3 == -900.0
                    game = False
                    finish = True
                elif y3 < -600.0 and y3 > -900.0:
                    y3 += 0.5
                elif y3 == -600.0:
                    y3 == -600.0
                    game = False
                    finish = True
                elif y3 < -300.0 and y3 > -600.0:
                    y3 += 0.5
                elif y3 == -300.0:
                    y3 == -300.0
                    game = False
                    finish = True
                elif y3 < 0.0 and y3 > -300.0:
                    y3 += 0.5
        else:
            y3 = -900.0
    if not game:
        print(y,y2,y3)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if not game:
                game = True
                finish = False
                start_time = pygame.time.get_ticks()//1000
                current_time = pygame.time.get_ticks()//1000
                #current_time2 = pygame.time.get_ticks()//1000
                #current_time3 = pygame.time.get_ticks()//1000
                roll_time = random.randint(5,8)
                roll_time2 = random.randint(10,12)
                roll_time3 = random.randint(14,16)
            #print(start_time)

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    screen.fill((0,0,100))






    '''
    if y >= 299:
        num = random.randint(0,3)
        pic = img[num]
        print(1)
    '''
    screen.blit(pic, (50, y))
    screen.blit(pic, (300, y2))
    screen.blit(pic, (550, y3))

    if finish:
        if y == y2 == y3:
            print('win')
            #break
        elif y == y2 or y == y3 or y2 == y3:
            print('two')
            continue
        print('lost')


    pygame.display.update()
