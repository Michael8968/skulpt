import pygame,re
from pygame.locals import *
from pygame import Rect

rc = re.compile(r'd\[-?\d{,2}:-?\d{,2}:?-?\d{,2}\]')
pygame.init()
screen = pygame.display.set_mode((650, 800))
pygame.display.set_caption("qiepian")
clock = pygame.time.Clock()

def get_key():
    while 1:
        clock.tick(30)   #每秒30帧
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
font1 = pygame.font.Font(None, 84)
font2 = pygame.font.Font('simhei.ttf', 60)
font3 = pygame.font.Font('simhei.ttf', 24)


def display_box(screen, message):
    screen.blit(bac, (0,0))
    #screen.fill((111,111,111))
    screen.blit(li, (37,30))
    global Q
    for t in Q:
        screen.blit(img[t], (60+Q.index(t)*76,283))
    print_text(font1, 50, 308, '[' + '    ,'*(len(Q)-1) + '    ]',(0,0,0))
    for i in range(8):
        screen.blit(button_list[i], (30+ 60*i, 386))
    #screen.fill((111,111,111))
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font(None,28)
    #pygame.draw.rect(screen, (0,0,0),(200,700,200,20), 0)
    pygame.draw.rect(screen, (255,255,255),(225,737,204,37), 3)
    if len(message) != 0:
        screen.blit(fontobject.render(message+ '|', 1, (0,0,0)),(228, 743))

    pygame.display.flip()

def display_box2(screen, message):
    #screen.fill((111,111,111))
    screen.blit(bac, (0,0))
    #screen.fill((111,111,111))
    screen.blit(li, (37,30))
    global Q
    for t in Q:
        screen.blit(img[t], (60+Q.index(t)*76,283))
    print_text(font1, 50, 308, '[' + '    ,'*(len(Q)-1) + '    ]',(0,0,0))
    for i in range(8):
        screen.blit(button_list[i], (30+ 60*i, 386))
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font(None,28)
    #pygame.draw.rect(screen, (0,0,0),(200,700,200,20), 0)
    pygame.draw.rect(screen, (255,255,255),(225,737,204,37), 3)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (0,0,0)),(228, 743))
    pygame.display.flip()

def ask(screen, question):
    "ask(screen, question) -> answer"
    pygame.font.init()
    current_string = []
    display_box(screen, question + " " + ''.join(current_string))
    i = 0
    inkey = 128
    while 1:
        clock.tick(30)   #每秒30帧
        i += 1
        inkey = 128
        #inkey = get_key()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                inkey = event.key


        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("-")
        elif inkey == 59:
            current_string.append(':')
        elif inkey <= 127:
            current_string.append(chr(inkey))
            print(chr(inkey))
        if i%100 in range(50):
            display_box(screen, question + " " + ''.join(current_string))
        else:
            display_box2(screen, question + " " + ''.join(current_string))

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
    return ''.join(current_string)
img = []
for i in range(12):
    aa = pygame.image.load('lesson14/tu/' + str(i+1) + '.png').convert_alpha()
    aa = pygame.transform.smoothscale(aa, (90,90))
    img.append(aa)


