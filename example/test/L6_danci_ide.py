#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import pygame,random
import sys
import time
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("words testing")
enfont = pygame.font.Font(None, 60)
zhfont = pygame.font.Font('simhei.ttf', 25)


xiang = pygame.image.load('lesson6/xiang.png').convert_alpha()
xiang = pygame.transform.smoothscale(xiang, (150,150))
xiang2 = pygame.transform.smoothscale(xiang, (154,154))
kong = pygame.image.load('lesson6/kong.png').convert_alpha()
kong = pygame.transform.smoothscale(kong, (150,150))
man = pygame.image.load('lesson6/man.png').convert_alpha()
man = pygame.transform.smoothscale(man, (150,150))

bac = pygame.image.load('lesson6/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (800,600))

big1 = 0
big2 = 0
big3 = 0
big4 = 0
op1 = 0
op2 = 0
op3 = 0
op4 = 0
score = 0
#zhongwen = []
all_words = { 'python': '蟒蛇', 'move': '移动', 'image': '图像', 'input': '输入',
              'print': '打印', 'up': '上', 'down': '下', 'right': '右', 'left': '左',
              'turtle': '海龟', 'forward': '向前的', 'goto': '转到', 'pen': '笔',
              'dot': '点', 'integer': '整数', 'string': '字符串', 'float': '浮点型',
              'bug': '程序缺陷', 'import': '进口', 'random': '随机的', 'max': '最大值',
              'min': '最小值', 'choice': '选择', 'red': '红的', 'green': '绿的',
              'blue': '蓝的', 'range': '范围', 'get': '取得', 'mode': '方式', 'feed': '喂'}

all_keys = list(all_words.keys())
#print(len(all_keys))
ques = []

num = 0
check = 0


for i in range(15):
    l = len(all_keys)
    aa = all_keys.pop(random.randint(0,l-1))
    ques.append(aa)
print(ques)

all_values = list(all_words.values())
#print(all_values)



def getZh(aa):
    global all_values
    global all_words
    global ques

    num = aa
    zhongwen = []
    zhongwen.append(all_words[ques[num]])


    for i in range(3):
        #print(all_values)
        random.shuffle(all_values)

        l = len(all_values)
        #n =
        value = all_values[random.randint(0,l-1)]
        while value in zhongwen:
            value = all_values[random.randint(0,len(all_values)-1)]
        else:
            zhongwen.append(value)
    random.shuffle(zhongwen)
    return zhongwen


ans = []
for i in range(15):
    a = getZh(i)
    ans.append(a)
#print(ans)
rightAns = []

for i in range(15):
    right = all_words[ques[i]]
    rightAns.append(ans[i].index(right))

print(rightAns)

nextQ = zhfont.render('下一题', 1 , (255,255,255))
nextQ = pygame.transform.smoothscale(nextQ,(100, 50))
nextQ2 = pygame.transform.smoothscale(nextQ,(104, 54))
bigxia = 0
finish = zhfont.render('完成', 1 , (255,255,255))
finish = pygame.transform.smoothscale(finish,(100, 50))
finish2 = pygame.transform.smoothscale(finish,(104, 54))

show = 0

while True:

    time.sleep(0.01)
    if check != num:
        big1 = 0
        big2 = 0
        big3 = 0
        big4 = 0
        op1 = 0
        op2 = 0
        op3 = 0
        op4 = 0
        check = num
        print(num)

    screen.blit(bac, (0,0))
    enText = enfont.render(ques[num], True, (255,255,255))
    #a = getZh()
    #print(a)
    screen.blit(enText, (350, 200))
    scoreImg = enfont.render(str(score), 1, (255,255,255))
    screen.blit(scoreImg, (600, 100))
    if show == 1:
        endtxt = zhfont.render('你的得分是：' + str(score), 1, (255,255,255))
        screen.blit(endtxt,(300, 500))

    atxt = zhfont.render(ans[num][0], 1, (255,255,255))
    btxt = zhfont.render(ans[num][1], 1, (255,255,255))
    ctxt = zhfont.render(ans[num][2], 1, (255,255,255))
    dtxt = zhfont.render(ans[num][3], 1, (255,255,255))
    screen.blit(atxt, (140, 400))
    screen.blit(btxt, (290, 400))
    screen.blit(ctxt, (440, 400))
    screen.blit(dtxt, (590, 400))
    if num < 14:
        if bigxia == 0:
            screen.blit(nextQ, (600,500))
        else:
            screen.blit(nextQ2, (598,498))
    elif num == 14:
        if bigxia == 0:
            screen.blit(finish, (600,500))
        else:
            screen.blit(finish2, (598,498))


    if big1 == 0:
        screen.blit(xiang, (120, 250))
    else:
        if op1 == 1:
            screen.blit(kong,(120,250))
        elif op1 == 2:
            screen.blit(man, (120, 250))
        else:
            screen.blit(xiang2, (118, 248))
    if big2 == 0:
        screen.blit(xiang, (270, 250))
    else:
        if op2 == 1:
            screen.blit(kong,(270, 250))
        elif op2 == 2:
            screen.blit(man,(270, 250))
        else:
            screen.blit(xiang2, (268, 248))
    if big3 == 0:
        screen.blit(xiang, (420, 250))
    else:
        if op3 == 1:
            screen.blit(kong, (420, 250))
        elif op3 == 2:
            screen.blit(man, (420, 250))
        else:
            screen.blit(xiang2, (418, 248))
    if big4 == 0:
        screen.blit(xiang, (570, 250))
    else:
        if op4 == 1:
            screen.blit(kong, (570, 250))
        elif op4 == 2:
            screen.blit(man, (570, 250))
        else:
            screen.blit(xiang2, (568, 248))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == MOUSEMOTION:
            if pygame.Rect(140,305,100,75).collidepoint(event.pos):
                #print('peng')
                big1 = 1
            else:
                if op1 == 1 or op1 == 2:
                    big1 = 1
                else:
                    big1 = 0
            if pygame.Rect(290,305,100,75).collidepoint(event.pos):
                #print('peng')
                big2 = 1
            else:
                if op2 == 1 or op2 == 2:
                    big2 = 1
                else:
                    big2 = 0
            if pygame.Rect(440,305,100,75).collidepoint(event.pos):
                #print('peng')
                big3 = 1
            else:
                if op3 == 1 or op3 == 2:
                    big3 = 1
                else:
                    big3 = 0
            if pygame.Rect(590,305,100,75).collidepoint(event.pos):
                #print('peng')
                big4 = 1
            else:
                if op4 == 1 or op4 == 2:
                    big4 = 1
                else:
                    big4 = 0

            if pygame.Rect(600,500,100,50).collidepoint(event.pos):
                bigxia = 1
            else:
                bigxia = 0
        if event.type == MOUSEBUTTONDOWN:
            if pygame.Rect(140,305,100,75).collidepoint(event.pos) and not op2 and not op3 and not op4:
                if rightAns[num] == 0:
                    op1 = 2
                    score += 10
                else:
                    op1 = 1
                #num += 1

            elif pygame.Rect(290,305,100,75).collidepoint(event.pos) and not op1 and not op3 and not op4:
                if rightAns[num] == 1:
                    op2 = 2
                    score += 10
                else:
                    op2 = 1
                #num += 1

            elif pygame.Rect(440,305,100,75).collidepoint(event.pos) and not op1 and not op2 and not op4:
                if rightAns[num] == 2:
                    op3 = 2
                    score += 10
                else:
                    op3 = 1
                #num += 1

            elif pygame.Rect(590,305,100,75).collidepoint(event.pos) and not op1 and not op2 and not op3:
                if rightAns[num] == 3:
                    op4 = 2
                    score += 10
                else:
                    op4 = 1
                #num += 1

            if pygame.Rect(600,500,100,50).collidepoint(event.pos) and (op1 or op2 or op3 or op4):
                if num < 14:
                    num += 1
                elif num == 14:
                    show = 1



    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()







    pygame.display.update()
