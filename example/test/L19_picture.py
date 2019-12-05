import pygame,sys,random
from pygame.locals import *

#将0-800转成0-255的函数
def transform(mousex):
    mousex = 255 - mousex/700*255
    return mousex

def sun(screen):
    screen.blit(pic1, (500,40))
    screen.blit(pic2, (500+10,50))
    screen.blit(pic3, (500+20,60))
    screen.blit(pic4, (500+30,70))
#带参数的sun()函数
'''
def sun(screen,x,y):
    pic = pygame.image.load('lesson19/sun.png')#.convert_alpha()
    pic1 = pygame.transform.smoothscale(pic, (160,160))
    pic2 = pygame.transform.smoothscale(pic, (140,140))
    pic3 = pygame.transform.smoothscale(pic, (120,120))
    pic4 = pygame.image.load('lesson19/sun2.png')#.convert_alpha()
    pic4 = pygame.transform.smoothscale(pic4, (100,100))
    screen.blit(pic1, (x,y))
    screen.blit(pic2, (x+10,y+10))
    screen.blit(pic3, (x+20,y+20))
    screen.blit(pic4, (x+30,y+30))
'''



'''
def building(screen,width, height, x, y):                        #已弃用
    suf = pygame.Surface((width, height))
    suf.fill((0,0,0))
    suf.set_alpha(80)
    windows_width = (width-5)/5 -5
    windows_height = (height-10)/6 -10
    for i in range(5):
        for j in range(6):
            if random.choice((0,1)):
                pygame.draw.rect(suf, (130,130,130), (5 + i*(windows_width+5),
                                10 + j*(windows_width+10),windows_width,windows_width))


    screen.blit(suf, (x, y))
'''

def stars(screen,poslist):
    for pos in poslist:
        if random.choice((0,1)):
            pygame.draw.rect(screen, (200,255,255), (pos[0],pos[1],2,2))


def snow(screen,snowy):
    screen.blit(snow1, (0, snowy))
    screen.blit(snow2, (0, snowy-700))


def bridge(screen):
    pygame.draw.rect(screen, (190,190,190), (0, 496, 700, 2))
    pygame.draw.rect(screen, (0,0,0), (0, 498, 700, 6))
    pygame.draw.rect(screen, (0,0,0), (0, 525, 700, 26))
    for i in range(27):
        pygame.draw.rect(screen, (0,0,0), (i*25+25, 500, 6, 25))


def car(screen,carx):
    pygame.draw.rect(screen, (40,40,40), (carx, 513, 35, 12))
    #pygame.draw.rect(screen, (190,190,190), (carx, 512, 35, 1))
    #pygame.draw.rect(screen, (255,255,255), (carx+33, 513+6, 2, 3))

######岸边
def ground(screen):
    pygame.draw.rect(screen, (200,250,250), (0,680,700,200))
    pygame.draw.rect(screen, (180,200,200), (0, 585, 700, 13))

    pygame.draw.ellipse(screen, (0,0,0), (-80,570,250,100))
    pygame.draw.ellipse(screen, (0,0,0), (-20,585,250,50))
    pygame.draw.ellipse(screen, (0,0,0), (290,595,140,60))
    pygame.draw.ellipse(screen, (0,0,0), (550,580,100,40))
    pygame.draw.ellipse(screen, (0,0,0), (500,580,100,20))
    pygame.draw.ellipse(screen, (0,0,0), (640,580,180,110))

    pygame.draw.ellipse(screen, (150,150,150), (400,580,130,1))
    pygame.draw.ellipse(screen, (150,150,150), (600,590,100,1))
    pygame.draw.ellipse(screen, (150,150,150), (140,580,100,1))
    pygame.draw.ellipse(screen, (255,255,255), (360,630+40,100,10))
    pygame.draw.ellipse(screen, (255,255,255), (400,650+40,60,1))
######水面反映
def ref(screen):
    reflection = pygame.Surface((700, 200))
    reflection.fill((171,198,198))
    #reflection.set_alpha(120)
    screen.blit(reflection, (0,580))

def game():
    pygame.display.set_caption("picture")
    times = pygame.time.Clock()
    poslist = []
    print(transform(600))
    x = 100
    mousex = 100
    snowy = 0
    carx = 0
    while True:
        carx += 6
        if carx >= 700:
            carx = 0
        snowy += 2
        if snowy == 700:
            snowy = 0
        times.tick(24)
        screen.fill((x,73,100))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                poslist.append(event.pos)

        stars(screen,poslist)
        sun(screen)
        car(screen,carx)
        car(screen,carx - 60)
        #car(carx + 60)
        pygame.draw.circle(screen, (x,73,100), (mousex,120), 47)  #移动的圆形阴影
        ground(screen)
        ref(screen)
        bridge(screen)
        snow(screen,snowy)

        ####################水面岸边的雪
        pygame.draw.ellipse(screen, (255,255,255), (-100,720,400,100))
        pygame.draw.ellipse(screen,(255,255,255), (-175,680,350,100))
        mousex,y = pygame.mouse.get_pos()    #获取当前鼠标坐标点
        x = transform(mousex)
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
        pygame.display.update()




pygame.init()
screen = pygame.display.set_mode((700, 700),NOFRAME)
pic = pygame.image.load('lesson19/sun.png')#.convert_alpha()
pic1 = pygame.transform.smoothscale(pic, (160,160))
pic2 = pygame.transform.smoothscale(pic, (140,140))
pic3 = pygame.transform.smoothscale(pic, (120,120))
pic4 = pygame.image.load('lesson19/sun2.png').convert_alpha()
pic4 = pygame.transform.smoothscale(pic4, (100,100))
snow1 = pygame.image.load('lesson19/snow.png').convert_alpha()
snow2 = snow1


game()
