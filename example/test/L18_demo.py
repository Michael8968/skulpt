import sys, random, time, pygame
from pygame.locals import *
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Demo")

def draw_map(screen):
    screen.blit(bac,(0,0))
    for i in range(20):
        for j in range(30):
            screen.blit(map_dict[map[i][j]][0], (0+30*j,0+30*i))

def draw_lan(screen, items, craft):
    lan_suf = pygame.Surface((670, 60))
    lan_suf.fill((100,100,100))
    for i in range(12):
        pygame.draw.rect(lan_suf, (255,255,255), (7.5+ i*55,5, 50,50))
    #pygame.draw.rect(lan_suf, (0,0,0), (7.5+11*55, 5, 50,50))
    lan_suf.blit(bag, (7.5+55*11,5))
    ii = 0
    for thing in items:
        if thing not in craft or thing == 'huodui' or thing == 'zhangpeng':
            if items[thing]:
                print_text(lan_suf, 7.5 +ii *55 , 5, str(items[thing]))
                ii += 1
    screen.blit(lan_suf, (115,540))

def draw_things(screen, items, craft):
    for thing in items:
        if thing not in craft:
            if items[thing]:
                lan_suf


def drawing(suf,items):
    items_list = [['dahuoshi','cao','shu','shumiao','eluanshi'],['yanshi','gancao','mutou','xizhi','chuizi'],['futou','huoba','huodui','zhangpeng']]
    screen.blit(suf, (100,40))
    pygame.draw.rect(suf, (255,255,255), ( 20, 20, 660, 460))
    pygame.draw.rect(suf, (200,200,200), ( 30, 40, 320, 420))
    for i in range(5):
        for j in range(6):
            pygame.draw.rect(suf, (255,255,255), (45+i*60, 60+j*60, 50,50))
    n = 0
    for a in items_list:
        m = 0
        for b in a:
            print_text(suf,45+m*60, 60+n*60, str(items[b]))
            m += 1
        n += 1

    pygame.draw.rect(suf, (200,200,200), (455, 100, 100, 100))
    pygame.draw.rect(suf, (255,255,255), (465, 110, 80, 80))

    pygame.draw.rect(suf, (200,200,200), (382, 220, 250, 60))
    for i in range(4):
        pygame.draw.rect(suf, (255,255,255), (392 + 60*i,225, 50,50))

    pygame.draw.rect(suf, (200,200,200), (455, 310, 100, 60))
    pygame.draw.rect(suf, (255,255,255), (460, 315, 90, 50))
    suf.blit(maked, (460,315))

font = pygame.font.Font(None, 18)
def print_text(suf, x, y, text):
    imgText = font.render(text, True, (0,0,0))
    suf.blit(imgText, (x,y))


def colli(suf,craft,iwant,pos):
    if suf and Rect(205,100,50,50).collidepoint(pos):
        print(2)
        if 'cao' in craft:
            iwant = 'cao'
        else:
            iwant = ''
    elif suf and Rect(265,100,50,50).collidepoint(pos):
        print(3)
        if 'shu' in craft:
            iwant = 'shu'
        else:
            iwant = ''
    elif suf and Rect(325,100,50,50).collidepoint(pos):
        print(4)
        if 'shumiao' in craft:
            iwant = 'shumiao'
        else:
            iwant = ''
    elif suf and Rect(385,100,50,50).collidepoint(pos):
        print(5)
        if 'eluanshi' in craft:
            iwant = 'eluanshi'
        else:
            iwant = ''
    elif suf and Rect(145,160,50,50).collidepoint(pos):
        print(6)
        if 'yanshi' in craft:
            iwant = 'yanshi'
        else:
            iwant = ''
    elif suf and Rect(205,160,50,50).collidepoint(pos):
        print(7)
        if 'gancao' in craft:
            iwant = 'gancao'
        else:
            iwant = ''
    elif suf and Rect(265,160,50,50).collidepoint(pos):
        print(8)
        if 'mutou' in craft:
            iwant = 'mutou'
        else:
            iwant = ''
    elif suf and Rect(325,160,50,50).collidepoint(pos):
        if 'xizhi' in craft:
            iwant = 'xizhi'
        else:
            iwant = ''
        print(9)
    elif suf and Rect(385,160,50,50).collidepoint(pos):
        print(10)
        if 'chuizi' in craft:
            iwant = 'chuizi'
        else:
            iwant = ''
    elif suf and Rect(145,220,50,50).collidepoint(pos):
        print(11)
        if 'futou' in craft:
            iwant = 'futou'
        else:
            iwant = ''
    elif suf and Rect(205,220,50,50).collidepoint(pos):
        print(12)
        if 'huoba' in craft:
            iwant = 'huoba'
        else:
            iwant = ''
    elif suf and Rect(265,220,50,50).collidepoint(pos):
        print(13)
        if 'huodui' in craft:
            iwant = 'huodui'
        else:
            iwant = ''
    elif suf and Rect(325,220,50,50).collidepoint(pos):
        print(14)
        if 'zhangpeng' in craft:
            iwant = 'zhangpeng'
        else:
            iwant = ''
    return iwant


