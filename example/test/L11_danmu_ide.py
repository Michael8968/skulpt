import pygame
from pygame.locals import *
from random import randint

class String(object):
    def __init__(self, x, y, speed, string):
        font = pygame.font.Font('simhei.ttf', randint(5,30))
        self.x = x
        self.y = y
        self.speed = speed
       # self.string = string
        self.img = font.render(string, True, (randint(10,250),randint(10,250),randint(10,250)))


str1 = '今天是个好日子啊每个人都能心想事成啊大吉大利今晚吃鸡好好学习天天向上'
list = ['666','66666','厉害厉害','好好学习，天天向上','大吉大利','社会社会',
        '你们知道他有多努力么','233333','23333','爱狗人士表示墙裂谴责',
        '爱谴责人士表示强烈狗','卖竹鼠啦','嘤嘤嘤','嘤嘤嘤','竹鼠3块一只，10块三只',
        '大天朝万岁','社会主义万岁','共产党万岁','毛主席万岁','66666666666666666666']

bac = []
for i in range(7):
    file = 'lesson11/bac' + str(i+1) + '.png'
    aa = pygame.image.load(file)
    aa = pygame.transform.smoothscale(aa, (800,600))
    bac.append(aa)
num = 0

pygame.init()
screen = pygame.display.set_mode((800, 600)) #, FULLSCREEN)
clock = pygame.time.Clock()
strings = []
timepass = 0

# 在第一帧，画上一些星星
for string in list:
    x = float(randint(0, 799))
    y = float(randint(0, 599))
    speed = float(randint(10, 300))
    strings.append( String(x, y, speed, string) )

clock = pygame.time.Clock()
flag = 0

while True:
    clock.tick(30)   #每秒30帧
    if flag <= 100:
        flag += 1
    else:
        flag = 0
        num += 1
    if num == 7:
        num = 0
    screen.blit(bac[num], (0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            pass

    # 增加一颗新的星星
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.

    if flag % 100 == 0:
        y = float(randint(0, 599))
        speed = float(randint(10, 300))
        string = String(800, y, speed, list[randint(0,len(list)-1)])
        strings.append(string)
        #print(flag)

    #screen.fill((0, 0, 0))

    # 绘制所有的星
    for string in strings:
        new_x = string.x - time_passed_seconds * string.speed
        screen.blit(string.img, (string.x, string.y))
        string.x = new_x
    pygame.display.update()
