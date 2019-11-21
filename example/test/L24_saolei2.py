import pygame,random,math,sys
from pygame.locals import *
from datetime import datetime
from pygame import Rect
#sys.setrecursionlimit(1000000)

CHUJI = 9,9,10         #第一个数字表示横排，第二个数字表示竖列，第三个数字表示雷的个数
ZHONGJI = 16,16,40
GAOJI = 30,16,99
game_level = CHUJI

def get():
    for i in range(game_level[1]):
        for j in range(game_level[0]):
            if Rect(42+ 30*j, 142+30+ i*30, 30, 30).collidepoint(event.pos):
                print(str(i) + '   ' +   str(j))
                return i,j

    return -1, -1

# 打开方块
def open_block(pos):
    if map_list[pos[0]][pos[1]] == -1:
        cover[pos[0]][pos[1]] = 0
        return True
    if map_list[pos[0]][pos[1]] != 0:
        cover[pos[0]][pos[1]] = 0
        open_list.append(pos)
    elif map_list[pos[0]][pos[1]] == 0:
        cover[pos[0]][pos[1]] = 0
        open_list.append(pos)
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if pos[0] + i >=0 and pos[0] +i <= game_level[1]-1 and pos[1] +j >=0 and pos[1] +j <= game_level[0]-1 and not (i == 0 and j == 0):
                    cover[pos[0]+i][pos[1]+j] = 0
                    if map_list[pos[0]+i][pos[1]+j] == 0 and [pos[0]+i, pos[1]+j] not in open_list:
                        open_block([pos[0]+i, pos[1]+j])

def is_win():
    for i in range(game_level[1]):
        for j in range(game_level[0]):
            if cover[i][j] and map_list[i][j] != -1:
                return False
    return True

def search (m, pos):
    mine_num = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if pos[0] + i >=0 and pos[0] +i <= game_level[1]-1 and pos[1] +j >=0 and pos[1] +j <= game_level[0]-1:
                if m[pos[0]+i][pos[1]+j] == -1:
                    mine_num += 1
    return mine_num


def create(game_level):
    m = [[0 for i in range(game_level[0])] for j in range(game_level[1])]
    num = 0
    while num <= game_level[2]-1:
        a = random.randint(0,game_level[1]-1)
        b = random.randint(0,game_level[0]-1)
        if m[a][b] == 0:
            m[a][b] = -1
            num += 1

    for i in range(game_level[1]):
        for j in range(game_level[0]):
            if m[i][j] == 0:
                m[i][j] = search(m, [i,j])

    return m

def show_mine_num(num = 10):
    # = num = 10
    h = num // 100
    t = (num%100) // 10
    u = num%10
    screen.blit(num_img[h], (50,80))
    screen.blit(num_img[t], (76,80))
    screen.blit(num_img[u], (102,80))

def show_time_num(second):
    h = second // 100
    t = (second%100) // 10
    u = second%10
    if h >= 10:
        tt = h/10
        h = h%10
        screen.blit(num_img[tt], (50+30*game_level[0]-128,80))
    screen.blit(num_img[h], (50+30*game_level[0]-102,80))
    screen.blit(num_img[t], (50+30*game_level[0]-76,80))
    screen.blit(num_img[u], (50+30*game_level[0]-50,80))


pygame.init()
screen = pygame.display.set_mode((350, 480))
pygame.display.set_caption("saolei")


dengji_img = []
for i in range(6):
    print(i)
    aa = pygame.image.load('lesson23/saolei/images/dengji' + str(i) + '.png').convert()
    aa = pygame.transform.smoothscale(aa, (60, 30))
    dengji_img.append(aa)

num_img = []
for i in range(10):
    aa = pygame.image.load('lesson23/saolei/images/' + str(i) + '.png').convert()
    aa = pygame.transform.smoothscale(aa, (26, 46))
    num_img.append(aa)

lei_img = []
for i in range(10):
    aa = pygame.image.load('lesson23/saolei/images/lei' + str(i) + '.png').convert()
    aa = pygame.transform.smoothscale(aa, (30, 30))
    lei_img.append(aa)