class Player(object):
    def __init__(self):
        self.img = []
        for i in range(5):
            aa = pygame.image.load('lesson18/image/ren/'+ str(i+1) + '.png').convert_alpha()
            aa = pygame.transform.smoothscale(aa, (36,36))
            self.img.append(aa)
        self.image = self.img[1]
        self.pos = [10,5]
        self.x = self.pos[0]*30
        self.y = self.pos[1]*30
        self.frame = 0
        self.last_time = 0
        self.old_frame = -1
        self.num = 1
        self.time = 0

    def draw(self):
        screen.blit(self.image, (self.x,self.y))

    def update(self,current_time):
        if self.num == 4:
            self.time += 1
            if self.time >= 10:
                self.time = 0
                self.num = 1
        if current_time > self.last_time:
            self.frame += 1
            if self.frame > self.num:
                self.frame = 0
            self.last_time = current_time
        if self.frame != self.old_frame:
            self.image = self.img[self.frame]
            self.old_frame = self.frame

        self.x = self.pos[0]*30
        self.y = self.pos[1]*30

    def moveUp(self):
        self.pos[1] -= 1
        if self.pos[1] <= 0:
            self.pos[1] = 0

    def moveDown(self):
        self.pos[1] += 1
        if self.pos[1] >= 19:
            self.pos[1] = 19

    def moveLeft(self):
        self.pos[0] -= 1
        if self.pos[0] <= 0:
            self.pos[0] = 0

    def moveRight(self):
        self.pos[0] += 1
        if self.pos[0] >= 29:
            self.pos[0] = 29

    def get(self):
        self.num = 4

