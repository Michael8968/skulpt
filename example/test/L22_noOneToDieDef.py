import pygame,random,sys

from pygame.locals import *
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("No One Die")


def showScore():
    SFont = pygame.font.Font(None, 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, (0,0,0))
    screen.blit(Ssurf, (350,10))
def showEnd():
    font = pygame.font.Font(None, 88)
    fontimg = font.render('game over', True, (255,0,0))
    screen.blit(fontimg, (250,250))
    fontimg2 = font.render('press return to restart', True, (255,0,0))
    screen.blit(fontimg2, (100,350))

def reset():       #设置初始值跟重置初始值的函数
    jump = 0
    high = 0
    can_jump = True
    rect_list = []
    random_time = 0
    return jump, high, can_jump, rect_list, random_time

def judge(rect_list, man_rect, gameover, score):    #判断是否游戏结束跟加分的函数
    for r in rect_list:
        pygame.draw.rect(screen, (0,0,0), r)
        if man_rect.colliderect(Rect(r[0],r[1],r[2],r[3])):
            gameover = True
        if r[0] <= -30:
            score += 1
            rect_list.pop(0)
    return gameover, score

def create(random_time, rect_list, place):        # 随机时间生成随机大小障碍物的函数，并使其向左移动
    pygame.draw.rect(screen, (0,0,0), (0, place, 800, 5))
    if random_time == 0:
        random_time = random.randint(110,150)
        rectx = random.randint(10,25)
        recty = random.randint(30,45)
        rect_l = [800, place-recty, rectx, recty]
        rect_list.append(rect_l)
    else:
        random_time -= 1

    for r in rect_list:
        r[0] -= 6
    return random_time

def jumping(jump, high, can_jump):
    if jump > -24:
        jump -= 2
    if high >= 24:
        high += jump
    else:
        can_jump = True
    return jump, high, can_jump


img = []
for i in range(15):
    aa = pygame.image.load('lesson22/noOneToDie/h' + str(i+1) + '.png').convert_alpha()
    img.append(aa)

img1 = img[:5]
img2 = img[5:10]
img3 = img[10:15]

times = pygame.time.Clock()
n = 0
score = 0
'''
##########1P
jump = 0
high = 0
can_jump = True
rect_list = []
rectx = 0
recty = 0
random_time = 0

###########2P
jump2 = 0
high2 = 0
can_jump2 = True
rect_list2 = []
rectx2 = 0
recty2 = 0
random_time2 = 0

#############3P
jump3 = 0
high3 = 0
can_jump3 = True
rect_list3 = []
rectx3 = 0
recty3 = 0
random_time3 = 0
'''
jump,high,can_jump,rect_list,random_time = reset()
jump2,high2,can_jump2,rect_list2,random_time2 = reset()
jump3,high3,can_jump3,rect_list3,random_time3 = reset()

#man_rect = img[0].get_rect()
gameover = False

