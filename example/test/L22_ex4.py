import pygame,random,sys
from pygame.locals import *



##### 任务4
# 碰撞障碍物游戏结束 + 游戏结束画面
# 分数系统 + 显示
# 按下enter键游戏重置

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("No One Die")
times = pygame.time.Clock()

########### PPT 18  练习 （代码增添和修改）#################
'''
def showScore():
    SFont = pygame.font.Font(None, 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, (0,0,0))
    screen.blit(Ssurf, (350,10))
def showEnd():
    font = pygame.font.Font(None, 88)
    fontimg = font.render('game over', True, (255,0,0))
    screen.blit(fontimg, (250,250))
'''
########### PPT 18  练习 （代码增添和修改）#################


img = []
for i in range(5):
    aa = pygame.image.load('lesson22/noOneToDie/h' + str(i+1) + '.png').convert_alpha()
    img.append(aa)



jump = 0
high = 0
can_jump = True
n = 0
rect_list = []
rectx = 0
recty = 0
random_time = 0


########### PPT 18  练习 （代码增添和修改）#################
'''
score = 0
gameover = False
'''
########### PPT 18  练习 （代码增添和修改）#################


while True:
    times.tick(30)
    screen.fill((255,255,255))

    man_rect = Rect(40, 363 -high, 35, 60)
    n += 1
    screen.blit(img[n%5], (30, 363-high))
    pygame.draw.rect(screen, (0,0,0), (0, 420, 800, 5))
    pygame.draw.rect(screen, (255,0,0), man_rect, 1)


    if random_time == 0:
        random_time = random.randint(110,150)
        rectx = random.randint(10,25)
        recty = random.randint(30,45)
        rect_l = [800, 420-recty, rectx, recty]
        rect_list.append(rect_l)
    else:
        random_time -= 1


########### PPT 18  练习 （代码增添和修改）#################
'''
    for r in rect_list:                    #画出所有障碍物
        pygame.draw.rect(screen, (0,0,0), r)
        r[0] -= 6
        if man_rect.colliderect(Rect(r)):      #如果小人碰到障碍物则游戏结束
            gameover = True
        if r[0] <= -30:                       # 如果障碍物从画布左边出去了， 则加一分，随之将该障碍物从障碍物列表中消除
            score += 1
            rect_list.remove(r) # 如果不加入这一行代码，跳过第一个障碍物之后会一直显示加分
'''

########### PPT 18  练习 （代码增添和修改）#################


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
            sys.exit()


        if event.type == KEYDOWN:
            if event.key == K_UP:
                if can_jump:
                    jump = 30
                    high = 0
                    can_jump = False

    showScore()
    if gameover:
        showEnd()

######################### PPT 18 游戏重置 #############
        '''
        while True:
            times.tick(10)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    jump = 0
                    high = 0
                    n = 0
                    rect_list = []
                    rectx = 0
                    recty = 0
                    random_time = 0
                    can_jump = True
                    gameover = False
                    score = 0
                    break
        '''
######################### PPT 18 游戏重置 #############

            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update()