bac = pygame.image.load('lesson14/bac/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (650, 800))
li = pygame.image.load('lesson14/tu/li.png').convert_alpha()
button_list = []
for i in range(8):
    aa = pygame.image.load('lesson14/bac/' + str(i+1) + '.png').convert_alpha()
    aa = pygame.transform.smoothscale(aa, (60, 60))
    button_list.append(aa)


#print (ask(screen, "Name") + " was entered")
d = [0,1,2,3,4,5,6,7,8,9,10,11]
T1 = [0,1,2,3,4,5]         # d[0:6] or d[:6] or d[:-6] or d[0:-6]
T2 = [1,2,3,4,5,6]         # d[1:7] or d[1:-5]
T3 = [5,6,7,8,9]           # d[5:10] or d[5:-2]
T4 = [7,8,9,10,11]         # d[7:] or d[7:12]
T5 = [0,2,4,6,8,10]        # d[::2]
T6 = [11,8,5,2]            # d[::-3]
T7 = [3,6,9]               # d[3::3] or d[3:12:3]
T8 = [8,4,0]               # d[-4::-4] or d[-4:-13:-4]
                           # 以上答案没有包括全部正确答案，只要运行出来结果显示一样就行

Q = T1
A = []
answer = False
wrong = False
while True:
    clock.tick(30)   #每秒30帧
    screen.blit(bac, (0,0))
    #screen.fill((111,111,111))
    screen.blit(li, (37,30))
    for i in range(8):
        screen.blit(button_list[i], (30+ 60*i, 386))

    '''
    for i in range(6):
        screen.blit(img[i], (120+i*76,30))
        screen.blit(img[i+6], (120+i*76, 130))
    print_text(font1, 50, 60, 'd=[   ,    ,    ,    ,    ,    ,',(0,0,0))
    print_text(font1, 40, 160, '         ,    ,    ,    ,    ,    ]',(0,0,0))
    '''
    #A = ask(screen, '')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if Rect(35,390,53,53).collidepoint(event.pos):
                #T1
                #print('1')
                Q = T1
                wrong = False
                A = []

            if Rect(95,390,53,53).collidepoint(event.pos):
                #T2
                #print('2')
                Q = T2
                wrong = False
                A = []
            if Rect(155,390,53,53).collidepoint(event.pos):
                #T3
                #print('3')
                Q = T3
                wrong = False
                A = []
            if Rect(215,390,53,53).collidepoint(event.pos):
                #T4
                #print('4')
                Q = T4
                wrong = False
                A = []
            if Rect(275,390,53,53).collidepoint(event.pos):
                #T5
                #print('5')
                Q = T5
                wrong = False
                A = []
            if Rect(335,390,53,53).collidepoint(event.pos):
                #T6
                #print('6')
                Q = T6
                wrong = False
                A = []
            if Rect(395,390,53,53).collidepoint(event.pos):
                #T7
                #print('7')
                Q = T7
                wrong = False
                A = []
            if Rect(455,390,53,53).collidepoint(event.pos):
                #T8
                #print('8')
                Q = T8
                wrong = False
                A = []
            if Rect(515,305,100,75).collidepoint(event.pos):
                #T9
                pass
            if Rect(225,737,204,37).collidepoint(event.pos):
                #答题输入框
                answer = True
                wrong = False
                A = []



    #pygame.draw.rect(screen, (0,0,0),(220,750,200,20), 0)
    pygame.draw.rect(screen, (255,255,255),(225,737,204,37), 3)
    if answer:
        ans = ask(screen, '')
        #print(ans)
        #lll = rc.findall(ans)
        if ans.startswith("d["):
            strlist = ans[len("d["):(len(ans)-1)].split(":")
            arr = []
            num = [False,False]
            isEnd = True
            for index in range(len(strlist)):
                if strlist[index] =="":
                    if index==0:
                        strlist[index] = 0
                        num[0] = True
                    elif isEnd:
                        strlist[index] = len(d)
                        num[1] = True
                        isEnd = False
                    else:
                        strlist[index] = 1
                arr.append(int(strlist[index]))

            print(arr)

            if len(arr) == 2:
                A = d[arr[0]:arr[1]]
            if len(arr) == 3:
                if arr[2] > 0:
                    A = d[arr[0]:arr[1]:arr[2]]
                else:
                    if (num[0]==True) and (num[1]==True):
                        A = d[::arr[2]]
                    elif (num[0]==False) and (num[1]==True):
                        A = d[arr[0]::arr[2]]
                    elif (num[0]==True) and (num[1]==False):
                        A = d[:arr[1]:arr[2]]
                    else:
                        A = d[arr[0]:arr[1]:arr[2]]

            #A = eval(ans)
        else:
            wrong = True

        answer = False
    if wrong:
        print_text(font2, 50, 600, '请输入正确的格式。',(255,0,0))

    print_text(font3, 228, 743, '点击这里输入答案', (111,111,111))
    for a in A:
        #screen.blit(img[a], (,))
        pass
    '''
    if A == Q:
        print('right')
    else:
        print('wrong')
    '''

    for t in Q:
        screen.blit(img[t], (60+Q.index(t)*76,283))
    print_text(font1, 50, 308, '[' + '    ,'*(len(Q)-1) + '    ]',(0,0,0))

    if len(A) == 0:
        pass
    elif len(A) <= 6:
        for t in A:
            screen.blit(img[t], (60+A.index(t)*76,483))
        print_text(font1, 50, 510, '[' + '    ,'*(len(A)-1) + '    ]',(0,0,0))
    else:
        for i in range(6):
            screen.blit(img[A[i]], (60+i*76,483))
        print_text(font1, 50, 510, '[' + '    ,'*6,(0,0,0))
        for i in range(len(A)-6):
            screen.blit(img[A[i+6]], (60+i*76,575))
        print_text(font1, 50, 608, ' ' + '    ,'*(len(A)-7) + '    ]',(0,0,0))


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