bac = pygame.image.load('lesson18/image/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (900,600))
flint = pygame.image.load('lesson18/image/flint.png').convert_alpha()
dahuoshi = pygame.transform.smoothscale(flint, (50,50))
flint1 = pygame.transform.smoothscale(flint, (30,30))
grass = pygame.image.load('lesson18/image/grass.png').convert_alpha()
cao = pygame.transform.smoothscale(grass, (50,50))
grass1 = pygame.image.load('lesson18/image/grass0.png').convert_alpha()
grass1 = pygame.transform.smoothscale(grass1, (30,30))
grass2 = pygame.image.load('lesson18/image/grass1.png').convert_alpha()
grass2 = pygame.transform.smoothscale(grass2, (30,30))
grass3 = pygame.image.load('lesson18/image/grass2.png').convert_alpha()
grass3 = pygame.transform.smoothscale(grass3, (30,30))
hay = pygame.image.load('lesson18/image/hay.png').convert_alpha()
gancao = pygame.transform.smoothscale(hay, (50,50))
hay1 = pygame.transform.smoothscale(hay, (30,30))
tree = pygame.image.load('lesson18/image/tree.png').convert_alpha()
shu = pygame.transform.smoothscale(tree, (50,50))
log = pygame.image.load('lesson18/image/log.png').convert_alpha()
mutou = pygame.transform.smoothscale(log, (50,50))
sapling = pygame.image.load('lesson18/image/sapling2.png').convert_alpha()
shumiao = pygame.transform.smoothscale(sapling, (50,50))
sapling1 =pygame.image.load('lesson18/image/sapling.png').convert_alpha()
sapling1 = pygame.transform.smoothscale(sapling1, (30,30))
twig = pygame.image.load('lesson18/image/twig.png').convert_alpha()
xizhi = pygame.transform.smoothscale(twig, (50,50))
boulder1 = pygame.image.load('lesson18/image/boulder.png').convert_alpha()
boulder1 = pygame.transform.smoothscale(boulder1, (30,30))
boulder = pygame.image.load('lesson18/image/boulder2.png').convert_alpha()
eluanshi = pygame.transform.smoothscale(boulder, (50,50))
rock = pygame.image.load('lesson18/image/rock.png').convert_alpha()
yanshi = pygame.transform.smoothscale(rock, (50,50))
pickaxe = pygame.image.load('lesson18/image/pickaxe.png').convert_alpha()
chuizi = pygame.transform.smoothscale(pickaxe, (50,50))
axe = pygame.image.load('lesson18/image/axe.png').convert_alpha()
futou = pygame.transform.smoothscale(axe, (50,50))
firepit = pygame.image.load('lesson18/image/firepit.png').convert_alpha()
huodui = pygame.transform.smoothscale(firepit, (50,50))
tent = pygame.image.load('lesson18/image/tent.png').convert_alpha()
zhangpeng = pygame.transform.smoothscale(tent, (50,50))
torch = pygame.image.load('lesson18/image/torch.png').convert_alpha()
huoba = pygame.transform.smoothscale(torch, (50,50))
water = pygame.image.load('lesson18/image/water.png').convert_alpha()
water = pygame.transform.smoothscale(water, (50,50))
water1 = pygame.transform.smoothscale(water, (30,30))
dirt = pygame.Surface((30, 30))
#dirt.set_alpha(0)
rock1 = pygame.image.load('lesson18/image/rock1.png').convert_alpha()
rock1 = pygame.transform.smoothscale(rock1, (30,30))
rock2 = pygame.image.load('lesson18/image/rock2.png').convert_alpha()
rock2 = pygame.transform.smoothscale(rock2, (30,30))
rock3 = pygame.image.load('lesson18/image/rock3.png').convert_alpha()
rock3 = pygame.transform.smoothscale(rock3, (30,30))
rock4 = pygame.image.load('lesson18/image/rock4.png').convert_alpha()
rock4 = pygame.transform.smoothscale(rock4, (30,30))
tree1 = pygame.image.load('lesson18/image/tree1.png').convert_alpha()
tree1 = pygame.transform.smoothscale(tree1, (30,30))
tree2 = pygame.image.load('lesson18/image/tree2.png').convert_alpha()
tree2 = pygame.transform.smoothscale(tree2, (30,30))
tree3 = pygame.image.load('lesson18/image/tree3.png').convert_alpha()
tree3 = pygame.transform.smoothscale(tree3, (30,30))
tree4 = pygame.image.load('lesson18/image/tree4.png').convert_alpha()
tree4 = pygame.transform.smoothscale(tree4, (30,30))

bag = pygame.image.load('lesson18/image/bag.png').convert_alpha()
bag = pygame.transform.smoothscale(bag, (50,50))

maked = pygame.image.load('lesson18/image/make.png').convert_alpha()
maked = pygame.transform.smoothscale(maked, (90,50))

map = [
          [20,21,20,21,20,21,18,15,16,17,11,12,17,15,16,15,19,19,19,19,19,10,10,10,10,10,10,10,10,19],
          [22,23,22,23,22,23,18,17,15,15,13,14,15,17,15,16,17,19,19,19,10,10,10,10,19,19,10,19,10,10],
          [16,18,17,20,21,18,17,18,15,16,16,17,15,16,17,17,17,15,19,19,19,10,10,10,10,19,19,19,19,19],
          [20,21,17,22,23,20,21,15,16,17,17,15,16,17,17,18,18,16,17,16,19,19,19,19,19,19,19,19,19,19],
          [22,23,18,16,16,22,23,24,24,25,25,25,16,16,15,16,17,15,17,15,16,15,20,21,15,16,19,19,19,19],
          [25,25,25,24,24,24,24,25,25,25,25,25,25,25,16,17,15,16,15,16,16,15,22,23,11,12,17,15,19,19],
          [16,25,25,25,25,25,25,25,25,25,25,25,25,25,25,15,17,16,15,17,16,15,16,16,13,14,17,15,16,16],
          [16,15,25,25,25,25,25,25,25,25,25,25,25,25,25,25,17,17,15,16,17,15,17,17,15,16,15,15,15,17],
          [16,15,15,16,25,25,25,25,25,25,25,25,25,25,25,25,25,16,17,16,15,17,15,17,15,15,20,21,16,17],
          [15,16,16,15,16,16,25,25,25,25,25,25,25,25,25,25,25,17,15,18,15,16,17,17,17,16,22,23,17,17],
          [15,17,15,17,15,15,24,25,25,25,25,25,25,25,25,25,25,25,25,15,16,15,15,16,17,16,17,15,16,15],
          [15,17,20,21,15,16,18,24,25,25,25,25,25,25,24,24,25,25,25,25,16,16,17,15,16,15,16,16,15,17],
          [15,17,22,23,16,17,16,15,24,24,25,25,24,24,17,18,15,16,25,25,25,25,15,17,16,15,17,17,11,12],
          [17,15,16,15,16,16,16,15,17,16,24,24,15,17,15,15,15,18,15,24,25,25,25,25,17,15,16,17,13,14],
          [19,17,15,17,15,17,18,17,15,17,17,15,17,15,17,16,20,21,17,18,24,24,25,25,25,25,24,24,24,25],
          [19,19,15,16,17,17,17,15,16,17,15,18,15,16,16,15,22,23,17,15,16,17,24,24,16,15,25,25,25,25],
          [19,19,19,17,16,20,21,15,16,16,15,17,16,18,15,15,17,15,17,15,15,15,16,15,15,18,15,16,15,16],
          [10,19,19,19,15,22,23,17,15,15,15,16,15,17,16,17,15,17,16,15,17,15,15,15,15,16,15,15,17,15],
          [19,10,10,19,10,19,19,19,15,16,16,15,11,12,15,16,15,17,15,17,16,17,15,16,15,15,17,16,17,15],
          [19,19,19,19,19,19,19,19,19,19,16,15,13,14,15,17,17,15,15,16,17,16,17,15,16,15,15,15,16,16]
      ]

map_dict = {
                10:[flint1,'dahuoshi'],
                11:[rock1,'yanshi'],
                12:[rock2,'yanshi'],
                13:[rock3,'yanshi'],
                14:[rock4,'yanshi'],
                15:[grass2,'cao'],
                16:[grass3,'cao'],
                17:[grass1,'cao'],
                18:[sapling1,'shumiao'],
                19:[dirt,'dirt'],
                20:[tree1,'shu'],
                21:[tree2,'shu'],
                22:[tree3,'shu'],
                23:[tree4,'shu'],
                24:[boulder1,'eluanshi'],
                25:[water1,'water'],
            }



suf = ''
#an inventory of items
items = {
            "dahuoshi" : 0,   #打火石

            "cao" : 0,  #草
            "gancao" : 0,      #干草

            "shu" : 0,   #树
            "mutou" : 0,      #原木

            "shumiao" : 0, #树苗
            "xizhi" : 0,      #细枝

            "eluanshi" : 0,   #卵石
            "yanshi" : 0,       #岩石

            "chuizi" : 0,    #镐
            "futou" : 0,        #斧头

            "huodui" : 0,    #火堆
            "zhangpeng" : 0,       #帐篷

            "huoba" : 0,      #火把
        }



#rules to make new objects
craft = {
            "gancao" : { "cao" : 1 },
            "xizhi" : { "shumiao" : 1 },
            "mutou" : { "futou" : 1, "shu" : 1 },
            "futou" : { "xizhi" : 3, "dahuoshi" : 1 },
            "zhangpeng" : { "xizhi" : 10, "gancao" : 15 },
            "huodui" : { "eluanshi" : 5, "mutou" : 3, "xizhi" : 1, "huoba" : 1 },
            "huoba" : { "dahuoshi" : 1, "cao" : 1, "xizhi" : 1 },
            "chuizi" : { "dahuoshi" : 2, "xizhi" : 1 }
        }
iwant = ''

leo = Player()
times = pygame.time.Clock()
while True:
    ticks = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    draw_map(screen)
    leo.update(ticks)
    leo.draw()
    draw_lan(screen,items,craft)

    make = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if not suf and event.type == KEYDOWN:
            if event.key == K_UP:
                leo.moveUp()
            elif event.key == K_DOWN:
                leo.moveDown()
            elif event.key == K_LEFT:
                leo.moveLeft()
            elif event.key == K_RIGHT:
                leo.moveRight()
            elif event.key == K_SPACE:
                leo.get()
                if map_dict[map[leo.pos[1]][leo.pos[0]]][1] in items:
                    items[map_dict[map[leo.pos[1]][leo.pos[0]]][1]] += 10
                    map[leo.pos[1]][leo.pos[0]] = 19
        if event.type == MOUSEBUTTONDOWN:
            if Rect(727,545, 50,50).collidepoint(event.pos):
                if not suf:
                    suf = pygame.Surface((700, 500))
                    suf.fill((50,50,50))
                    #suf.set_alpha(210)
                elif suf:
                    suf = ''
            elif suf and Rect(145,100,50,50).collidepoint(event.pos):
                iwant = 'dahuoshi'
            iwant = colli(suf,craft,iwant,event.pos)

            if suf and Rect(555, 350, 100, 60).collidepoint(event.pos):
                make = True


    if suf:
        drawing(suf,items)
        if iwant in craft :
            suf.blit(my_dict[iwant], (480,125))
            num = 0
            for i in craft[iwant]:
                suf.blit(my_dict[i], (392+num*60,225))
                print_text(suf, 392+num*60, 225, str(craft[iwant][i]))
                num += 1
            kaiguan = True
            for i in craft[iwant]:
                if craft[iwant][i] > items[i]:
                    kaiguan = False
                    break

            if kaiguan and make:
                for i in craft[iwant]:
                    items[i] -= craft[iwant][i]
                items[iwant] += 1

                print("iwant crafted\n")


            if items["zhangpeng"] >= 1 and items["huodui"] >= 1:
                final = pygame.image.load('lesson18/image/cunhuo.png').convert_alpha()
                final = pygame.transform.smoothscale(final, (700,500))
                suf.blit(final,(8,12))


    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    times.tick(15)
    pygame.display.update()
