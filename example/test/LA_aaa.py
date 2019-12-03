import pygame,random,math,sys

from pygame.locals import *
from datetime import datetime, date, time
from LA_bbb import *
from pygame import Rect

class Arrow(pygame.sprite.Sprite):
    def __init__(self, speed):
        imgR = []
        for i in range(4):
            aa = pygame.image.load('lessonA/jiantou/' + str(i+1) + '.png').convert_alpha()
            imgR.append(aa)
        imgB = []
        for i in range(4):
            aa = pygame.image.load('lessonA/jiantou/' + str(i+1)*2 + '.png').convert_alpha()
            imgB.append(aa)

        self.speed = speed
        self.x = 736
        self.y = -150
        pygame.sprite.Sprite.__init__(self)

        self.rect = Rect(self.x, self.y, 200, 200)
        self.ys = random.choice(['Red','Blue'])
        self.fx = random.randint(273,276)
        if self.fx == 273:
            self.ffx = 274
        elif self.fx == 274:
            self.ffx = 273
        elif self.fx == 275:
            self.ffx = 276
        elif self.fx == 276:
            self.ffx = 275

        if self.ys == 'Blue':
            if self.fx == 273:
                self.image = imgB[0]
            elif self.fx == 274:
                self.image = imgB[1]
            elif self.fx == 275:
                self.image = imgB[2]
            elif self.fx == 276:
                self.image = imgB[3]
        elif self.ys == 'Red':
            if self.ffx == 274:
                self.image = imgR[0]
            elif self.ffx == 273:
                self.image = imgR[1]
            elif self.ffx == 276:
                self.image = imgR[2]
            elif self.ffx == 275:
                self.image = imgR[3]
        self.last_time = 0

    def update(self, current_time, rate=0):
        if current_time > self.last_time + rate:
            self.rect.move_ip(0,self.speed)
            self.last_time = current_time
        if self.rect.top > 423:
            self.kill()
            global game
            game = 'lose'

class Human(pygame.sprite.Sprite):
    def __init__(self):

        self.x = 160
        self.y = 160
        pygame.sprite.Sprite.__init__(self)

        self.rect = Rect(self.x, self.y, 400, 400)

        self.last_time = 0
        self.img = []
        for i in range(28):
            aa = pygame.image.load('lessonA/ren2/ren' + str(i) + '.png').convert_alpha()
            self.img.append(aa)
        self.image = self.img[0]
        self.frame = 0
        self.old_frame = -1

    def update(self, current_time, rate=65):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > 27:
                self.frame = 0

            self.last_time = current_time
        if self.frame != self.old_frame:
            self.image = self.img[self.frame]
            self.old_frame = self.frame




pygame.init()
screen = pygame.display.set_mode((1120,630))
pygame.display.set_caption("aaa")

num = -1
pre_time = 0
add_num = False
score = 0
num2 = -1

group = pygame.sprite.Group()
arrowGroup = pygame.sprite.Group()

easy = pygame.image.load('lessonA/choice/easy.png').convert_alpha()
easy2 = pygame.image.load('lessonA/choice/easy2.png').convert_alpha()

normal = pygame.image.load('lessonA/choice/normal.png').convert_alpha()
normal2 = pygame.image.load('lessonA/choice/normal2.png').convert_alpha()

hard = pygame.image.load('lessonA/choice/hard.png').convert_alpha()
hard2 = pygame.image.load('lessonA/choice/hard2.png').convert_alpha()

#音乐



big1 = 0
big2 = 0
big3 = 0
finish = False

#背景
bac = pygame.image.load('lessonA/bac/bac.png').convert_alpha()

ban = pygame.image.load('lessonA/bac/ban.png').convert_alpha()

hei = pygame.image.load('lessonA/bac/hei.png').convert_alpha()

tiao = []
for i in range(11):
    aa = pygame.image.load('lessonA/tiao/' + str(i) + '.png').convert_alpha()
    tiao.append(aa)

#人
hm = Human()
group.add(hm)
win = pygame.image.load('lessonA/bac/win.png').convert_alpha()

win2 = pygame.image.load('lessonA/bac/win2.png').convert_alpha()

lose = pygame.image.load('lessonA/bac/lose.png').convert_alpha()

lose2 = pygame.image.load('lessonA/bac/lose2.png').convert_alpha()


