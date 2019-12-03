import os
import sys
import pygame
import time
from pygame.locals import *

CAPTION = "Rescue Xiaomeng"
SCREEN_SIZE = (800, 600)
pygame.init()
pygame.display.set_caption(CAPTION)
screen = pygame.display.set_mode(SCREEN_SIZE)


def loo():
    while True:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


class People(object):
    def __init__(self):
        self.x = 380
        self.y = 230
        self.up = pygame.image.load('lesson1/up.png').convert_alpha()
        self.up = pygame.transform.smoothscale(self.up, (30,40))
        self.down = pygame.image.load('lesson1/down.png').convert_alpha()
        self.down = pygame.transform.smoothscale(self.down, (30,40))
        self.left = pygame.image.load('lesson1/left.png').convert_alpha()
        self.left = pygame.transform.smoothscale(self.left, (30,40))
        self.right = pygame.image.load('lesson1/right.png').convert_alpha()
        self.right = pygame.transform.smoothscale(self.right, (30,40))

        self.bac1 = pygame.image.load('lesson1/back.png').convert_alpha()
        self.bac1 = pygame.transform.smoothscale(self.bac1, (800,600))
        self.bac2 = pygame.image.load('lesson1/map.png').convert_alpha()
        self.bac2 = pygame.transform.smoothscale(self.bac2, (800,600))
        self.start = pygame.image.load('lesson1/start.png').convert_alpha()
        self.start = pygame.transform.smoothscale(self.start, (50,60))
        self.end = pygame.image.load('lesson1/end.png').convert_alpha()
        self.end = pygame.transform.smoothscale(self.end, (50,60))

    def showBac(self):
        screen.blit(self.bac1, (0,0))
        screen.blit(self.bac2, (0,0))
        screen.blit(self.start, (300,130))
        screen.blit(self.end, (550,500))

    def show(self):
        framerate = pygame.time.Clock()
        for n in range(30):
            framerate.tick(30)
            self.showBac()
            screen.blit(self.down, (self.x, self.y))
            pygame.display.update()

    def moveUp(self, num=1):

        framerate = pygame.time.Clock()
        for n in range(num*5):
            framerate.tick(30)
            self.showBac()
            if n%4 == 0:
                screen.blit(self.up, (self.x, self.y))
            else:
                screen.blit(self.up, (self.x, self.y-5))
            self.y -= 5
            pygame.display.update()

            #fpsClock.tick(FPS)
    def moveDown(self, num=1):
        framerate = pygame.time.Clock()
        for n in range(num*5):
            framerate.tick(30)
            self.showBac()
            if n%4 == 0:
                screen.blit(self.down, (self.x, self.y))
            else:
                screen.blit(self.down, (self.x, self.y-5))
            self.y += 5
            pygame.display.update()
    def moveRight(self, num=1):
        framerate = pygame.time.Clock()
        for n in range(num*5):
            framerate.tick(30)
            self.showBac()
            if n%4 == 0:
                screen.blit(self.right, (self.x, self.y))
            else:
                screen.blit(self.right, (self.x, self.y-5))
            self.x += 5
            pygame.display.update()
    def moveLeft(self, num=1):
        framerate = pygame.time.Clock()
        for n in range(num*5):
            framerate.tick(30)
            self.showBac()
            if n%4 == 0:
                screen.blit(self.left, (self.x, self.y))
            else:
                screen.blit(self.left, (self.x, self.y-5))
            self.x -= 5
            pygame.display.update()

xm = People()
xm.show()

def run():

    xm.moveRight(3)
    xm.moveDown(3)
    xm.moveLeft(9)
    xm.moveDown(3)
    xm.moveRight(11)
    xm.moveDown(7)



    loo()
run()
