#!/usr/bin/env python3
#! -*-conding:utf-8 -*-

#!@Time   :2018/4/11 17:14
#!@Author :@liuweqia
#!@File   :class.py

import pygame,random
from pygame.locals import *
from pygame import Rect

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, property=0):
        pygame.sprite.Sprite.__init__(self)
       # self.target_surface = target
        self.x = x
        self.y = y
        self.Img = []
        if property:
            ff = pygame.image.load('lesson8/img/fireArrow.png').convert_alpha()
            self.Img.append(ff.subsurface(Rect(0,0,48,15)))
            self.Img.append(ff.subsurface(Rect(0,0,48,15)))
            self.Img.append(ff.subsurface(Rect(0,0,48,15)))
        else:
            ii = pygame.image.load('lesson8/img/iceArrow.png').convert_alpha()
            self.Img.append(ii.subsurface(Rect(0,0,48,15)))
            self.Img.append(ii.subsurface(Rect(0,0,48,15)))
            self.Img.append(ii.subsurface(Rect(0,0,48,15)))
        self.image = self.Img[0]
        self.last_time = 0
        self.property = property
        self.frame = 0
        self.old_frame = -1
        self.rect = Rect(self.x,self.y,48,15)

        self.rect.left = x
        self.rect.top = y
        #self.mask = pygame.mask.from_surface(self.image)

    def update(self, current_time, rate = 300):
        #self.x += 10
        #self.rect = Rect(self.x,self.y,48,15)
        self.rect.top = self.y
        self.rect.left += 10
        self.rect = Rect(self.rect.left,self.rect.top,48,15)

        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame >= 3:
                self.frame = 0
            self.last_time = current_time
        if self.frame != self.old_frame:
            self.image = self.Img[self.frame]
            #self.mask = pygame.mask.from_surface(self.image)
            self.old_frame = self.frame
        if self.rect.left > 1000:
            self.kill()

class Fire(pygame.sprite.Sprite):
    def __init__(self, x,y,huo,bing,property = 0):
        pygame.sprite.Sprite.__init__(self)
       # self.target_surface = target
        self.x = x
        self.y = y
        self.img = []
        self.last_time = 0
        if property == 0:
            for i in range(3):
                self.img.append(huo[i])
        else:
            self.img.append(bing)
        self.image = self.img[0]
        self.rect = Rect(self.x,self.y, 30,26)
        self.property = property
        self.frame = 0
        self.old_frame = -1

    def update(self, current_time, rate = 300):
        self.x -= 5
        self.rect = Rect(self.x,self.y, 30,26)
        if self.property == 1:
            self.image = self.img[0]
        else:
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame >= 3:
                    self.frame = 0
                self.last_time = current_time
            if self.frame != self.old_frame:
                self.image = self.img[self.frame]
                self.old_frame = self.frame

        if self.rect.left <= -20:
            self.kill()

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((width,height))
        self.rect = Rect(self.x,self.y,width,height)
        #print(self.rect)

    def update(self, current_time):
        pass

