import pygame,random,math,sys
from pygame.locals import *
from datetime import datetime
from L24_saolei3def import open_block, get
from pygame import Rect
##############################
#扫雷游戏的设计思路
#首先分析游戏逻辑，1. 点击鼠标左键：1）如果所点击的格子周围没雷，则会自动扩散到周围有雷的格子，并显示格子的雷数
#                                 2）如果所点击的格子周围有雷，则打开该格子，显示出格子的雷数
#                                 3）如果所点击的格子底下有雷，则显示所有雷的位置，并且游戏结束
#                                 4）如果点击到笑脸位置，则重置游戏
#                                 5）如果点击到其他地方，没有反应
#                 2. 点击鼠标右键：在格子上插旗，表示底下有雷，插旗的地方左键不能点击，再次点击右键取消插旗，左键重新可以点击
#                 3. 地雷分布在9X9的格子中，随机分布，其余格子中的数字代表其自身周围八个格子中有几个雷，如周围有八个雷则该格子中的数字为8，
#                 4. 显示当前雷数，右键插旗则减少一个雷数
#                 5. 显示当前时间，以秒为单位
#                 6. 只要所有非雷的格子都被点开，则游戏胜利，成功扫雷
#####
#然后开始设计
#1. 构造出地雷的分布图：1）9x9的格子中的数据可以存放在二维列表中，我们可以将-1表示为雷，0-8表示为雷数，如何生成一个随机的地雷图是难点。    * create()函数  map_list是地雷分布图
#                      2）先生成一个都是0的9x9二维列表
#                      3）随机10个位置，存入该二维列表
#                      4）根据该二维列表中-1的位置，计算出其余格子中的雷数 *程序中的search()函数
#2. 思考如何将格子中的雷数展示出来：1）一种思路是：先在界面画出遮盖的图像，然后当左键点击的时候，将坐标存入一个列表中，然后画出该列表的雷数的图像
#                                 2）另一种思路是：先将所有雷数的图像按分布图画出来，再画出一个遮盖的图像，当左键点击的时候，
#                                                  将坐标存入一个列表中，然后列表中的坐标点的位置则不画遮盖， *本程序选择了这种思路 *cover 列表
#                                 #）数字如何跟图片联系起来？ 可以使用字典  *程序中的map_dict字典
#
#3. 如何解决点击事件：1）之前应该学过，根据位置返回坐标 **为什么初始坐标是（-1，-1）？ 因为（0，0）是存在的，所以不能用来当作初始坐标   *get()函数
#                    2）获取了坐标点之后，根据点击事件是左键还是右键来进行接下来的分支程序：1）如果是左键：判断是不是已经被打开了，如果不是，
#                                                                                                    则使用open_block()函数打开该格子，如果是雷数为0的格子，会自动扩散，如果是雷，则返回True。
#                                                                                      2）如果是右键：则判断是不是已经被打开了，如果不是，
#                                                                                                    则将该坐标点存如flag_list列表中  *后续再增加再次点击则将旗子移除的功能
#4. 截至目前，游戏的基本逻辑就完成了大概，接下来要对程序进行完善
#           1）画出旗子
#           2）右键旗子功能的完善
#           3）增加判断是否胜利的程序
#           4）当游戏失败时会怎样，游戏胜利时会怎样
#           5）如何重置游戏
#           6）显示当前雷数和当前时间



def is_win():
    for i in range(9):
        for j in range(9):
            if cover[i][j] == 1 and map_list[i][j] != -1:  ###### 如果存在不是雷的方块还没有点开，那么游戏就没有结束
                return False
    return True

def search (m, f, s):     # 计算每个格子的雷数的函数  *****
    mine_num = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if f + i >=0 and f +i <= 8 and s +j >=0 and s +j <= 8: # 控制位置的范围
                if m[f+i][s+j] == -1: ###如果有雷存在
                    mine_num += 1 ## 那么雷的数目增加1
    return mine_num


