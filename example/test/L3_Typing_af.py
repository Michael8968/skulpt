import sys, random, time, pygame
from pygame.locals import *
import L3_Setting_af
import time

def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("typing game")
font1 = pygame.font.Font(None, 100) #倒计时
font2 = pygame.font.Font(None, 180) #大字母
font3 = pygame.font.Font(None, 90) #得分
font4 = pygame.font.Font('simhei.ttf', 22) #游戏规则

white = 255,255,255
key_flag = False
correct_answer = 97 #"a"
seconds = 31
score = 0
clock_start = 0
game_over = True

back = pygame.image.load('lesson3/back.png').convert_alpha()
back = pygame.transform.smoothscale(back, (1000,600))
docNor = pygame.image.load('lesson3/normal.png').convert_alpha()
docNor = pygame.transform.smoothscale(docNor, (180,240))
docSmill = pygame.image.load('lesson3/smill.png').convert_alpha()
docSmill = pygame.transform.smoothscale(docSmill, (180,240))
docMad = pygame.image.load('lesson3/wrong.png').convert_alpha()
docMad = pygame.transform.smoothscale(docMad, (180,240))
setx, sety = L3_Setting_af.setpos()
docFlag = 0  #0是normal，1是smile, 2是mad(wrong)
count = 0

while True:
    time.sleep(0.01)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key != correct_answer and not game_over:
            print(correct_answer)
            docFlag = 2

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 31
            r,g,b = L3_Setting_af.setcolor()

        clock_start = time.clock()
    current = time.clock() - clock_start
    speed = score * 2
    if seconds-current < 0:
        game_over = True
    elif current <= 30:
        if keys[correct_answer] and not game_over:
            correct_answer = random.randint(97,122)
            score += 1
            setx,sety = L3_Setting_af.setpos()
            docFlag = 1
            r,g,b = L3_Setting_af.setcolor()

    screen.blit(back, (0,0))


    #切换三个图片
    if docFlag == 0:
        screen.blit(docNor, (670,180))
        r,g,b=L3_Setting_af.setcolor()
        color=r,g,b
    elif docFlag == 1:
        screen.blit(docSmill, (670,180))
        r,g,b=L3_Setting_af.setcolor()
        color=r,g,b
    elif docFlag == 2:#如果输入的字母是错误的
        screen.blit(docMad, (670,180))
        r=200
        g=0
        b=0
        color=r,g,b
        #课堂练习3（黑色变成红色）




    if docFlag != 0:  # 让smill跟wrong图片停留一段时间
        count +=1
        if count == 90:
            count = 0
            docFlag = 0

    #显示倒计时
    if game_over:
        # print_text(font1, 0, 160, "Press Enter to start...")
        print_text(font1, 65, 53, '30')
    if not game_over:
        #字母颜色变化
        if r <= 225 and g <= 225 and b <= 225:
            r += random.randint(15,20)/100
            g += random.randint(15,20)/100
            b += random.randint(15,20)/100
        else:
            r = 205
            g = 205
            b = 155
        color = r,g,b

        if int(seconds-current) >=10:
            print_text(font1, 65, 53, str(int(seconds-current)))
        else:
            print_text(font1, 65, 53, ' ' + str(int(seconds-current)),(255,0,0))
        # print_text(font1, 0, 80, "Time: " + str(int(seconds-current)))

    #显示得分
    if speed < 10:
        speedStr = ' ' + str(speed)
    else:
        speedStr = str(speed)
    print_text(font3, 760, 110, speedStr)

    #显示大字母
    print_text(font2, setx, sety, chr(correct_answer-32), color)
    #显示游戏说明
    print_text(font4, 220, 450, '       游戏规则：按下Enter键开始游戏')
    print_text(font4, 220, 480, '                 在键盘上敲下你看到的字母')
    print_text(font4, 220, 510, '                 看你能够得到多少分')


    pygame.display.update()