class Long(pygame.sprite.Sprite):
    def __init__(self, x, y,group):
        pygame.sprite.Sprite.__init__(self)
      #  self.target_surface = target
        self.x = x
        self.y = y
        self.group = group
        self.hp = 100
        self.huoimg = []
        self.bingimg = []

        ll1 = pygame.image.load('lesson8/img/long11.png').convert_alpha()
        ll1 = pygame.transform.smoothscale(ll1, (200,210))
        ll2 = pygame.image.load('lesson8/img/long22.png').convert_alpha()
        ll2 = pygame.transform.smoothscale(ll2, (200,210))
        ll3 = pygame.image.load('lesson8/img/long33.png').convert_alpha()
        ll3 = pygame.transform.smoothscale(ll3, (200,210))

        ll4 = pygame.image.load('lesson8/img/long44.png').convert_alpha()
        ll4 = pygame.transform.smoothscale(ll4, (200, 210))
        ll5 = pygame.image.load('lesson8/img/long55.png').convert_alpha()
        ll5 = pygame.transform.smoothscale(ll5, (200, 210))
        ll6 = pygame.image.load('lesson8/img/long66.png').convert_alpha()
        ll6 = pygame.transform.smoothscale(ll6, (200, 210))

        self.huoimg.append(ll1)
        self.huoimg.append(ll2)
        self.huoimg.append(ll1)
        self.huoimg.append(ll2)
        self.huoimg.append(ll1)
        self.huoimg.append(ll3)
        self.bingimg.append(ll4)
        self.bingimg.append(ll5)
        self.bingimg.append(ll4)
        self.bingimg.append(ll5)
        self.bingimg.append(ll4)
        self.bingimg.append(ll6)

        #self.img.append(ll2)
        self.image = ll1
        self.rect = Rect(self.x, self.y, 200, 210)
        self.last_time = 0
        self.frame = 0
        self.old_frame = -1
        self.ff = None
        self.fireGroup = []
        self.property = 0
        self.change = 0
        #创建龙喷的火与冰
        self.huo = []
        huo1 = pygame.image.load('lesson8/img/huo1.png').convert_alpha()
        huo1 = pygame.transform.smoothscale(huo1, (30,26))
        self.huo.append(huo1)
        huo2 = pygame.image.load('lesson8/img/huo2.png').convert_alpha()
        huo2 = pygame.transform.smoothscale(huo2, (30,26))
        self.huo.append(huo2)
        huo3 = pygame.image.load('lesson8/img/huo3.png').convert_alpha()
        huo3 = pygame.transform.smoothscale(huo3, (30,26))
        self.huo.append(huo3)
        self.bing = pygame.image.load('lesson8/img/bing1.png').convert_alpha()
        self.bing = pygame.transform.smoothscale(self.bing, (30,26))

    def update(self, current_time, rate = 300):
        global fireGroup
        self.rect = Rect(self.x, self.y, 200, 210)
        if current_time > self.last_time + rate:
            self.change += 1
            self.frame += 1
            if self.frame == 5:
                if self.property == 0:
                    self.ff = Fire(self.x, self.y+100,self.huo,self.bing)
                else:
                    self.ff = Fire(self.x, self.y+100,self.huo,self.bing, 1)
                    #self.property = 1
                #print(self.ff.rect)
                self.ff.add(self.group)
                self.fireGroup.append(self.ff)

            if self.frame >= 6:
                self.y = random.randint(0,420)
                self.frame = 0
            self.last_time = current_time

            if self.change >= 20:
                if self.property == 0:
                    self.property = 1
                else:
                    self.property = 0
                self.change = 0

        if self.frame != self.old_frame:
            if self.property == 0:
                self.image = self.huoimg[self.frame]
            else:
                self.image = self.bingimg[self.frame]
            self.old_frame = self.frame


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 62,90)
        self.last_time = 1
        self.frame = 0
        self.old_frame = -1
        self.direction = 0
        self.right = []
        self.gravity = 3
        self.jumping = False
        self.air = False
        self.jump_vel = -15
        self.player_start_y = self.y
        self.moveLeft = True
        self.moveRight = True
        self.moving = False
        self.shoot = False
        self.shootTime = 0
        self.hp = 100
        for i in range(4):
            aa = pygame.image.load('lesson8/img/' + str(4-i)*2 + '.png').convert_alpha()
            self.right.append(aa)
        self.left = []
        for i in range(4):
            aa = pygame.image.load('lesson8/img/' + str(4-i)*2 + '.png').convert_alpha()
            aa = pygame.transform.flip(aa,1,0)
            self.left.append(aa)
        self.shootImg = []
        aa = pygame.image.load('lesson8/img/she.png').convert_alpha()
        #aa = pygame.transform.smoothscale(aa, (79,90))
        self.shootImg.append(aa)
        self.shootImg.append(aa)
        self.up = pygame.image.load('lesson8/img/11.png').convert_alpha()
        self.stop = pygame.image.load('lesson8/img/stand.png').convert_alpha()
        self.image = self.stop


    def update(self, current_time, rate = 20):
        RIGHT = 0
        LEFT = 1
        UP = 2
        STOP = 3
        self.x = self.rect.x
        self.y = self.rect.y

        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame >= 4:
                self.frame = 0
                #self.shoot = False
            self.last_time = current_time
        if self.frame != self.old_frame:

            #print(self.shoot)
            if self.shoot:
                self.shootTime += 1
                self.image = self.shootImg[self.frame%2]
                if self.shootTime == 4:
                    self.shootTime = 0
                    self.shoot = False

            elif self.direction == RIGHT:# and self.moveRight:
                #self.image = self.right[self.frame]
                #self.x += 5
                if self.air:
                    self.image = self.up
                elif not self.moving:
                    self.image = self.stop
                elif not self.air:
                    self.image = self.right[self.frame]


                #elif not self.moving:
                #    self.image = self.stop
            elif self.direction == LEFT:# and self.moveLeft:
                #self.image = self.left[self.frame]
                #self.x -= 5
                if self.air:
                    self.image = pygame.transform.flip(self.up ,1 ,0)
                elif not self.moving:
                    self.image = pygame.transform.flip(self.stop, 1, 0)
                elif not self.air:
                    self.image = self.left[self.frame]

            elif self.direction == UP:
                self.image = self.up
            elif self.direction == STOP:
                #self.jump = 0
                self.image = self.stop
            self.old_frame = self.frame
