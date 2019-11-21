import sys, random, time, pygame
from pygame.locals import *
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Demo")

bac = pygame.image.load('lesson15/goods/supermarket.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (1000,600))

bac2 = pygame.image.load('lesson15/bill/pay.png').convert_alpha()
bac2 = pygame.transform.smoothscale(bac2, (1000,600))

say = pygame.image.load('lesson15/goods/say.png').convert_alpha()
say = pygame.transform.smoothscale(say, (200,60))

bill = pygame.image.load('lesson15/bill/bill.png').convert_alpha()
bill = pygame.transform.smoothscale(bill, (400,600))

font = pygame.font.Font(None, 18)
font1 = pygame.font.Font('simhei.ttf', 50)
font2 = pygame.font.Font('simhei.ttf', 20)

def print_text(aa,font, x, y, text, color= (0,0,0)):
    imgText = font.render(text, True, color)
    aa.blit(imgText, (x,y))


price_dict = {'苹果': 4, '香蕉': 5, '鲤鱼': 7, '火龙果': 9,
             '菠萝': 3, '紫葡萄': 15, '青葡萄': 12, '螃蟹': 35,
              '西瓜': 3, '龙虾': 28, '茄子': 4, '玉米': 4, '南瓜': 3,
              '紫薯': 5, '红薯': 5, '萝卜': 3, '黄瓜': 3}


need_buy_dict = {'苹果':4, '香蕉':4, '紫葡萄': 1, '西瓜':1, '龙虾':3, '鲤鱼': 2, '黄瓜':4, '萝卜':2, '紫薯':3, '红薯':3}


select_dict = {}
suf = ''
suf2 = ''
aa = 0
sayit = False
show_bill = False
clock = pygame.time.Clock()

while True:
    clock.tick(30)   #每秒30帧
    x,y = pygame.mouse.get_pos()

    screen.fill((100,100,100))
    screen.blit(bac,(0,0))

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if not suf2 and Rect(870,250,50,160).collidepoint(event.pos):
                if not suf:
                    suf = pygame.Surface((300, 400))

                elif suf:
                    suf = ''

            if not suf2 and Rect(28,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '龙虾' in need_buy_dict:
                        if '龙虾' in select_dict:
                            select_dict['龙虾'] += 1
                        else:
                            select_dict['龙虾'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '龙虾' in select_dict:
                        if select_dict['龙虾'] >= 1:
                            select_dict['龙虾'] -= 1
                        else:
                            del select_dict['龙虾']

            if not suf2 and Rect(148,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '黄瓜' in need_buy_dict:
                        if '黄瓜' in select_dict:
                            select_dict['黄瓜'] += 1
                        else:
                            select_dict['黄瓜'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '黄瓜' in select_dict:
                        if select_dict['黄瓜'] >= 1:
                            select_dict['黄瓜'] -= 1
                        else:
                            del select_dict['黄瓜']

            if not suf2 and Rect(268,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '萝卜' in need_buy_dict:
                        if '萝卜' in select_dict:
                            select_dict['萝卜'] += 1
                        else:
                            select_dict['萝卜'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '萝卜' in select_dict:
                        if select_dict['萝卜'] >= 1:
                            select_dict['萝卜'] -= 1
                        else:
                            del select_dict['萝卜']

            if not suf2 and Rect(388,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '红薯' in need_buy_dict:
                        if '红薯' in select_dict:
                            select_dict['红薯'] += 1
                        else:
                            select_dict['红薯'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '红薯' in select_dict:
                        if select_dict['红薯'] >= 1:
                            select_dict['红薯'] -= 1
                        else:
                            del select_dict['红薯']

            if not suf2 and Rect(508,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '南瓜' in need_buy_dict:
                        if '南瓜' in select_dict:
                            select_dict['南瓜'] += 1
                        else:
                            select_dict['南瓜'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '南瓜' in select_dict:
                        if select_dict['南瓜'] >= 1:
                            select_dict['南瓜'] -= 1
                        else:
                            del select_dict['南瓜']

            if not suf2 and Rect(628,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '茄子' in need_buy_dict:
                        if '茄子' in select_dict:
                            select_dict['茄子'] += 1
                        else:
                            select_dict['茄子'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '茄子' in select_dict:
                        if select_dict['茄子'] >= 1:
                            select_dict['茄子'] -= 1
                        else:
                            del select_dict['茄子']

            if not suf2 and Rect(748,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '玉米' in need_buy_dict:
                        if '玉米' in select_dict:
                            select_dict['玉米'] += 1
                        else:
                            select_dict['玉米'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '玉米' in select_dict:
                        if select_dict['玉米'] >= 1:
                            select_dict['玉米'] -= 1
                        else:
                            del select_dict['玉米']

            if not suf2 and Rect(868,43,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '紫薯' in need_buy_dict:
                        if '紫薯' in select_dict:
                            select_dict['紫薯'] += 1
                        else:
                            select_dict['紫薯'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '紫薯' in select_dict:
                        if select_dict['紫薯'] >= 1:
                            select_dict['紫薯'] -= 1
                        else:
                            del select_dict['紫薯']

            if not suf2 and Rect(28,238,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '鲤鱼' in need_buy_dict:
                        if '鲤鱼' in select_dict:
                            select_dict['鲤鱼'] += 1
                        else:
                            select_dict['鲤鱼'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '鲤鱼' in select_dict:
                        if select_dict['鲤鱼'] >= 1:
                            select_dict['鲤鱼'] -= 1
                        else:
                            del select_dict['鲤鱼']

            if not suf2 and Rect(28,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '螃蟹' in need_buy_dict:
                        if '螃蟹' in select_dict:
                            select_dict['螃蟹'] += 1
                        else:
                            select_dict['螃蟹'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '螃蟹' in select_dict:
                        if select_dict['螃蟹'] >= 1:
                            select_dict['螃蟹'] -= 1
                        else:
                            del select_dict['螃蟹']

            if not suf2 and Rect(148,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '菠萝' in need_buy_dict:
                        if '菠萝' in select_dict:
                            select_dict['菠萝'] += 1
                        else:
                            select_dict['菠萝'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '菠萝' in select_dict:
                        if select_dict['菠萝'] >= 1:
                            select_dict['菠萝'] -= 1
                        else:
                            del select_dict['菠萝']

            if not suf2 and Rect(268,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '西瓜' in need_buy_dict:
                        if '西瓜' in select_dict:
                            select_dict['西瓜'] += 1
                        else:
                            select_dict['西瓜'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '西瓜' in select_dict:
                        if select_dict['西瓜'] >= 1:
                            select_dict['西瓜'] -= 1
                        else:
                            del select_dict['西瓜']

            if not suf2 and Rect(388,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '香蕉' in need_buy_dict:
                        if '香蕉' in select_dict:
                            select_dict['香蕉'] += 1
                        else:
                            select_dict['香蕉'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '香蕉' in select_dict:
                        if select_dict['香蕉'] >= 1:
                            select_dict['香蕉'] -= 1
                        else:
                            del select_dict['香蕉']

            if not suf2 and Rect(508,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '青葡萄' in need_buy_dict:
                        if '青葡萄' in select_dict:
                            select_dict['青葡萄'] += 1
                        else:
                            select_dict['青葡萄'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '青葡萄' in select_dict:
                        if select_dict['青葡萄'] >= 1:
                            select_dict['青葡萄'] -= 1
                        else:
                            del select_dict['青葡萄']

            if not suf2 and Rect(628,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '苹果' in need_buy_dict:
                        if '苹果' in select_dict:
                            select_dict['苹果'] += 1
                        else:
                            select_dict['苹果'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '苹果' in select_dict:
                        if select_dict['苹果'] >= 1:
                            select_dict['苹果'] -= 1
                        else:
                            del select_dict['苹果']

            if not suf2 and Rect(748,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '紫葡萄' in need_buy_dict:
                        if '紫葡萄' in select_dict:
                            select_dict['紫葡萄'] += 1
                        else:
                            select_dict['紫葡萄'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '紫葡萄' in select_dict:
                        if select_dict['紫葡萄'] >= 1:
                            select_dict['紫葡萄'] -= 1
                        else:
                            del select_dict['紫葡萄']

            if not suf2 and Rect(868,438,106,140).collidepoint(event.pos):
                if event.button[0] == 1:
                    if '火龙果' in need_buy_dict:
                        if '火龙果' in select_dict:
                            select_dict['火龙果'] += 1
                        else:
                            select_dict['火龙果'] = 1
                    else:
                        sayit = True
                elif event.button[2] == 1:
                    if '火龙果' in select_dict:
                        if select_dict['火龙果'] >= 1:
                            select_dict['火龙果'] -= 1
                        else:
                            del select_dict['火龙果']

            if suf2 and Rect(815,290, 125, 410).collidepoint(event.pos):
                suf2 = ''
            if not suf2 and Rect(780,370,80,45).collidepoint(event.pos):
                #print('aaa')
                suf2 = pygame.Surface((1000, 600))
                suf2.fill((255,255,255))
                suf2.blit(bac2,(0,0))

            if suf2 and Rect(30, 185, 230, 150).collidepoint(event.pos):
                show_bill = True




    if sayit:
        aa += 1
        screen.blit(say, (800,200))
        if aa >= 200:
            aa = 0
            sayit = False


    if suf:

        screen.blit(suf, (500,100))
        suf.fill((255,255,255))
        #suf.set_alpha(200)
        print_text(suf,font1,55,10, '购物清单')
        i = 0
        for a in need_buy_dict:
            if a in select_dict:
                select_thing_num = select_dict[a]
            else:
                select_thing_num = 0
            i += 1
            print_text(suf,font2,30, 40+i*30, a + '要买' + str(need_buy_dict[a]) + '个'+ '     已买' + str(select_thing_num) + '个',(100,100,100))

    if suf2:
        screen.blit(suf2,(0,0))
        sum = 0
        if show_bill:
            suf2.blit(bill, (350,20))
            i = 0
            print_text(suf2,font2, 400 , 180, '商品名   单价   个数   总价',(50,50,50))
            for a in select_dict:
                i += 1
                print_text(suf2,font2,   400 , 180+i*30, a + '    ' + str(price_dict[a]) + '元/个  ' + str(select_dict[a]) + '个    ' + str(select_dict[a]*price_dict[a]) + '元',(50,50,50))
                sum += select_dict[a]*price_dict[a]

            print_text(suf2,font2, 400,  510, '全部                    ' + str(sum)+ '元')

    print_text(screen,font,10,10,str(x)+ '  ' + str(y))

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
