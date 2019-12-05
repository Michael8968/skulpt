import pygame,random,sys
from pygame.locals import *



##### 任务2 障碍物
#1. 障碍出现的时间随机
#2. 障碍的大小在一定范围内随机
#3. 障碍物有多个而且都向左移动

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("No One Die")
times = pygame.time.Clock()


img = []
for i in range(5):
    aa = pygame.image.load('lesson22/noOneToDie/h' + str(i+1) + '.png').convert_alpha()
    img.append(aa)

n = 0

######## PPT 6 练习 ##########
'''
rect_list = []
rectx = 0
recty = 0
random_time = 0
'''
######## PPT 6 练习 ##########

while True:
    times.tick(30)
    screen.fill((255,255,255))


    n += 1
    screen.blit(img[n%5], (30, 363))       # 小人图片
    pygame.draw.rect(screen, (0,0,0), (0, 420, 800, 5))   # 地上黑线

####################### PPT 6 练习 ##################
    '''
    if random_time == 0:         #控制障碍物的大小跟出现时间
        random_time = random.randint(110,150)
        rectx = random.randint(10,25)
        recty = random.randint(30,45)
        rect_l = [800, 420-recty, rectx, recty]
        rect_list.append(rect_l)
    else:
        random_time -= 1


    for r in rect_list:                    #画出所有障碍物
        pygame.draw.rect(screen, (0,0,0), r)
        r[0] -= 6

    print(rect_list)
    '''
####################### PPT 6 练习 ##################

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update()
