import sys, random, time, pygame
from pygame.locals import *
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()
num = 0
flag = 0

x = 300
y = 350
words_list = [['老虎', '狮子', '蛇', '蛤蟆', '老鼠', '蜘蛛'],
              ['丑', '可爱', '美丽', '凶猛', '勤劳', '警觉'],
              ['头', '翅膀', '脚趾', '嘴巴', '鼻子', '眼睛'],
              ['小猫', '小狗', '金鱼', '熊猫', '兔子', '鹦鹉'],
              ['脸', '手臂', '毛发', '四肢', '触角', '尾巴'],
              ['鸡腿', '薯片', '火锅', '饺子', '苹果', '西瓜'],
              ['跑', '走', '跳', '散步', '躺下', '蹲下']]

long1 = pygame.image.load('lesson2/long1.png').convert_alpha()
long1 = pygame.transform.smoothscale(long1, (x,y))
pillar = pygame.image.load('lesson2/pillar.png').convert_alpha()
pillar = pygame.transform.smoothscale(pillar, (340,600))
bbb = pygame.image.load('lesson2/bbb.png').convert_alpha()
bbb = pygame.transform.smoothscale(bbb, (800,600))
st = pygame.image.load('lesson2/st.png').convert_alpha()
st = pygame.transform.smoothscale(st, (120,60))
st2 = pygame.transform.smoothscale(st, (130,70))
#st = pygame.transform.rotate(st, 20)
long2 = pygame.image.load('lesson2/long2.png').convert_alpha()
long2 = pygame.transform.smoothscale(long2, (180,180))
ren = pygame.image.load('lesson2/ren.png').convert_alpha()
ren = pygame.transform.smoothscale(ren, (60,60))
re = pygame.image.load('lesson2/re.png').convert_alpha()
re = pygame.transform.smoothscale(re, (120,60))
re2 = pygame.transform.smoothscale(re, (130,70))