def create():              #创建地雷分布图的函数
    m = [[0 for i in range(9)] for j in range(9)]

    num = 0
    while num < 10:       # 这里的数字等于雷数
        a = random.randint(0,8)
        b = random.randint(0,8)
        if m[a][b] == 0:
            m[a][b] = -1
            num += 1 ##把雷的地方搞出来

    for i in range(9):
        for j in range(9):
            if m[i][j] == 0:
                m[i][j] = search(m, i, j) # 计算出其他格子的数目是多少（可能0-8都有可能）
    return m
def show_mine_num(num = 10): #显示雷的数目
    # = num = 10
    h = num // 100
    t = (num%100) // 10
    u = num%10
    screen.blit(num_img[h], (50,50))
    screen.blit(num_img[t], (76,50))
    screen.blit(num_img[u], (102,50))

def show_time_num(second): # 显示度过的时间
    h = second // 100
    t = (second%100) // 10
    u = second%10
    screen.blit(num_img[h], (220,50))
    screen.blit(num_img[t], (246,50))
    screen.blit(num_img[u], (272,50))


pygame.init()
screen = pygame.display.set_mode((350,450))
pygame.display.set_caption("saolei")

bac = pygame.image.load('lesson23/saolei/bac.png').convert()

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
flag_list = [] #你点下的flag
game_lose = False
mine_num = 10
game_win = False
game_start = False
current_time = 0

first, second = -1, -1 #点击获取位置
times = pygame.time.Clock()
while True:
    times.tick(16)
    screen.blit(bac, (0,0))

    show_mine_num(mine_num)     #显示当前雷数
    screen.blit(face_img[0], (151,50))    # 显示中间的笑脸
    show_time_num(current_time)        #显示当前进行了几秒

    ########################################################
    '''
    # 画地下的炸弹情况的
    for i in range(9):
        for j in range(9):
            screen.blit(map_dict[map_list[i][j]], (42 + j*30, 142 + i*30))

    # 画遮盖的
    for i in range(9):
        for j in range(9):
            if cover[i][j]:
                screen.blit(lei_img[9], (42 + j*30, 142 + i*30))

    # 修复插旗后的旗子在格子扩散的时候不会被消除的bug
    for i in range(9):
        for j in range(9):
            if [i,j] in flag_list and not cover[i][j]:
                flag_list.remove([i,j])
                mine_num += 1
    '''
    ########################################
    #以上代码可以合并
    for i in range(9):
        for j in range(9):
            screen.blit(map_dict[map_list[i][j]], (42 + j*30, 142 + i*30))
            if cover[i][j]:
                screen.blit(lei_img[9], (42 + j*30, 142 + i*30))

            if [i,j] in flag_list and not cover[i][j]:
                flag_list.remove([i,j])
                mine_num += 1  #### 没有合并的上述代码

    # 画小旗
    for flag in flag_list:
        screen.blit(other_img[2], (42 + flag[1]*30, 142 + flag[0]*30))




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION and not game_lose and not game_win:  # 鼠标移动
            first, second = get(event.pos)
        if event.type == MOUSEBUTTONDOWN:
            if not game_lose and not game_win:
                first2, second2 = get(event.pos)
                if first2 >= 0:       #将鼠标点击事件控制在9x9的格子内，排除超出的部分
                    if not game_start:    # 计时
                        clock_start = datetime.now()
                        game_start = True
                    if event.button[0] == 1:
                        if cover[first2][second2] == 1 and [first2,second2] not in flag_list:
                            game_lose = open_block(map_list, cover, open_list, first2, second2)
                            game_win = is_win() ###左键
                    elif event.button[2] == 1:
                        if cover[first2][second2] == 1 and [first2,second2] not in flag_list:
                            flag_list.append([first2,second2])
                            mine_num -= 1 ###右键
                        elif [first2,second2] in flag_list:
                            flag_list.remove([first2,second2])
                            mine_num += 1 ##两次按下后取消插旗子，并且雷数目增加1

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
