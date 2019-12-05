import pygame,random,sys
from pygame.locals import *
from L22_aaaaadef import showScore,showEnd,reset,judge,create,jumping
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("No One Die")

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

    random_time = create(screen,random_time,rect_list, 270)
    random_time2 = create(screen,random_time2,rect_list2, 520)
    random_time3 = create(screen,random_time3,rect_list3, 770)


    n += 1
    screen.blit(img1[n%5], (30, 213 - high))
    screen.blit(img2[n%5], (30, 463 - high2))
    screen.blit(img3[n%5], (30, 713 - high3))

    gameover, score = judge(screen, rect_list, man_rect, gameover, score)
    gameover, score = judge(screen, rect_list2, man2_rect, gameover,score)
    gameover, score = judge(screen, rect_list3, man3_rect, gameover,score)

    print(rect_list)
    print(score)


    jump, high, can_jump = jumping(jump, high, can_jump)
    jump2, high2, can_jump2 = jumping(jump2, high2, can_jump2)
    jump3, high3, can_jump3 = jumping(jump3, high3, can_jump3)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if can_jump:
                    jump = 24
                    high = 24
                    can_jump = False

            elif event.key == K_DOWN:
                if can_jump2:
                    jump2 = 30
                    high2 = 0
                    can_jump2 = False

            elif event.key == K_RIGHT:
                if can_jump3:
                    jump3 = 30
                    high3 = 0
                    can_jump3 = False

    showScore(screen, score)

    if gameover:
        showEnd(screen)
        while True:
            times.tick(10)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    jump,high,can_jump,rect_list,random_time = reset()
                    jump2,high2,can_jump2,rect_list2,random_time2 = reset()
                    jump3,high3,can_jump3,rect_list3,random_time3 = reset()
                    n = 0
                    gameover = False
                    score = 0
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

    pygame.display.update()
