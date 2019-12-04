import os
import sys
import pygame
import time
from pygame.locals import *

CAPTION = "Move xiaomeng"
SCREEN_SIZE = (800, 600)
'''
def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color, (255,255,0))
    screen.blit(imgText, (x,y))
'''
def loo():
    while True:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
              #  sys.exit()


class People(object):
    def __init__(self):
        self.x = 10
        self.y = 380
        self.rect = pygame.Rect(self.x,self.y,0,0)
        self.up = []
        self.down = []
        self.right = []
        self.guaizou = []
        self.meatNum = 0
        self.back = []
        self.backNum = 0
        self.eat = 0
        self.men = pygame.image.load('lesson5/men.png').convert_alpha()
        self.men = pygame.transform.smoothscale(self.men, (160,160))
        #self.image = self.load('zoulu.png', 105, 221, 4)
        self.meat = pygame.image.load('lesson5/meat2.png').convert_alpha()
        self.meat = pygame.transform.smoothscale(self.meat, (50,50))
        self.meatPos = [[145, 60],[300, 60],[455, 60],[610, 60]]
        #self.meatPos = []
        self.meatPos2 = [[200,10],[150,10],[100,10],[50,10]]
        self.meatRect = [pygame.Rect((145, 60),(30,30)),
                         pygame.Rect((300, 60),(30,30)),
                         pygame.Rect((455, 60),(30,30)),
                         pygame.Rect((610, 60),(30,30))]

        for i in range(4):
            a = pygame.image.load('lesson5/ren/d' + str(i+1) + '.png').convert_alpha()
            a = pygame.transform.smoothscale(a, (45,70))
            self.down.append(a)
        for i in range(4):
            a = pygame.image.load('lesson5/ren/u' + str(i+1) + '.png').convert_alpha()
            a = pygame.transform.smoothscale(a, (45,70))
            self.up.append(a)
        for i in range(4):
            a = pygame.image.load('lesson5/ren/r' + str(i+1) + '.png').convert_alpha()
            a = pygame.transform.smoothscale(a, (45,70))
            self.right.append(a)
        for i in range(4):
            a = pygame.image.load('lesson5/g' + str(i+1) + '.png').convert_alpha()
            a = pygame.transform.smoothscale(a, (400,400))
            self.guaizou.append(a)

        self.pika = pygame.image.load('lesson5/u2.png').convert_alpha()
        self.pika = pygame.transform.smoothscale(self.pika, (135,210))
        self.pika2 = pygame.image.load('lesson5/u2.png').convert_alpha()
        self.pika2 = pygame.transform.smoothscale(self.pika2, (135,210))
        self.guai1 = pygame.image.load('lesson5/guai3.png').convert_alpha()
        self.guai1 = pygame.transform.smoothscale(self.guai1, (400,400))
        self.guai2 = pygame.image.load('lesson5/guai4.png').convert_alpha()
        self.guai2 = pygame.transform.smoothscale(self.guai2, (400,400))
        #self.guai3 = pygame.image.load('lesson5/guai1.png').convert_alpha()
        #self.guai4 = pygame.image.load('lesson5/guai2.png').convert_alpha()

        bac1 = pygame.image.load('lesson5/bac1111.png').convert_alpha()
        bac1 = pygame.transform.smoothscale(bac1, (800,600))
        bac2 = pygame.image.load('lesson5/bac2.png').convert_alpha()
        bac2 = pygame.transform.smoothscale(bac2, (800,600))
        self.back.append(bac1)
        self.back.append(bac2)

    def showMeat(self):
        for meatPos in self.meatPos:
            screen.blit(self.meat, meatPos)
        screen.blit(self.meat, (700, 525))

    def showNum(self):
        font = pygame.font.Font(None, 54)
        imgText = font.render('X'+ str(self.meatNum), True, (255,255,255))
        screen.blit(imgText, (750, 535))

    def showBack(self):
        #screen.blit(self.bac1, (0,0))
        screen.blit(self.back[self.backNum], (0,0))


    def show(self):
        framerate = pygame.time.Clock()
        if self.backNum == 0:
            for n in range(30):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                framerate.tick(30)
                self.showBack()
                self.showMeat()
                self.showNum()
                screen.blit(self.down[2], (self.x, self.y))
                screen.blit(self.men, (560,440))
                pygame.display.update()
        elif self.backNum == 1:

            if self.eat < 4:
                for n in range(30):
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                    framerate.tick(30)
                    self.showBack()
                    self.showMeat()
                    self.showNum()
                    aa = pygame.transform.smoothscale(self.meat, (80,80))
                    screen.blit(aa, (255, 430))
                    screen.blit(self.pika, (200,400))

                    screen.blit(self.guai1, (300,100))
                    pygame.display.update()
            if self.eat == 4 and self.meatNum == 0:
                aa = []
                for i in range(4):
                    a = pygame.image.load('lesson5/ren/r' + str(i+1) + '.png').convert_alpha()
                    a = pygame.transform.smoothscale(a, (135,210))
                    aa.append(a)
                bb = []
                for i in range(4):
                    a = pygame.image.load('lesson5/ren/u' + str(i+1) + '.png').convert_alpha()
                    a = pygame.transform.smoothscale(a, (135,210))
                    bb.append(a)

                for n in range(60):
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                    framerate.tick(30)
                    self.showBack()
                    self.showMeat()
                    self.showNum()
                    screen.blit(self.pika, (200,400))
                    screen.blit(self.guaizou[n%12//3], (330+n*10,100))
                    pygame.display.update()
                for n in range(26):
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                    framerate.tick(30)
                    self.showBack()
                    self.showMeat()
                    self.showNum()
                    #screen.blit(self.pika, (200,400))
                    screen.blit(aa[n%12//3], (200+n*10,400))
                    print(200+n*10)
                    pygame.display.update()
                for n in range(20):
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                    framerate.tick(30)
                    self.showBack()
                    self.showMeat()
                    self.showNum()
                    #screen.blit(self.pika, (200,400))
                    screen.blit(bb[n%12//3], (450,400-n*10))
                    pygame.display.update()
               # self.moveRight(10)

    def feed(self):
        framerate = pygame.time.Clock()
        if self.backNum == 1:
            if self.meatNum != 0:
                self.meatPos.append(self.meatPos2[self.meatNum-1])
                self.eat += 1
                print(self.eat)
                self.meatNum -= 1
                for n in range(30):
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                    framerate.tick(30)
                    self.showBack()
                    self.showMeat()
                    self.showNum()
                    screen.blit(self.pika2, (205,395))
                    screen.blit(self.guai2, (300,100))
                    pygame.display.update()
            self.show()


    def moveUp(self, num=1):

        framerate = pygame.time.Clock()
        for n in range(num*5):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            framerate.tick(30)
            self.showBack()
            self.showMeat()
            self.showNum()
            screen.blit(self.up[n%12//3], (self.x, self.y))
            screen.blit(self.men, (560,440))
            self.y -= 5
            pygame.display.update()

            #fpsClock.tick(FPS)
    def moveDown(self, num=1):
        framerate = pygame.time.Clock()
        for n in range(num*5):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            framerate.tick(30)
            self.showBack()
            self.showMeat()
            self.showNum()
            screen.blit(self.down[n%12//3], (self.x, self.y))
            screen.blit(self.men, (560,440))
            self.y += 5
            pygame.display.update()

        if pygame.Rect(self.x,self.y,48,48).colliderect(pygame.Rect(600,500,100,100)):
            self.backNum = 1
            self.meatPos = []
            self.show()
    def moveRight(self, num=1):
        framerate = pygame.time.Clock()
        for n in range(num*5):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            framerate.tick(30)
            self.showBack()
            self.showMeat()
            self.showNum()
            screen.blit(self.right[n%12//3], (self.x, self.y))
            screen.blit(self.men, (560,440))

            self.x += 5
            pygame.display.update()
    def moveLeft(self, num=1):
        framerate = pygame.time.Clock()
        for n in range(num*5):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            framerate.tick(30)
            self.showBack()
            self.showMeat()
            self.showNum()
            screen.blit(self.left[n%12//3], (self.x, self.y))
            screen.blit(self.men, (560,440))

            self.x -= 5
            pygame.display.update()

    def say(self, sentence):
        framerate = pygame.time.Clock()
        for n in range(10):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            framerate.tick(30)
            self.showBack()
            self.showMeat()
            self.showNum()
            screen.blit(self.down[0], (self.x, self.y))
            font = pygame.font.SysFont('SimHei',18)
            imgText = font.render(sentence, True, (0,0,0), (255,255,0))
            screen.blit(imgText, (self.x+30,self.y-20))
            pygame.display.update()
        #print_text(font, self.x+30, self.y-20, sentence)

    def get(self):


        for i in range(4):
            if pygame.Rect(self.x,self.y,48,48).colliderect(self.meatRect[i]):
                self.meatNum += 1
               # print(self.meatRect[0])
                print('haha'+ str(i))
                #print(self.rect)
                self.meatPos[i] = [700,525]
        framerate = pygame.time.Clock()
        for n in range(30):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            framerate.tick(30)
            self.showBack()
            self.showMeat()
            self.showNum()
            screen.blit(self.down[2], (self.x, self.y))
            screen.blit(self.men, (560,440))
            pygame.display.update()


#if __name__ == "__main__":
pygame.init()
pygame.display.set_caption(CAPTION)
screen = pygame.display.set_mode(SCREEN_SIZE)

xm = People()
xm.show()





 # 课堂上学生需要修改的代码，注意缩进
xm.moveRight(6)
xm.moveUp(12)
xm.get()
xm.moveDown(12)


#xm.moveDown(7) 只有学生正确完成 吃鸡腿相关的for循环的修改后再取消注释

for i in range(1):
    xm.feed()

loo()
