import pygame,random,sys
from pygame.locals import *
from pygame import Rect

#五子棋游戏的设计思路
#首先分析游戏逻辑
#1. 默认先手为黑棋，鼠标左键点击哪里，则在哪里放置一颗棋，黑白棋轮流放
#2. 已经放置棋子的地方不可再放棋
#3. 先或横或竖或斜连成5子的玩家则胜利
#####
#然后开始设计游戏
#1. 画出棋盘 *如果使用bacc.png则不需要画棋盘
#2. 生成一个19x19的二维列表，以0填充 *也可以不以0填充，但之后的判断则要随之改变
#3. 当鼠标点击棋盘上某个点，根据get()函数的返回的坐标点的值，判断该坐标点在二维列表中的值是否为0， 如果为0，则将二维列表中该坐标的值改为1或2，1表示黑棋，2表示白棋
#4. 判断是否游戏胜利（该程序的重点难点，如果能设计出更好的算法，请告诉我）：五子棋的胜利条件是--某一方棋子在横向,纵向或斜向连续五个连成一条线，则判为胜利。
#               1）由以上胜利条件可以得出共有四个连线方向
#               2）我们可以遍历棋盘上的每个坐标点，看该点在这四个方向（横向、纵向、左斜向、右斜向）上是否能有连续五个相同颜色的棋子，
#                  但是这样会造成大量无用的计算，其实我们只需要判断最后一个落子在这四个方向中有没有跟它相同颜色的连续的其它四个棋子就行了
#               3）获取最后一个落子坐标点，分四个方向讨论，比如横向：横向包括向左跟向右，因为只要连续五个棋子则胜利，
#                  所以先向左循环四次（如果棋子颜色跟最后落子一样，则数值加1，否则退出循环），再向右循环四次（如果棋子颜色跟最后落子一样，则数值加1，否则退出循环），
#                  看叠加的数值是否大于或等于5（初始值为1），如果是，则说明在横向上该棋子达成了胜利条件，则游戏为最后落子的一方胜利
#               4）其他三个方向也是如此
#               5）如果没有一个方向达成胜利条件，则说明落子方还没胜利，继续由另一方落子。另一方落子后，继续进行该判断。
####以上完成了游戏的基本内容，接下来可以对程序进一步的完善
# 1. 胜利之后显示是黑棋或者白棋获得胜利
# 2. 按Enter回车键重置游戏


# 另一种判断游戏是否胜利的思路是：四个方向（上到下、左到右、左上到右下、左下到右上）依次遍历，
#       比如上到下：19列每一列从第一个数（作为当前数）开始如果下一个数跟它一样，则计数的数值加1，否则将当前数改成新的数字，如果计数的数值大于或等于五，则该当前数代表的棋子那一方胜利
#       依次遍历其他三个方向



pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("wuziqi")

def is_win(first,second):   #判断是否赢棋的函数
    num = 5           # 改变数字，成为相应的几子棋，如num=5则为五子棋,num=4则为四子棋
    winflag = 1
    chess_kind = map1[first][second]
    #print(chess_kind)

    ############## 横向检测
    for i in range(1,num):    #向右检测
        if second + i <= 18:
            if map1[first][second+i] == chess_kind:
                winflag += 1 ####如果winflag等于5个，就是赢啦啦啦啦
            else:
                break

    for i in range(1,num):     #向左检测
        if second - i >= 0:
            if map1[first][second-i] == chess_kind:
                winflag += 1
            else:
                break
    if winflag >= num:
        return True
    else:
        winflag = 1


    ################## 纵向检测
    for i in range(1,num):    # 向下检测
        if first + i <= 18:
            if map1[first+i][second] == chess_kind:
                winflag += 1
            else:
                break
    for i in range(1,num):    # 向上检测
        if first - i >= 0:
            if map1[first-i][second] == chess_kind:
                winflag += 1
            else:
                break
    if winflag >= num:
        return True
    else:
        winflag = 1

   ################## 左下到右上检测
    for i in range(1,num):   # 向右上检测
        if first - i >= 0 and second + i <= 18:
            if map1[first-i][second+i] == chess_kind:
                winflag += 1
            else:
                break
    for i in range(1,num):   # 向左下检测
        if first + i <= 18 and second - i >= 0:
            if map1[first+i][second-i] == chess_kind:
                winflag += 1
            else:
                break
    if winflag >= num:
        return True
    else:
        winflag = 1


    ################### 左上到右下检测
    for i in range(1,num):   # 向左上检测
        if first - i >= 0 and second - i >= 0:
            if map1[first-i][second-i] == chess_kind:
                winflag += 1
            else:
                break
    for i in range(1,num):   # 向右下检测
        if first + i <= 18 and second + i <= 18:
            if map1[first+i][second+i] == chess_kind:
                winflag += 1
            else:
                break
    if winflag >= num:
        return True

    return False



