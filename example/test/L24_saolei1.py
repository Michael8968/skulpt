import pygame,random,math,sys
from pygame.locals import *
from datetime import datetime
from pygame import Rect

#sys.setrecursionlimit(1000000)

def get():
    for i in range(9):
        for j in range(9):
            if Rect(42+ 30*j, 142+ i*30, 30, 30).collidepoint(event.pos):
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
                if pos[0] + i >=0 and pos[0] +i <= 8 and pos[1] +j >=0 and pos[1] +j <= 8 and not (i == 0 and j == 0):
                    cover[pos[0]+i][pos[1]+j] = 0
                    if map_list[pos[0]+i][pos[1]+j] == 0 and [pos[0]+i, pos[1]+j] not in open_list:
                        open_block([pos[0]+i, pos[1]+j])

def is_win():
    for i in range(9):
        for j in range(9):
            if cover[i][j] and map_list[i][j] != -1:
                return False
    return True

def search (m, pos):
    mine_num = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if pos[0] + i >=0 and pos[0] +i <= 8 and pos[1] +j >=0 and pos[1] +j <= 8:
                if m[pos[0]+i][pos[1]+j] == -1:
                    mine_num += 1
    return mine_num


def create():
    m = [[0 for i in range(9)] for j in range(9)]
    num = 0
    while num <= 9:
        a = random.randint(0,8)
        b = random.randint(0,8)
        if m[a][b] == 0:
            m[a][b] = -1
            num += 1

    for i in range(9):
        for j in range(9):
            if m[i][j] == 0:
                m[i][j] = search(m, [i,j])

    return m

def show_mine_num(num = 10):
    # = num = 10
    h = num // 100
    t = (num%100) // 10
    u = num%10
    screen.blit(num_img[h], (50,50))
    screen.blit(num_img[t], (76,50))
    screen.blit(num_img[u], (102,50))

def show_time_num(second):
    h = second // 100
    t = (second%100) // 10
    u = second%10
    screen.blit(num_img[h], (220,50))
    screen.blit(num_img[t], (246,50))
    screen.blit(num_img[u], (272,50))


pygame.init()
screen = pygame.display.set_mode((350,450))
pygame.display.set_caption("saolei")


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

map_list = create()
cover = [[1 for i in range(9)] for j in range(9)]    # 1是有遮盖，0则没有
open_list = []    #为0且已经被打开
flag_list = []
game_lose = False
mine_num = 10
game_win = False
game_start = False
current_time = 0

first, second = -1, -1
times = pygame.time.Clock()
while True:

    times.tick(16)
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (192,192,192), (15,15, 320,420))
    pygame.draw.rect(screen, (255,255,255), (17,17, 316,416))
    pygame.draw.rect(screen, (192,192,192), (20,20, 313,413))

    pygame.draw.rect(screen, (255,255,255), (35,107,282,4))
    pygame.draw.polygon(screen, (137,137,137), [(35,35), (110,35),(35,110)])
    pygame.draw.rect(screen, (137,137,137), (35,35,282,4))
    pygame.draw.polygon(screen, (255,255,255), [(316,110), (316,35),(241,110)])

    pygame.draw.rect(screen, (192,192,192), (39,39, 274,68))

    pygame.draw.polygon(screen, (137,137,137), [(35,135), (316,135),(35,420)])
    pygame.draw.polygon(screen, (255,255,255), [(316,420), (316,135),(35,420)])
    pygame.draw.rect(screen, (192,192,192), (40,140, 272,276))


    show_mine_num(mine_num)     #显示当前雷数
    screen.blit(face_img[0], (151,50))
    show_time_num(current_time)        #显示当前进行了几秒


    # 画地下的炸弹情况的
    for i in range(9):
        for j in range(9):
            #if
            screen.blit(map_dict[map_list[i][j]], (42 + j*30, 142 + i*30))

    # 画遮盖的
    for i in range(9):
        for j in range(9):
            if cover[i][j]:
                screen.blit(lei_img[9], (42 + j*30, 142 + i*30))

    for i in range(9):
        for j in range(9):
            if [i,j] in flag_list and not cover[i][j]:
                flag_list.remove([i,j])
                mine_num += 1
    # 画小旗
    for flag in flag_list:
        screen.blit(other_img[2], (42 + flag[1]*30, 142 + flag[0]*30))



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION and not game_lose and not game_win:  # 鼠标移动
            first, second = get()
        if event.type == MOUSEBUTTONDOWN:
            if not game_lose and not game_win:
                first2, second2 = get()
                if first2 >= 0:       #将鼠标点击事件控制在9x9的格子内，排除超出的部分
                    if not game_start:    # 计时
                        clock_start = datetime.now()
                        game_start = True

                    print(event.button)

                    if event.button[0] == 1:
                        if cover[first2][second2] and [first2,second2] not in flag_list:
                            game_lose = open_block([first2,second2])
                            game_win = is_win()
                    elif event.button[2] == 1:
                        if cover[first2][second2] and [first2,second2] not in flag_list:
                            flag_list.append([first2,second2])
                            mine_num -= 1
                        elif [first2,second2] in flag_list:
                            flag_list.remove([first2,second2])
                            mine_num += 1
            if Rect(151,50, 46, 46).collidepoint(event.pos):         # 按笑脸重置
                screen.blit(face_img[1], (151,50))
                map_list = create()
                cover = [[1 for i in range(9)] for j in range(9)]
                open_list = []    #为0且已经被打开
                flag_list = []
                game_lose = False
                mine_num = 10
                game_win = False
                game_start = False
                current_time = 0


    #鼠标移到哪里哪里就凹下去
    if first >= 0:
        if cover[first][second] and [first,second] not in flag_list:
            screen.blit(lei_img[0], (42+second*30, 142+first*30))

    if game_lose:   # 游戏结束时将地底的雷，包括插旗插错的雷显示出来
        game_start = False
        screen.blit(face_img[4], (151,50))
        for i in range(9):
            for j in range(9):
                if map_list[i][j] == -1 and (i,j) != (first2,second2):
                    screen.blit(other_img[3], (42 + j*30, 142 + i*30))
        for flag in flag_list:
            if map_list[flag[0]][flag[1]] != -1:
                screen.blit(other_img[5], (42 + flag[1]*30, 142 + flag[0]*30))

    if game_win:
        game_start = False
        screen.blit(face_img[3], (151,50))

    if game_start:
        current_time = (datetime.now() - clock_start).seconds

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update()