face_img = []
for i in range(5):
    aa = pygame.image.load('lesson23/saolei/images/f' + str(i+1) + '.png').convert()
    aa = pygame.transform.smoothscale(aa, (46, 46))
    face_img.append(aa)

other_img = []
for i in range(6):
    aa = pygame.image.load('lesson23/saolei/images/i' + str(i) + '.png').convert()
    aa = pygame.transform.smoothscale(aa, (30, 30))
    other_img.append(aa)

#bac = pygame.image.load('image/bac.png').convert_alpha()
#bac = pygame.transform.smoothscale(bac, (30,30))

map_dict = {
                -1: other_img[4],
                0: lei_img[0],
                1: lei_img[1],
                2: lei_img[2],
                3: lei_img[3],
                4: lei_img[4],
                5: lei_img[5],
                6: lei_img[6],
                7: lei_img[7],
                8: lei_img[8],
            }

map_list = create(game_level)
cover = [[1 for i in range(game_level[0])] for j in range(game_level[1])]    # 1是有遮盖，0则没有
open_list = []    #为0且已经被打开
flag_list = []
question_mark_list = []
game_lose = False
mine_num = 10
game_win = False
game_start = False
current_time = 0



first, second = -1, -1
times = pygame.time.Clock()
while True:
    screen = pygame.display.set_mode((80+30*game_level[0], 210+ 30*game_level[1]))
    #screen.blit(face_img[0], (0,0))
    times.tick(16)
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (192,192,192), (15,15, 50+30*game_level[0], 180+ 30*game_level[1]))
    pygame.draw.rect(screen, (255,255,255), (17,47, 46+30*game_level[0],146+30*game_level[1]))
    pygame.draw.rect(screen, (192,192,192), (20,50, 43+30*game_level[0],143+30*game_level[1]))

    pygame.draw.rect(screen, (255,255,255), (35,137,12+30*game_level[0],4))
    pygame.draw.polygon(screen, (137,137,137), [(35,65), (110,65),(35,140)])
    pygame.draw.rect(screen, (137,137,137), (35,65,12+30*game_level[0],4))
    pygame.draw.polygon(screen, (255,255,255), [(46+30*game_level[0],140), (46+30*game_level[0],65),(80++30*game_level[0]-109,140)])

    pygame.draw.rect(screen, (192,192,192), (39,69, 4+30*game_level[0],68))

    pygame.draw.polygon(screen, (137,137,137), [(35,165), (46+30*game_level[0],165),(35,180+30*game_level[1])])
    pygame.draw.polygon(screen, (255,255,255), [(46+30*game_level[0],180+30*game_level[1]), (46+30*game_level[0],165),(35,180+30*game_level[1])])
    pygame.draw.rect(screen, (192,192,192), (40,170, 2+30*game_level[0],6+30*game_level[1]))


    show_mine_num(mine_num)     #显示当前雷数
    screen.blit(face_img[0], ((80+30*game_level[0])/2 -23,80))
    show_time_num(current_time)        #显示当前进行了几秒

    screen.blit(dengji_img[0], (17,17))
    screen.blit(dengji_img[2], (77,17))
    screen.blit(dengji_img[4], (137,17))

    # 画地下的炸弹情况的
    for i in range(game_level[1]):
        for j in range(game_level[0]):
            #if
            screen.blit(map_dict[map_list[i][j]], (42 + j*30, 172 + i*30))

    # 画遮盖的
    for i in range(game_level[1]):
        for j in range(game_level[0]):
            if cover[i][j]:
                screen.blit(lei_img[9], (42 + j*30, 172 + i*30))

    for i in range(9):
        for j in range(9):
            if [i,j] in flag_list and not cover[i][j]:
                flag_list.remove([i,j])
                mine_num += 1
            if [i,j] in question_mark_list and not cover[i][j]:
                question_mark_list.remove([i,j])

    # 画小旗
    for flag in flag_list:
        screen.blit(other_img[2], (42 + flag[1]*30, 172 + flag[0]*30))

    # 画问号
    for question_mark in question_mark_list:
        screen.blit(other_img[0], (42 + question_mark[1]*30, 172 + question_mark[0]*30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION and not game_lose and not game_win:  # 鼠标移动
            first, second = get()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_lose and not game_win:
                first2, second2 = get()
                if first2 >= 0:       #将鼠标点击事件控制在9x9的格子内，排除超出的部分
                    if not game_start:    # 计时
                        clock_start = datetime.now()
                        game_start = True
                    if event.button[0] == 1:
                        if cover[first2][second2] and [first2,second2] not in flag_list and [first2,second2] not in question_mark_list:
                            game_lose = open_block([first2,second2])
                            game_win = is_win()
                    elif event.button[2] == 1:
                        if cover[first2][second2] and [first2,second2] not in flag_list and [first2,second2] not in question_mark_list:
                            flag_list.append([first2,second2])
                            mine_num -= 1
                        elif [first2,second2] in flag_list:
                            flag_list.remove([first2,second2])
                            question_mark_list.append([first2,second2])
                            mine_num += 1
                        elif [first2,second2] in question_mark_list:
                            question_mark_list.remove([first2,second2])

        #if event.type == MOUSEBUTTONDOWN:
            if Rect((80+30*game_level[0])/2 -23,80, 46, 46).collidepoint(event.pos):         # 按笑脸重置
                screen.blit(face_img[1], ((80+30*game_level[0])/2 -23,80))
                map_list = create(game_level)
                cover = [[1 for i in range(game_level[0])] for j in range(game_level[1])]
                open_list = []    #为0且已经被打开
                flag_list = []
                question_mark_list = []
                game_lose = False
                mine_num = game_level[2]
                game_win = False
                game_start = False
                current_time = 0
            if Rect(17,17, 60, 30).collidepoint(event.pos):
                screen.blit(dengji_img[1], (17,17))
                game_level = CHUJI
                mine_num = game_level[2]
                cover = [[1 for i in range(game_level[0])] for j in range(game_level[1])]
                map_list = create(game_level)
                open_list = []    #为0且已经被打开
                flag_list = []
                question_mark_list = []
                game_lose = False
                game_win = False
                game_start = False
                current_time = 0
                first, second = -1, -1
            if Rect(77,17, 60, 30).collidepoint(event.pos):
                screen.blit(dengji_img[3], (77,17))
                game_level = ZHONGJI
                map_list = create(game_level)
                cover = [[1 for i in range(game_level[0])] for j in range(game_level[1])]
                mine_num = game_level[2]
                open_list = []    #为0且已经被打开
                flag_list = []
                question_mark_list = []
                game_lose = False
                game_win = False
                game_start = False
                current_time = 0
                first, second = -1, -1
            if Rect(137,17, 60, 30).collidepoint(event.pos):
                screen.blit(dengji_img[5], (137,17))
                game_level = GAOJI
                map_list = create(game_level)
                cover = [[1 for i in range(game_level[0])] for j in range(game_level[1])]
                mine_num = game_level[2]
                open_list = []    #为0且已经被打开
                flag_list = []
                question_mark_list = []
                game_lose = False
                game_win = False
                game_start = False
                current_time = 0
                first, second = -1, -1

    #鼠标移到哪里哪里就凹下去
    if first >= 0:
        if cover[first][second] and [first,second] not in flag_list and [first,second] not in question_mark_list:
            screen.blit(lei_img[0], (42+second*30, 142+30+first*30))

    if game_lose:   # 游戏结束时将地底的雷，包括插旗插错的雷显示出来
        game_start = False
        screen.blit(face_img[4], ((80+30*game_level[0])/2 -23,80))
        for i in range(game_level[1]):
            for j in range(game_level[0]):
                if map_list[i][j] == -1 and (i,j) != (first2,second2):
                    screen.blit(other_img[3], (42 + j*30, 142+30 + i*30))
        for flag in flag_list:
            if map_list[flag[0]][flag[1]] != -1:
                screen.blit(other_img[5], (42 + flag[1]*30, 142+30 + flag[0]*30))

    if game_win:
        game_start = False
        screen.blit(face_img[3], ((80+30*game_level[0])/2 -23,80))

    if game_start:
        current_time = (datetime.now() - clock_start).seconds

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