def get():
    for i in range(19):
        for j in range(19):
            if Rect(20+ 40*j, 20+ i*40, 40, 40).collidepoint(event.pos):
                #print(str(i) + '   ' +   str(j))
                return i,j #####  获取坐标，这个函数可以直接告诉学生


bac = pygame.image.load('lesson24/wuziqi/bac.jpg').convert_alpha()
bac = pygame.transform.smoothscale(bac, (800,800))

bacc = pygame.image.load('lesson24/wuziqi/bacc.png').convert_alpha()

white = pygame.image.load('lesson24/wuziqi/white.png').convert_alpha()
new_white = pygame.image.load('lesson24/wuziqi/new_white.png').convert_alpha()
black = pygame.image.load('lesson24/wuziqi/black.png').convert_alpha()
new_black = pygame.image.load('lesson24/wuziqi/new_black.png').convert_alpha()


#map1 = [[0 for i in range(19)] for j in range(19)]    # 列表生成式写法

# 非列表生成式写法
map1 = []
for i in range(19):
    map1.append([])

for x in map1:
    for i in range(19):
        x.append(0)

#print(map1)

put_black = True
winner = ''
times = pygame.time.Clock()
new_first = 0    #存储最后一个棋子的坐标点
new_second = 0
while True:
    times.tick(30)
    screen.fill((255,255,255))
    screen.blit(bacc, (0,0))          #如果不想画棋盘，则改成bacc，否则改成bac

    # 控制
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 重置游戏
        elif event.type == KEYDOWN:# and winner: #如果不想游戏还没结束就可以按回车重来，则加上
            if event.key == K_RETURN:
                for i in range(19):
                    for j in range(19):
                        map1[i][j] = 0

                new_first = 0
                new_second = 0
                put_black = True
                winner = ''

        elif event.type == MOUSEBUTTONDOWN and event.button[0] == 1 and not winner:   # 鼠标按下且得是左键且游戏还没胜利者的时候

            print('鼠标点击2')

            if get():
                first, second = get()
                #print(first,second)
                if not map1[first][second]:  #已经有棋子的地方不算   也可以写 if map[first][second] == 0:
                    new_first = first           #控制最后一个棋子的显示不出错
                    new_second = second
                    print(new_first,new_second)
                    if put_black:
                        map1[first][second] = 1
                    else:
                        map1[first][second] = 2

                    if is_win(first,second):
                        if put_black:
                            winner = 'black'
                        else:
                            winner = 'white'
                    put_black = not put_black ###这一行要注意
    '''
    #############################################
    #画棋盘,   如果使用bacc.png当背景， 则不需要画棋盘
    for i in range(19):
        pygame.draw.line(screen, (0,0,0), (40, 40 + i*40),(760, 40 + i*40) , 2)
        pygame.draw.line(screen, (0,0,0), (40 + i*40, 40),(40 + i*40, 760) , 2)

    pygame.draw.line(screen, (0,0,0), (40, 40),(40, 760) , 4)
    pygame.draw.line(screen, (0,0,0), (760, 40),(760, 760) , 4)
    pygame.draw.line(screen, (0,0,0), (40, 40),(760, 40) , 4)
    pygame.draw.line(screen, (0,0,0), (760, 760),(40, 760) , 4)

    for i in range(4,17,6):
        for j in range(4,17,6):
            pygame.draw.circle(screen, (0,0,0), (40*i,40*j), 8)
    ###########################################
    '''

    # 将有棋的地方放上棋子的图片
    for i in range(19):
        for j in range(19):
            if map1[i][j] == 1:
                screen.blit(black, (23+j*40, 23+i*40))
            elif map1[i][j] == 2:
                screen.blit(white, (23+j*40, 23+i*40))
    # 显示最后下的棋子
    if new_first:
        if not put_black:
            screen.blit(new_black, (23+new_second*40, 23+new_first*40))
        else:
            screen.blit(new_white, (23+new_second*40, 23+new_first*40))


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    if winner:
        #print(winner)
        font = pygame.font.Font(None, 88)
        fontimg = font.render(winner + ' chess win', True, (0,250,154))
        screen.blit(fontimg, (160,250))
        fontimg2 = font.render('press enter to restart', True, (0,250,154))
        screen.blit(fontimg2, (100,350))
    pygame.display.update()
