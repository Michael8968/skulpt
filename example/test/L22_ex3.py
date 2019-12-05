import pygame,random,sys
from pygame.locals import *
from pygame import Rect


##### 任务3
# 按下向下的箭头，小人跳过障碍


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("No One Die")
times = pygame.time.Clock()


img = []
for i in range(5):
    aa = pygame.image.load('lesson22/noOneToDie/h' + str(i+1) + '.png').convert_alpha()
    img.append(aa)

######### PPT 9 练习 ###########

jump = 0
high = 0
can_jump = True

######### PPT 9 练习 ###########

n = 0
rect_list = []
rectx = 0
recty = 0
random_time = 0

while True:
    times.tick(30)
    screen.fill((255,255,255))

    man_rect = Rect(40, 363 -high, 35, 60) #小人外接框，看的更清楚
    n += 1
    screen.blit(img[n%5], (30, 363-high))       # 小人图片，代码需要做修改
    pygame.draw.rect(screen, (0,0,0), (0, 420, 800, 5))
    pygame.draw.rect(screen, (255,0,0), man_rect, 1) #画出小人外接框


    if random_time == 0:
        random_time = random.randint(110,150)
        rectx = random.randint(10,25)
        recty = random.randint(30,45)
        rect_l = [800, 420-recty, rectx, recty]
        rect_list.append(rect_l)
    else:
        random_time -= 1


    for r in rect_list:
        pygame.draw.rect(screen, (0,0,0), r)
        r[0] -= 6

######### PPT 9 练习 ###########
    '''
    high += jump

    if high >= 160:
        jump = - jump
    elif high < 0:
        high = 0
        jump = 0
        can_jump = True


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if can_jump:
                    jump = 10
                    high = 0
                    can_jump = False
    print(jump)
    print(high)
##### 以上是匀速上升下降的代码
##### 以下是非匀速上升下降的代码 PPT 14-16 拓展部分

    high = high + jump
    jump -= 3

    if high <= 0:
        high = 0
        jump = 0
        can_jump = True

    for r in rect_list:
        r[0] -= 6

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if can_jump:
                    jump = 30
                    high = 0
                    can_jump = False

    '''


######### PPT 9 练习 ###########

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update()