def showText(string):
    font = pygame.font.Font('simhei.ttf', 25)
    global screen
    global num

    if len(string) <= 23:
        if num < len(string):
            num += 1
            imgText = font.render(string[0:num], True, (160,82,45))
            screen.blit(imgText, (120, 175))
        else:
            num = len(string)
            imgText = font.render(string[0:num], True, (160,82,45))
            screen.blit(imgText, (120, 175))
    elif len(string) <= 46:
        if num < 23:
            num += 1
            imgText = font.render(string[0:num], True, (160,82,45))
            screen.blit(imgText, (120, 175))
        elif num >= 23 and num < len(string):
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            num += 1
            imgText2 = font.render(string[23:num], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
        else:
            num = len(string)
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            imgText2 = font.render(string[23:num], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
    elif len(string) <= 69:
        if num < 23:
            num += 1
            imgText = font.render(string[0:num], True, (160,82,45))
            screen.blit(imgText, (120, 175))
        elif num >= 23 and num < 46:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            num += 1
            imgText2 = font.render(string[23:num], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
        elif num >= 46 and num < 69:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            imgText2 = font.render(string[23:46], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
            num += 1
            imgText3 = font.render(string[46:num], True, (160,82,45))
            screen.blit(imgText3, (120, 235))
        else:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            imgText2 = font.render(string[23:46], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
            num = len(string)
            imgText3 = font.render(string[46:num], True, (160,82,45))
            screen.blit(imgText3, (120, 235))
    elif len(string) <= 92:
        if num < 23:
            num += 1
            imgText = font.render(string[0:num], True, (160,82,45))
            screen.blit(imgText, (120, 175))
        elif num >=23 and num < 46:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            num += 1
            imgText2 = font.render(string[23:num], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
        elif num >= 46 and num < 69:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            imgText2 = font.render(string[23:46], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
            num += 1
            imgText3 = font.render(string[46:num], True, (160,82,45))
            screen.blit(imgText3, (120, 235))
        elif num >= 69 and num < 92:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            imgText2 = font.render(string[23:46], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
            imgText3 = font.render(string[46:69], True, (160,82,45))
            screen.blit(imgText3, (120, 235))
            num += 1
            imgText4 = font.render(string[69:num], True, (160,82,45))
            screen.blit(imgText4, (120, 265))
        else:
            imgText = font.render(string[0:23], True, (160,82,45))
            screen.blit(imgText, (120, 175))
            imgText2 = font.render(string[23:46], True, (160,82,45))
            screen.blit(imgText2, (120, 205))
            imgText3 = font.render(string[46:69], True, (160,82,45))
            screen.blit(imgText3, (120, 235))
            num = len(string)
            imgText4 = font.render(string[69:num], True, (160,82,45))
            screen.blit(imgText4, (120, 265))


def showbac():
    global bacNum
    global bac
    global animal
    global animal2
    global adj
    global body
    global body2
    global food
    global act
    global movex
    global big
    global flag

    if bacNum == 0:

        screen.blit(bac[bacNum],(0,0))
        screen.blit(long1,(240,160))

        screen.blit(bbb,(movex+30,0))
        screen.blit(pillar,(movex,0))
        if movex == 675:
            if not big:
                screen.blit(st,(550,430))
            else:
                screen.blit(st2,(545,425))
            #print(st.get_rect())

    elif bacNum == 1:
        screen.blit(bac[bacNum],(0,0))
    elif bacNum == 2:
        screen.blit(bac[bacNum],(0,0))
        font = pygame.font.Font('simhei.ttf',38)
        string = animal + '是世界上最' + adj + '的动物,他们有' + body +'和长得像'\
            + animal2 +'的' + body2 + '。它喜欢吃' + food \
            + ',如果你遇上了它们千万记住要' + act + '，否则你就会被吃掉！'
        showText(string)
        flag += 1
        if flag%6 == 0 or flag%6 == 1 or flag%6 == 2:
            screen.blit(long2,(120,350))
            screen.blit(ren, (370, 460))

        elif flag%6 == 3 or flag%6 == 4 or flag%6 == 5:
            screen.blit(long2,(140,350))
            screen.blit(ren, (350, 460))
        if not big:
            screen.blit(re,(550,430))
        else:
            screen.blit(re2,(545,425))


def get_key():
    while 1:
        time.sleep(0.2)
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        elif event.type == QUIT:
            pygame.quit()
        else:
            pass

def display_box(screen, message):
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font('simhei.ttf',18)
    pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 100,
                                      (screen.get_height() / 2) - 10,
                                      200,20), 0)
    pygame.draw.rect(screen, (0,0,0),((screen.get_width() / 2) - 102,
                                            (screen.get_height() / 2) - 12,
                                            204,24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (0,0,0)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.update()

def ask(screen, question,num_question):
    "ask(screen, question) -> answer"
    showbac()
    pygame.font.init()
    current_string = []
    fontobject = pygame.font.Font('simhei.ttf',38)
    screen.blit(fontobject.render(question, 1, (0,0,0)),(295, 200))
    fon = pygame.font.Font('simhei.ttf',16)
    screen.blit(fon.render('(从下方给出的内容里选择一个并输入对应的拼音)',1,(255,0,0)),(295,235))
    screen.blit(fon.render('1.输入拼音，如"laohu"，"shizi"。',1,(210,105,30)),(295,400))
    screen.blit(fon.render('2.输入正确的拼音后敲击回车会出现对应的中文。',1,(210,105,30)),(295,420))
    #screen.blit(fon.render('  输入拼音，如果是多个字，拼音间用空格隔开，如"li zi"，"pin yin"。',1,(210,105,30)),(100,400))
    #screen.blit(fon.render('  输入拼音后敲击回车会出现中文，使用键盘上下键可进行选择。',1,(210,105,30)),(100,420))
    screen.blit(fon.render('3.确定了想要的中文单词，再敲击回车即可。',1,(210,105,30)),(295,440))
    fon2 = pygame.font.Font('simhei.ttf',55)
    screen.blit(fon2.render('回答问题',1,(139,69,19)),(355,100))
    words = words_list[num_question]
    for i in range(len(words)):
        screen.blit(fontobject.render(words[i], 1, (0,0,0)),(295+i*40, 310))

    display_box(screen, ''.join(current_string))
    num = 0
    result = {}
    while 1:

        inkey = get_key()
        print(inkey)
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
            display_box(screen, ''.join(current_string))
        elif len(result) == 0 and inkey == K_RETURN:
            string = ''.join(current_string)
            lis = string.split(' ')
            result = dag(dagparams, lis, 3)
            display_box(screen, ''.join(result[num].path))
            print(''.join(result[0].path))
        elif len(result) and inkey == K_RETURN:
            hanzi = ''.join(result[num].path)
            break
        elif len(result) and inkey == K_DOWN:
            num += 1
            if num >= 3:
                num = 2
            display_box(screen, ''.join(result[num].path))
        elif len(result) and inkey == K_UP:
            num -= 1
            if num <= -1:
                num = 0
            display_box(screen, ''.join(result[num].path))
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
            display_box(screen, ''.join(current_string))

    return hanzi












pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("maoxian")

#背景
bac = []
bacNum = 0
bac1 = pygame.image.load('lesson2/bac.png').convert_alpha()
bac1 = pygame.transform.smoothscale(bac1, (800,600))
bac2 = pygame.image.load('lesson2/middle.png').convert_alpha()
bac2 = pygame.transform.smoothscale(bac2, (800,600))
bac3 = pygame.image.load('lesson2/bac.png').convert_alpha()
bac3 = pygame.transform.smoothscale(bac3, (800,600))
bac.append(bac1)
bac.append(bac2)
bac.append(bac3)

showquiz = 0
movex = 200
framerate = pygame.time.Clock()
big = 0

while True:
    keys = pygame.key.get_pressed()
    #screen.fill((100,100,100))
    pygame.draw.rect(screen,(100,100,100),(0,0,800,600))
    if movex < 675:
        movex += 5
       # print(1)
    else:
        movex = 675
    showbac()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if bacNum == 0 and event.type == MOUSEMOTION:
            #mouse_x,mouse_y = event.pos
            if pygame.Rect(550,430,120,60).collidepoint(event.pos):
                #print('peng')
                big = 1
            else:
                big = 0
        #if 鼠标在特定位置且点击
        #更改背景，调用回答问题函数
        if bacNum == 0 and event.type == MOUSEBUTTONDOWN and pygame.Rect(550,430,120,60).collidepoint(event.pos):
            bacNum = 1
            showquiz = 1
            print(1)
        if bacNum == 2 and event.type == MOUSEMOTION:
            #mouse_x,mouse_y = event.pos
            if pygame.Rect(550,430,120,60).collidepoint(event.pos):
                #print('peng')
                big = 1
            else:
                big = 0
        if bacNum == 2 and event.type == MOUSEBUTTONDOWN and pygame.Rect(550,430,120,60).collidepoint(event.pos):
            bacNum = 0
            num = 0
            print(1)
        #if 回答问题结束
        #更改背景，进入结尾，调用结尾函数


    if keys[K_ESCAPE]:
        pygame.quit()

    if showquiz == 1:
        showbac()
        print(2)
        animal = ask(screen, "写下你不喜欢的动物", 0)
        adj = ask(screen, '写下一个形容词', 1)
        body = ask(screen, '写下你最喜欢的身体部位', 2)
        animal2 = ask(screen, '写你喜欢的一种动物', 3)
        body2 = ask(screen, '再写下一个身体部位', 4)
        food = ask(screen, '写下你喜欢的食物', 5)
        act = ask(screen, '写下一个动作', 6)
        bacNum = 2
        showquiz = 0

    framerate.tick(10)
    pygame.display.update()
