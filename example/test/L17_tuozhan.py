import pygame,random,math,sys
from pygame.locals import *
from datetime import datetime

def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def get(pos):
    for i in range(4):
        for j in range(4):
            if Rect(210+ 100*j, 130+ i*100, 80, 80).collidepoint(event.pos):
                print(str(i) + '   ' +   str(j))
                return i,j
    else:
        return -1, -1

#print(matrix)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("jiyi")


bac = pygame.image.load('lesson17/image/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (800,600))
kabac = pygame.image.load('lesson17/image/kaface.png').convert_alpha()
kabac = pygame.transform.smoothscale(kabac, (80,80))
#bac = pygame.image.load('image/bac.png').convert_alpha()
#bac = pygame.transform.smoothscale(bac, (800,600))

ka0 = pygame.image.load('lesson17/image/0.png').convert_alpha()
ka0 = pygame.transform.smoothscale(ka0, (80,80))
ka1 = pygame.image.load('lesson17/image/1.png').convert_alpha()
ka1 = pygame.transform.smoothscale(ka1, (80,80))
ka2 = pygame.image.load('lesson17/image/2.png').convert_alpha()
ka2 = pygame.transform.smoothscale(ka2, (80,80))
ka3 = pygame.image.load('lesson17/image/3.png').convert_alpha()
ka3 = pygame.transform.smoothscale(ka3, (80,80))
ka4 = pygame.image.load('lesson17/image/4.png').convert_alpha()
ka4 = pygame.transform.smoothscale(ka4, (80,80))
ka5 = pygame.image.load('lesson17/image/5.png').convert_alpha()
ka5 = pygame.transform.smoothscale(ka5, (80,80))
ka6 = pygame.image.load('lesson17/image/6.png').convert_alpha()
ka6 = pygame.transform.smoothscale(ka6, (80,80))
ka7 = pygame.image.load('lesson17/image/7.png').convert_alpha()
ka7 = pygame.transform.smoothscale(ka7, (80,80))
ka8 = pygame.image.load('lesson17/image/8.png').convert_alpha()
ka8 = pygame.transform.smoothscale(ka8, (80,80))
ka9 = pygame.image.load('lesson17/image/9.png').convert_alpha()
ka9 = pygame.transform.smoothscale(ka9, (80,80))



############################################ 学生可以完成的部分
'''
matrix = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

dddd = {
           0: ka0,
           1: ka1,
           2: ka2,
           3: ka3,
           4: ka4,
           5: ka5,
           6: ka6,
           7: ka7,
           8: ka8,
           9: ka9,
        }

hi = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(hi)
n = 0
for i in range(4):
    for j in range(4):
        matrix[i][j] = hi[n]
        n += 1
'''
####################################################
font1 = pygame.font.Font(None, 400)
font2 = pygame.font.Font('simhei.ttf', 200)
font3 = pygame.font.Font(None, 80)
x1 = -1
y1 = -1
x2 = -1
y2 = -1

seconds = 3
clock_start = datetime.now()
count_down = False
game_start = False
game_over = False
true_list = []
times = pygame.time.Clock()
game = ''

while not game_over:
    screen.blit(bac, (0,0))

    ########################################## 学生可以完成的部分（加载全部的背面图）
    '''
    for i in range(4):
        for j in range(4):
            if [i,j] not in true_list:
                screen.blit(kabac, (210 + j*100, 130 + i*100))
    '''
    #############################################
    if count_down:
        current = (datetime.now() - clock_start).seconds
        if seconds - current >= 1:
            print_text(font1, 250, 200, ' ' + str(int(seconds-current)),(250,246,76))
        elif seconds - current >= 0:
            print_text(font2, 100, 200, ' ' + '开始',(250,246,76))
        elif seconds-current < 0:
            game_start = True
            count_down = False
            clock_start = datetime.now()
            seconds = 20
    ##############倒计时2

    if game_start:
        current = (datetime.now() - clock_start).seconds
        if seconds-current >= 10:
            print_text(font3, 353, 43, ' ' + str(int(seconds-current)),(255,0,0))
        elif seconds-current >= 0:
            print_text(font3, 370, 43, ' ' + str(int(seconds-current)),(255,0,0))
        else:
            game_over = True
            game = 'lose'
    else:
        print_text(font3, 353, 43, ' 20',(255,0,0))
    #########################倒计时3和游戏结局

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RETURN and not count_down:
            count_down = True
            clock_start = datetime.now()

        if event.type == MOUSEBUTTONDOWN and game_start:
            if x1 < 0:
                x1, y1 = get(event.pos)
                x2, y2 = -1, -1

            elif x1 >= 0:
                x2, y2 = get(event.pos)

    #print((x1,y1,x2,y2))
    #print(aaa) 鼠标事件
######################################### 学生可以完成的部分
    '''
    if x1 >= 0:
        screen.blit(dddd[matrix[x1][y1]], (210 + 100*y1,130 + 100*x1))
    if x2 >= 0 and not [x1,y1] == [x2,y2]:
        screen.blit(dddd[matrix[x2][y2]], (210 + 100*y2,130 + 100*x2))
        pygame.display.update()
        pygame.time.delay(300)
        if matrix[x1][y1] == matrix[x2][y2]:
            matrix[x1][y1] = 0
            matrix[x2][y2] = 0

            if [x1,y1]not in true_list:
                true_list.append([x1,y1])
            if [x2,y2] not in true_list:
                true_list.append([x2,y2])
    '''
######################################################学生可以完成的部分

    x1=-1
    y1=-1
    x2=-1
    y2=-1


    if len(true_list) == 16:
        game_over = True
        game = 'win'


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    times.tick(16)
    pygame.display.update()


while True:
    screen.blit(bac, (0,0))
    for i in range(4):
        for j in range(4):
            screen.blit(dddd[random.randint(0,9)], (210 + i*100, 130 + j*100))
    if game == 'win':
        print_text(font1, 100, 200, ' ' + 'win',(255,0,0))
    elif game == 'lose':
        print_text(font1, 100, 200, ' ' + 'lose',(255,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    print(true_list)

    times.tick(2)
    pygame.display.update()
