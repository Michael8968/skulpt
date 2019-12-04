#!/usr/bin/env python3
#! -*-conding:utf-8 -*-

#!@Time   :2018/3/30 15:05
#!@Author :@liuweqia
#!@File   :Story.py

import pygame
from pygame.locals import *
from random import randint
num = 0

def showText(string):
    font = pygame.font.Font('simhei.ttf', 25)
    global screen
    global num
    if len(string) <= 23:
        if num < len(string):
            num += 1
            imgText = font.render(string[0:num], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
        else:
            num = len(string)
            imgText = font.render(string[0:num], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
    elif len(string) <= 46:
        if num < 23:
            num += 1
            imgText = font.render(string[0:num], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
        elif num >= 23 and num < len(string):
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            num += 1
            imgText2 = font.render(string[23:num], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
        else:
            num = len(string)
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            imgText2 = font.render(string[23:num], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
    elif len(string) <= 69:
        if num < 23:
            num += 1
            imgText = font.render(string[0:num], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
        elif num >= 23 and num < 46:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            num += 1
            imgText2 = font.render(string[23:num], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
        elif num >= 46 and num < 69:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            imgText2 = font.render(string[23:46], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
            num += 1
            imgText3 = font.render(string[46:num], True, (255, 255, 255))
            screen.blit(imgText3, (180, 535))
        else:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            imgText2 = font.render(string[23:46], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
            num = len(string)
            imgText3 = font.render(string[46:num], True, (255, 255, 255))
            screen.blit(imgText3, (180, 535))
    elif len(string) <= 92:
        if num < 23:
            num += 1
            imgText = font.render(string[0:num], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
        elif num >=23 and num < 46:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            num += 1
            imgText2 = font.render(string[23:num], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
        elif num >= 46 and num < 69:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            imgText2 = font.render(string[23:46], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
            num += 1
            imgText3 = font.render(string[46:num], True, (255, 255, 255))
            screen.blit(imgText3, (180, 535))
        elif num >= 69 and num < 92:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            imgText2 = font.render(string[23:46], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
            imgText3 = font.render(string[46:69], True, (255, 255, 255))
            screen.blit(imgText3, (180, 535))
            num += 1
            imgText4 = font.render(string[69:num], True, (255, 255, 255))
            screen.blit(imgText4, (180, 565))
        else:
            imgText = font.render(string[0:23], True, (255, 255, 255))
            screen.blit(imgText, (180, 475))
            imgText2 = font.render(string[23:46], True, (255, 255, 255))
            screen.blit(imgText2, (180, 505))
            imgText3 = font.render(string[46:69], True, (255, 255, 255))
            screen.blit(imgText3, (180, 535))
            num = len(string)
            imgText4 = font.render(string[69:num], True, (255, 255, 255))
            screen.blit(imgText4, (180, 565))


'''
def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color, (255,255,0))
    screen.blit(imgText, (x,y))
'''

def run():
   # pygame.init()
    step = 0
  #  screen = pygame.display.set_mode((800, 600))  # , FULLSCREEN)

    bac1 = pygame.image.load('lesson4/bac1.png').convert_alpha()
    bac1 = pygame.transform.smoothscale(bac1, (800, 600))
    bac2 = pygame.image.load('lesson4/bac2.png').convert_alpha()
    bac2 = pygame.transform.smoothscale(bac2, (800, 600))
    bac3 = pygame.image.load('lesson4/bac3.png').convert_alpha()
    bac3 = pygame.transform.smoothscale(bac3, (800, 600))
    da = pygame.image.load('lesson4/da.png').convert_alpha()
    da = pygame.transform.smoothscale(da, (200, 300))
    er = pygame.image.load('lesson4/er.png').convert_alpha()
    er = pygame.transform.smoothscale(er, (185, 300))
    san = pygame.image.load('lesson4/san.png').convert_alpha()
    san = pygame.transform.smoothscale(san, (200, 300))
    wang = []
    for i in range(4):
        im = pygame.image.load('lesson4/wang' + str(i + 1) + '.png').convert_alpha()
        im = pygame.transform.smoothscale(im, (175,300))
        wang.append(im)
    kuan = pygame.image.load('lesson4/kuan.png').convert_alpha()
    kuan = pygame.transform.smoothscale(kuan, (680, 155))

    clock = pygame.time.Clock()

    white = (255, 255, 255)
    kuany = 600
    renx = -200
    global num
    num = 0
    font = pygame.font.Font('simhei.ttf', 25)
    king = '今天，我有一件重要的事情要宣布，我现在年事渐高，准备从你们三人中选出一个继承我{1}的人。我会给你们出个{0}，答案使我满意的人，将成为下一任的国王。'.format('题目','王位')
    king2 = '今年我们的国家遭遇了比较重大的{}，很多穷苦的人受此影响吃不上饭，所以本王现在准备发放国家的储备粮。'.format('旱灾')
    king3 = '那问题就来了，如果一个穷人需要4个{a}才能吃饱，现在本王给你们每人10个{a}，你们觉得你们可以接济几个穷人？'.format(a='面包')
    prince1 = '大王子：这是我的面包，为什么要分给别人。'

    aa=10
    bb=aa/4
    cc=2

    prince2 = '二王子：我知道我知道！10除以4等于'+bb+'，所以我可以帮助'+bb+'个人。'
    king4 = '你见过'+bb+'个人吗？'
    prince3 = '小王子：我可以再买'+cc+'块面包，这样就可以分给'+(aa+cc)/4+'个穷人让他们吃饱啦。'



    while True:
        clock.tick(30)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                print(1)
                if step <= 10:
                    step += 1
                    kuany = 600
                    renx = -200
                    num = 0
                else:
                    pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()


        time_passed = clock.tick()
        if step == 0:
            screen.blit(bac1, (0, 0))
            #screen.blit(kuan, (120, 450))
            #screen.blit(wang[0], (0, 300))

        elif step == 1:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(wang[0], (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(king)

        elif step == 2:
            screen.blit(bac2, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(wang[0], (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(king2)
        elif step == 3:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(wang[0], (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(king3)
        elif step == 4:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(da, (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(prince1)
        elif step == 5:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(wang[1], (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText('......')
        elif step == 6:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(er, (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(prince2)
        elif step == 7:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(wang[2], (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(king4)
        elif step == 8:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(san, (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText(prince3)
        elif step == 9:
            screen.blit(bac1, (0, 0))
            screen.blit(kuan, (120, kuany))
            if kuany > 450:
                kuany -= 10
            else:
                kuany = 450
            screen.blit(wang[3], (renx, 300))
            if renx < 0:
                renx += 10
            else:
                renx = 0
            if kuany == 450:
                showText('很好。')
        elif step == 10:
            screen.fill((0,0,0))
            ss = '很多年以后，三王子成为了国王，人们过上富足的生活......'
            num += 1
            font = pygame.font.Font('simhei.ttf', 30)
            if num < len(ss):
                imgText = font.render(ss[0:num], True, (255, 255, 255))
                screen.blit(imgText, (20, 300))
            else:
                num = len(ss)
                imgText = font.render(ss[0:num], True, (255, 255, 255))
                screen.blit(imgText, (20, 300))

            #guodudonghua
        elif step == 11:
            screen.blit(bac3, (0, 0))











        pygame.display.update()


#if __name__ == "__main__":
pygame.init()
screen = pygame.display.set_mode((800, 600))
run()