times = pygame.time.Clock()
mode = 'easy'


while True:
    times.tick(30)
    screen.blit(bac, (0, 0))
    screen.blit(ban, (0, 0))
    screen.blit(win, (190, 170))
    screen.blit(tiao[10], (0, 0))
    screen.blit(hei, (0, 0))

    if not big1:
        screen.blit(easy, (350,100))
    else:
        screen.blit(easy2, (347,97))

    if not big2:
        screen.blit(normal, (350,250))
    else:
        screen.blit(normal2, (347,247))

    if not big3:
        screen.blit(hard, (350,400))
    else:
        screen.blit(hard2, (347, 397))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            if Rect(395,145,305,100).collidepoint(event.pos):
                #print('1')
                big1 = 1
            else:
                big1 = 0
            if Rect(395,295,305,100).collidepoint(event.pos):
                big2 = 1
            else:
                big2 = 0
            if Rect(395,445,305,100).collidepoint(event.pos):
                big3 = 1
            else:
                big3 = 0
        if event.type == MOUSEBUTTONDOWN:
            if Rect(395,145,305,100).collidepoint(event.pos):
                print(1)
                mode = 'easy'
                finish = True
            if Rect(395,295,305,100).collidepoint(event.pos):
                print(2)
                mode = 'normal'
                finish = True
            if Rect(395,445,305,100).collidepoint(event.pos):
                print(3)
                mode = 'hard'
                finish = True


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if finish:
        break
    pygame.display.update()



game = 0
speed = 5
music = 0

if mode == 'easy':
    speed = 3
    pygame.mixer.music.load('lessonA/music/flower.mp3')
elif mode == 'normal':
    speed = 5
    pygame.mixer.music.load('lessonA/music/keluo.mp3')
    #pygame.mixer.music.rewind()
    #pygame.mixer.music.set_pos(3.0)
elif mode == 'hard':
    speed = 10
    pygame.mixer.music.load('lessonA/music/bees.mp3')
tt = pygame.time.get_ticks()

#i = 0
pygame.mixer.music.play()
while True:
    #print(pygame.mixer.music.get_pos())
    #screen.fill((0,0,100))
    #print(game)
   # i += 1
    screen.blit(bac, (0,0))
    screen.blit(ban, (0, 0))
    #screen.blit(tiao, (0,0))

    ticks = pygame.time.get_ticks()

    current_time = (ticks- tt)//1000


    #print(current_time)

    if current_time%1 == 0 and add_num:
        num += 1
        a = Arrow(speed)
        group.add(a)
        arrowGroup.add(a)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            num2 += 1
            aList = arrowGroup.sprites()
            if len(aList):
                jiantou = aList[0]
                anjian = event.key
                #jiantou = jiantou.fx

                ##########################
                game, score = logic(jiantou, anjian, score, game)
                '''
                if jiantou.ys == 'Gray':
                    if anjian == jiantou.fx:
                        score += 1
                        jiantou.kill()
                        #print('score:' + str(score))

                    else:
                        #print('lose')
                        game = 'lose'
                elif jiantou.ys == 'Yellow':
                    if anjian == jiantou.ffx:
                        score += 1
                        jiantou.kill()
                        #print('score:' + str(score))
                    else:
                        #print('lose')
                        game = 'lose'
                '''

                ###########################
    if score >= 10:
        game = 'win'
    if score <= 0:
        score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if game:
        break



    if pre_time != current_time:
        add_num = True
        pre_time = current_time
    else:
        add_num = False

    group.update(ticks)
    group.draw(screen)
    screen.blit(tiao[score], (0,0))
    times.tick(30)
    pygame.display.update()

pygame.mixer.music.stop()

if game == 'lose':
    pygame.mixer.music.load('lessonA/music/lose.mp3')
elif game == 'win':
    pygame.mixer.music.load('lessonA/music/win.mp3')
pygame.mixer.music.play()

while True:

    screen.blit(bac, (0,0))
    screen.blit(ban, (0, 0))
    screen.blit(tiao[score], (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game == 'lose':
        screen.blit(lose, (190, 170))
        screen.blit(lose2, (0, 0))


    elif game == 'win':
        screen.blit(win, (190, 170))
        screen.blit(win2, (0, 0))



    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    times.tick(10)
    pygame.display.update()
