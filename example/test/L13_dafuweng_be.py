import pygame,random,math,sys

from pygame.locals import *
from datetime import datetime, date, time
from pygame import Rect

class Dice(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.last_time = 0
        self.old_frame = -1
        #self.first_frame = 0
        self.roll = []
        for i in range(4):
            aa = pygame.image.load('lesson13/we/dice_Action_' + str(i) + '.png').convert_alpha()
            self.roll.append(aa)
        self.result = []
        for i in range(6):
            aa = pygame.image.load('lesson13/we/dice_' + str(i+1) + '.png').convert_alpha()
            self.result.append(aa)

        self.image = self.result[0]
        self.x = 600
        self.y = 400
        self.rect = Rect(self.x, self.y, 100, 100)
        self.num = 0
        self.point = random.randint(1,6)
        self.end = False

    def update(self, current_time, rate = 60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
                self.num += 1
            self.last_time = current_time
        if self.frame != self.old_frame:
            if self.num < 3:
                self.image = self.roll[self.frame]
            elif self.num >= 3 and self.num < 6:
                self.image = self.result[self.point - 1]
                #self.end = True
            elif self.num == 6 and self.frame == 0:
                self.image = self.result[self.point - 1]
                self.end = True
            else:
                self.end = False
                global roll
                roll = True

                self.kill()
            self.old_frame = self.frame



class Cowboy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.last_time = 0
        self.old_frame = -1
        #self.first_frame = 0
        self.img = []
        for i in range(4):
            aa = pygame.image.load('lesson13/pic/' + str(i+1) + '.png').convert_alpha()
            aa = pygame.transform.smoothscale(aa, (150, 225))
            self.img.append(aa)

        self.image = self.img[0]
        self.x = 50
        self.y = 330
        self.rect = Rect(self.x, self.y, 150, 225)
        self.num = 0
        self.end = False
        self.mov = 0
        self.a = 0

    def update(self, current_time, rate = 60):
        global bacx
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
                self.num += 1
            self.last_time = current_time
        if self.frame != self.old_frame:
            self.image = self.img[self.frame]
            self.old_frame = self.frame
        ####
        if self.num >= 3:
            self.mov = self.a
            self.num = 0
        destination_point = 50 + (self.mov/2)*195

        if self.rect.left < 400:
            if self.rect.left < destination_point:
                self.rect.left += 10
        else:
            #manx = 400
            if bacx > 400 - destination_point and bacx > -3105:
                bacx -= 10

            if bacx <= -3105:
                bacx = -3105

        if bacx == -3105 and cb.rect.x <= destination_point - 3105:
            #print(destination_point)
            #print(bacx)
            cb.rect.left += 10
            #print(1)
        ####
        self.x = self.rect.left

    def moved(self, point):
        self.a += point




pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Dice")
bac = pygame.image.load('lesson13/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (4105, 600))
zao2 = pygame.image.load('lesson13/zao2.png').convert_alpha()
zao2 = pygame.transform.smoothscale(zao2, (255, 600))

img = []
for i in range(4):
    aa = pygame.image.load('lesson13/pic/' + str(i+1) + '.png').convert_alpha()
    aa = pygame.transform.smoothscale(aa, (150, 225))
    img.append(aa)

group = pygame.sprite.Group()

roll = True


times = pygame.time.Clock()


bacx = 0
cb = Cowboy()
#diceNum = 0
i = 0
dice = 0

step = 0


while True:
    screen.blit(bac, (0,0))
    #print(game)
    ticks = pygame.time.get_ticks()
    i += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #dice = random.randint(1,6)
            #print(dice)
            if roll:
                dice = Dice()
                group.add(dice)
                #diceNum = dice.point
                roll = False


    ##################################
    if dice and dice.end:      #当投了骰子且骰子的动画播放结束
        print(dice.point)
        #if dice.point == 6 or dice.point==3:
            #break

    #提高：改代码写成不止为6的时候跳出循环

    ###################################



    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    #screen.fill((0,0,100))
    screen.blit(img[i%4], (50, 330))

    group.update(ticks)
    group.draw(screen)
    screen.blit(zao2, (0, 0))

    times.tick(15)
    pygame.display.update()


#将屏障升上去
for i in range(60):
    screen.blit(bac, (0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    screen.blit(img[i%4], (50, 330))

    screen.blit(zao2, (0,0- i*10))
    times.tick(15)
    pygame.display.update()



#cb = Cowboy()
group.add(cb)
dice = 0
while True:
    #print(game)
    screen.blit(bac, (bacx,0))
    ticks = pygame.time.get_ticks()
    #screen.blit(zao, (0,0))

    #diceNum = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if roll:
                dice = Dice()
                group.add(dice)
                #diceNum = dice.point
                roll = False

   # print(move)
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    #screen.blit(img[i%4], (manx, 330))
    group.update(ticks)
    group.draw(screen)
    #screen.blit(zao, (0,0))


    #############################



    '''
    if dice and dice.end:

        if dice.point == 6:
            game = 'lose'
            break
        elif dice.point == 1:
            continue

        step += dice.point
        cb.moved(dice.point)


    if step == 11 and bacx <= -1800:#当步数等于11，且背景移动到一定的位置的时候

        game = 'lose'
        break
    if step >= 20 and cb.x >= 850: #当步数大于或等于，且牛仔的横坐标大于850的时候
        game = 'win'
        break
    '''

    #############################
    times.tick(15)
    pygame.display.update()

i = 0
while True:
    if i < 10:
        i += 1
    screen.blit(bac, (bacx,0))
    ticks = pygame.time.get_ticks()
    #screen.blit(zao, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game == 'win':
        print(game)
        font3 = pygame.font.Font(None, 60 + i * 10)
        img3 = font3.render('YOU  WIN!', 1, (255, 0, 0))
        screen.blit(img3, (230, 270))
    elif game == 'lose':
        print(game)
        font2 = pygame.font.Font(None, 60 + i * 10)
        img2 = font2.render('YOU  LOSE!', 1, (255, 0, 0))
        screen.blit(img2, (210, 270))


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    times.tick(15)
    pygame.display.update()