while True:
    times.tick(30)
    screen.fill((255,255,255))

    man_rect = Rect(35, 213 -high, 40, 60)
    man2_rect = Rect(35, 463 -high2, 40, 60)
    man3_rect = Rect(35, 713 -high3, 40, 60)
    #print(man_rect)

    '''
    if random_time == 0:
        random_time = random.randint(110,150)
        rectx = random.randint(10,25)
        recty = random.randint(30,45)
        rect_l = [800, 270-recty, rectx, recty]
        rect_list.append(rect_l)
    else:
        random_time -= 1


    if random_time2 == 0:
        random_time2 = random.randint(110,150)
        rectx2 = random.randint(10,25)
        recty2 = random.randint(30,45)
        rect_l2 = [800, 520-recty2, rectx2, recty2]
        rect_list2.append(rect_l2)
    else:
        random_time2 -= 1


    if random_time3 == 0:
        random_time3 = random.randint(110,150)
        rectx3 = random.randint(10,25)
        recty3 = random.randint(30,45)
        rect_l3 = [800, 770-recty3, rectx3, recty3]
        rect_list3.append(rect_l3)
    else:
        random_time3 -= 1
    '''
    random_time = create(random_time,rect_list, 270)
    random_time2 = create(random_time2,rect_list2, 520)
    random_time3 = create(random_time3,rect_list3, 770)


    n += 1
    screen.blit(img1[n%5], (30, 213 - high))
    #pygame.draw.rect(screen, (0,0,0), (0, 270, 800, 5))

    screen.blit(img2[n%5], (30, 463 - high2))
    #pygame.draw.rect(screen, (0,0,0), (0, 520, 800, 5))

    screen.blit(img3[n%5], (30, 713 - high3))
    #pygame.draw.rect(screen, (0,0,0), (0, 770, 800, 5))

    '''
    for r in rect_list:
        r[0] -= 6

    for r2 in rect_list2:
        r2[0] -= 6

    for r3 in rect_list3:
        r3[0] -= 6
    '''
    '''
    for r in rect_list:
        pygame.draw.rect(screen, (0,0,0), r)
        if man_rect.colliderect(Rect(r)):
            gameover = True
        if r[0] <= -30:
            score += 1
            rect_list.pop(0)


    for r2 in rect_list2:
        pygame.draw.rect(screen, (0,0,0), r2)
        if man2_rect.colliderect(Rect(r2)):
            gameover = True
        if r2[0] <= -30:
            score += 1
            rect_list2.pop(0)


    for r3 in rect_list3:
        pygame.draw.rect(screen, (0,0,0), r3)
        if man3_rect.colliderect(Rect(r3)):
            gameover = True
        if r3[0] <= -30:
            score += 1
            rect_list3.pop(0)
    '''
    gameover, score = judge(rect_list, man_rect, gameover, score)
    gameover, score = judge(rect_list2, man2_rect, gameover,score)
    gameover, score = judge(rect_list3, man3_rect, gameover,score)

    print(rect_list)
    print(score)


    jump, high, can_jump = jumping(jump, high, can_jump)
    jump2, high2, can_jump2 = jumping(jump2, high2, can_jump2)
    jump3, high3, can_jump3 = jumping(jump3, high3, can_jump3)
    '''
    high = high + jump
    jump -= 3

    if high <= 0:
        high = 0
        jump = 0
        can_jump = True

    high2 = high2 + jump2
    jump2 -= 3

    if high2 <= 0:
        high2 = 0
        jump2 = 0
        can_jump2 = True


    high3 = high3 + jump3
    jump3 -= 3

    if high3 <= 0:
        high3 = 0
        jump3 = 0
        can_jump3 = True
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if can_jump:
                    jump = 30
                    high = 0
                    can_jump = False

            elif event.key == pygame.K_DOWN:
                if can_jump2:
                    jump2 = 30
                    high2 = 0
                    can_jump2 = False

            elif event.key == pygame.K_RIGHT:
                if can_jump3:
                    jump3 = 30
                    high3 = 0
                    can_jump3 = False

    showScore()

    if gameover:
        showEnd()
        while True:
            times.tick(10)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jump,high,can_jump,rect_list,random_time = reset()
                    jump2,high2,can_jump2,rect_list2,random_time2 = reset()
                    jump3,high3,can_jump3,rect_list3,random_time3 = reset()
                    '''
                    jump = 0
                    high = 0
                    rect_list = []
                    rectx = 0
                    recty = 0
                    random_time = 0
                    can_jump = True

                    jump2 = 0
                    high2 = 0
                    rect_list2 = []
                    rectx2 = 0
                    recty2 = 0
                    random_time2 = 0
                    can_jump2 = True

                    jump3 = 0
                    high3 = 0
                    rect_list3 = []
                    rectx3 = 0
                    recty3 = 0
                    random_time3 = 0
                    can_jump3 = True
                    '''

                    n = 0
                    gameover = False
                    score = 0
                    break
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update()
