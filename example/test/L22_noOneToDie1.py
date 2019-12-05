import pygame,random,sys
from pygame.locals import *
from pygame import Rect

##########################
#一个都不能死游戏的设计思路
#首先分析游戏逻辑：  1）画面中有个小人一直在原地跑
#                 2）会有障碍物从右边出现并往左边移动
#                 3）按下按键后小人会向上跳起，可躲避障碍物
#                 4）如小人不能及时躲避障碍物，则游戏结束，如躲避了一个障碍物，则加一分
#                 5）多个小人版也只是将上面的逻辑实现多份而已
####
#然后开始设计
#1. 画出地上的线
#2. 画出小人的图片并使其跑起来
#3. 画出障碍物：1）障碍物出现的时间随机
#              2）障碍物的大小随机
#              3）障碍物有多个且都向左移动
#4. 实现小人的跳起动作：1）跳起时并不是每帧移动相同距离的
#                      **2）向上时每帧的移动距离逐渐减小，一直到最顶点的时候移动距离为0，然后再反方向移动  *我们使用jump来作为每帧移动的距离 使用high来表示距离地面的距离
#                      3）我们如果不限制什么时候可以跳，则会造成可以连跳的情况所以要加入一个变量，控制落地的情况才可以跳， *我们使用can_jump变量
#
#5. 实现小人跟障碍物间的碰撞及碰撞后游戏结束的画面
#6. 实现加分
#7. 实现重置游戏
#改成双人版的
#1. 双人版其实就是把各种变量，各种逻辑程序块給复制一遍然后做些数值上跟变量名上的修改
#2. 可以将重复的程序块做成函数，这样只要调用两次就行了，可以简化代码    *noOneToDieDef.py文件实现了各个函数

# noOneToDie1.py 是一个小人的没函数化版
# noOneToDie2.py 是两个小人的没函数化版
# noOneToDie3.py 是三个小人的没函数化版
# noOneToDieDef.py 是三个小人的函数化过程版
# noOneToDieDef2.py 是三个小人的函数化完成版
# aaaaa.py 是三个小人的函数化的拆分版， 拆分出来的函数放在aaaaadef.py
# aaaaa2.py 是两个小人的函数化的拆分版， 函数文件还是aaaaadef.py

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("No One Die")


def showScore():
    SFont = pygame.font.Font(None, 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, (0,0,0))
    screen.blit(Ssurf, (350,10))
def showEnd():
    font = pygame.font.Font(None, 88)
    fontimg = font.render('game over', True, (255,0,0))
    screen.blit(fontimg, (250,250))
    fontimg2 = font.render('press return to restart', True, (255,0,0))
    screen.blit(fontimg2, (100,350))

img = []
for i in range(5):
    aa = pygame.image.load('lesson22/noOneToDie/h' + str(i+1) + '.png').convert_alpha()
    img.append(aa)# 加载人物运动的图

times = pygame.time.Clock()

jump = 0
high = 0
n = 0
can_jump = True

rect_list = []
rectx = 0
recty = 0
score = 0
random_time = 0

gameover = False

while True:
    times.tick(30)
    screen.fill((255,255,255))
    man_rect = Rect(40, 363 -high, 35, 60) #小人外接框框
    #print(man_rect)

    if random_time == 0:         #控制障碍物的大小跟出现时间
        random_time = random.randint(110,150)
        rectx = random.randint(10,25)
        recty = random.randint(30,45)
        rect_l = [800, 420-recty, rectx, recty]
        rect_list.append(rect_l)
    else:
        random_time -= 1

    n += 1
    screen.blit(img[n%5], (30, 363 - high))       # 小人图片
    pygame.draw.rect(screen, (255,0,0), man_rect, 1)    # 辅助教学用，画出碰撞的矩形轮廓
    pygame.draw.rect(screen, (0,0,0), (0, 420, 800, 5))   # 地上黑线

    for r in rect_list:                    #画出所有障碍物
        pygame.draw.rect(screen, (0,0,0), r)
        if man_rect.colliderect(Rect(r[0],r[1],r[2],r[3])):      #如果小人碰到障碍物则游戏结束
            gameover = True
        if r[0] <= -30:                       # 如果障碍物从画布左边出去了， 则加一分，随之将该障碍物从障碍物列表中消除
            score += 1

            rect_list.remove(r)


    for r in rect_list:   # 控制障碍物向左移动
        r[0] -= 6

    if jump > -24:
        jump -= 2

    if high >= 24:
        high += jump
    else:
        can_jump = True # 跳跃方面的

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if can_jump:
                    jump = 24
                    high = 24
                    can_jump = False
    print(high)
    showScore()
    if gameover:
        showEnd()
        #  下面这个循环的作用是将游戏界面停止在死亡的那一刻，是游戏循环不再进行，当按下回车的时候重置游戏参数，回到原来的游戏循环
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
