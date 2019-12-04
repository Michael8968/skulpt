#! -*-conding:utf-8 -*-
import pygame,sys,random
#import time
from pygame.locals import *


def getNum():
    num = [23,533,245,223,435,234]   #输入40到550之间的任意的六个数

    if len(num) != 0:
        num.remove(max(num)) #去掉最大数
        num.remove(min(num)) #去掉最小数

    a = random.choice(num) #在剩下的四个数字里随机取1个，做为第一个小球出现的横坐标
    b = random.choice(num) # 在剩下的四个数字里随机取1个，做为第一个小球出现的纵坐标


    return a, b



class MyBall(object):
    def __init__(self, x, y):
        self.radius = random.randrange(40)
        self.posx = x
        self.posy = y
        self.speedx = random.randrange(-10,10)
        self.speedy = random.randrange(-10,10)

        self.color = 100,110,0   #让小球变得更加好看，让颜色随机

    def __str__(self):
        return '第一个小球的起始位置：(' + str(self.posx) + ' , ' + str(self.posy) + ')'






class Group(object):
    def __init__(self, screen):
        self.screen = screen
        self.color = []
        self.radius = []
        self.posx = []
        self.posy = []
        self.speedx = []
        self.speedy = []
        self.timer = pygame.time.Clock()
        self.num = 0
        self.show = []

    def add(self, ball):
        self.num += 1
        self.color.append(ball.color)
        self.radius.append(ball.radius)
        self.posx.append(ball.posx)
        self.posy.append(ball.posy)
        self.speedx.append(ball.speedx)
        self.speedy.append(ball.speedy)
        self.show.append(str(ball))


    def update(self):
        for i in range(self.num):
            self.posx[i] += self.speedx[i]
            self.posy[i] += self.speedy[i]
            if self.posx[i]+self.radius[i] >= 800 or self.posx[i]-self.radius[i] <= 0:
                self.speedx[i] = -self.speedx[i]

            if self.posy[i]+self.radius[i] >= 600 or self.posy[i]-self.radius[i] <= 0:
                self.speedy[i] = -self.speedy[i]



    def draw(self):
        for i in range(self.num):
            pygame.draw.circle(self.screen,self.color[i],
                               (self.posx[i],self.posy[i]), self.radius[i])



    def main_loop(self):
        while True:
            self.timer.tick(30)
            ticks = pygame.time.get_ticks()
            self.screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  #如果鼠标按下
                    spot = pygame.mouse.get_pos()
                    x = random.randrange(40,559)
                    y = random.randrange(40,559)
                    autoBall = MyBall(x,y)
                    group.add(autoBall)

            self.update()
            self.draw()
            font = pygame.font.Font('simhei.ttf',15)
            imgText = font.render(self.show[0], True, (0,0,0))
            imgText2 = font.render('第一个小球的当前位置：(' +str(self.posx[0]) +
                                   ' , ' + str(self.posy[0]) + ')', True, (0,0,0))
            screen.blit(imgText, (10,10))
            screen.blit(imgText2, (10,30))


            pygame.display.update()


#if __name__ == '__main__':
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Enter the numbers")




ballx, bally = getNum()




ball = MyBall(ballx,bally)



print(ball)
group = Group(screen)
group.add(ball)

group.main_loop()




pygame.quit()
sys.exit()
