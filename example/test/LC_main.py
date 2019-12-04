#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pygame, sys, time
from pygame.locals import *
from LC_jiangshi_set import *


# 坚果
class Nut(pygame.sprite.Sprite):
    nut_list = []

    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image_new = image
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])

    def display(self, num):
        screen.blit(self.image_new[num % 14], self.rect)


# 土豆地雷爆炸效果
class Boom(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_new = [pygame.image.load("lessonC/image/dl" + str(i + 1) + ".png") for i in range(10)]
        self.image = self.image_new[0]
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])

    def display(self, num):
        screen.blit(self.image_new[(int(num / 3))], self.rect)


# 土豆
class Potato(pygame.sprite.Sprite):
    potato_list = []

    def __init__(self, pos, image, boom):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        self.pengzhuang = False
        self.boom = boom

    def display(self):
        screen.blit(self.image, self.rect)


# 豌豆子弹和仙人掌刺
class Bullet(pygame.sprite.Sprite):
    bullet_list = []  # 创建一个类对象

    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])

    def display(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(10, 0)
        # 如果越界移除子弹
        if self.rect.left > 750:
            Bullet.bullet_list.remove(self)


# 僵尸
class Zombie(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        jiangshiList = []
        for i in range(31):
            jiangshi = pygame.image.load("lessonC/image/js/js" + str(1 + i) + ".png").convert_alpha()
            jiangshi = pygame.transform.smoothscale(jiangshi, (60, 90))
            jiangshiList.append(jiangshi)
        self.image = jiangshi
        self.image_new = jiangshiList
        self.rect = self.image.get_rect()
        self.rect.move_ip(708, 88)

    def set_pos(self, position):
        self.rect.left = position[0]
        self.rect.top = position[1]

    def display(self, num):
        screen.blit(self.image_new[num % 31], self.rect)

    def moveup(self):
        if self.rect.top > 65:
            self.rect.move_ip(0, -5)
            for i in Nut.nut_list:
                if jiangshi.rect.colliderect(i.rect):
                    self.rect.move_ip(0, 5)

    def movedown(self):
        if self.rect.bottom < 580:
            self.rect.move_ip(0, 5)
            for i in Nut.nut_list:
                if jiangshi.rect.colliderect(i.rect):
                    self.rect.move_ip(0, -5)

    def moveleft(self):
        if self.rect.left > 90:
            self.rect.move_ip(-5, 0)
            for i in Nut.nut_list:
                if jiangshi.rect.colliderect(i.rect):
                    self.rect.move_ip(5, 0)

    def moveright(self):
        if self.rect.right < 790:
            self.rect.move_ip(5, 0)
            for i in Nut.nut_list:
                if jiangshi.rect.colliderect(i.rect):
                    self.rect.move_ip(-5, 0)


class Anjian(object):
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False


def show_bac(num):
    screen.blit(bac, (0, 0))  # 刷新背景
    m = num
    screen.blit(wandou_img_list[num % 13], (200, 385))  # 绘制豌豆到屏幕上
    screen.blit(wandou_img_list[num % 13], (200, 200))
    screen.blit(xianrz_img_list[num % 11], (455, 480))  # 绘制仙人掌到屏幕上
    pygame.draw.rect(screen, (235, 106, 72), (700, 77, 3, 495))  # 绘制起点红线
    if num % speed == 0:
        bullet0 = Bullet((240, 390), wdzd)
        bullet1 = Bullet((240, 205), wdzd)
        bullet2 = Bullet((495, 502), xrzzd_img)
        Bullet.bullet_list.extend([bullet0, bullet1, bullet2])
    # 显示所有豌豆子弹
    for i in Bullet.bullet_list:
        i.display()
        i.move()


def key_control():
    # 对事件进行处理 它监听的是一个列表
    for event in pygame.event.get():
        # 按下键盘的事件判断
        if event.type == KEYDOWN:
            # 判断具体的键
            if event.key == K_UP:
                anjian.up = "anxia"
            elif event.key == K_DOWN:
                anjian.down = "anxia"
            elif event.key == K_LEFT:
                anjian.left = "anxia"
            elif event.key == K_RIGHT:
                anjian.right = "anxia"
        elif event.type == KEYUP:
            # 判断具体的键
            if event.key == K_UP:
                anjian.up = False
            elif event.key == K_DOWN:
                anjian.down = False
            elif event.key == K_LEFT:
                anjian.left = False
            elif event.key == K_RIGHT:
                anjian.right = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


pygame.mixer.init()
pygame.init()  # 初始化
pygame.display.set_caption("Plants vs Zombies")

n = 0  # 控制图片
game = 0  # 控制游戏胜负
# 控制爆炸效果
z = -1
boom = None
k = 0
pengzhuang = False
speed = 100  # 子弹间隔，越大间隔越大

screen = pygame.display.set_mode((800, 600))  # 设置屏幕大小
clock = pygame.time.Clock()
# 背景
bac = pygame.image.load("lessonC/image/background1.png")
bac = pygame.transform.smoothscale(bac, (800, 600))
# 豌豆
wandou_img_list = []
for i in range(13):
    wandou_img = pygame.image.load("lessonC/image/wandou" + str(i + 1) + ".png")
    wandou_img = pygame.transform.smoothscale(wandou_img, (60, 60))
    wandou_img_list.append(wandou_img)
# 豌豆子弹
wdzd = pygame.image.load('lessonC/image/dou.png')
wdzd = pygame.transform.smoothscale(wdzd, (28, 28))
# 仙人掌
xianrz_img_list = []
for i in range(11):
    xianrz_img = pygame.image.load("lessonC/image/xianrenzhang" + str(i + 1) + ".png")
    xianrz_img = pygame.transform.smoothscale(xianrz_img, (60, 70))
    xianrz_img_list.append(xianrz_img)
# 仙人掌子弹
xrzzd_img = pygame.image.load('lessonC/image/ci.png')
xrzzd_img = pygame.transform.scale(xrzzd_img, (15, 15))
# 坚果
nut_img_list = []
for i in range(14):
    nut_img = pygame.image.load("lessonC/image/nut" + str(i + 1) + ".png")
    nut_img = pygame.transform.smoothscale(nut_img, (55, 80))
    nut_img_list.append(nut_img)
# 土豆
potato_img = pygame.image.load("lessonC/image/potato.png")
# 胜利
victory_img = pygame.image.load("lessonC/image/victory.png")
victory_img = pygame.transform.smoothscale(victory_img, (500, 300))
# 失败
defeat_img = pygame.image.load("lessonC/image/defeat.png")
defeat_img = pygame.transform.smoothscale(defeat_img, (500, 300))
# 背景音乐
pygame.mixer.music.load('lessonC/music/music.mp3')
# pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(5)
# 胜利音效
victory_sound = pygame.mixer.Sound('lessonC/music/victory.wav')
# victory_sound.set_volume(0.2)
# 失败音效
defeat_sound = pygame.mixer.Sound('lessonC/music/defeat.wav')
# defeat_sound.set_volume(0.2)

# 创建对象
anjian = Anjian()
jiangshi = Zombie()
jianguo61 = Nut((590, 190), nut_img_list)
jianguo70 = Nut((647, 88), nut_img_list)
jianguo71 = Nut((645, 193), nut_img_list)
jianguo81 = Nut((700, 193), nut_img_list)
jianguo23 = Nut((331, 393), nut_img_list)
jianguo63 = Nut((580, 390), nut_img_list)
jianguo64 = Nut((580, 490), nut_img_list)
jianguo10 = Nut((265, 85), nut_img_list)
Nut.nut_list.extend([jianguo10, jianguo23, jianguo61, jianguo63, jianguo64, jianguo70, jianguo71, jianguo81])
boom0 = Boom((455, 300))
boom1 = Boom((330, 300))
boom2 = Boom((200, 500))
boom3 = Boom((710, 400))
boom4 = Boom((710, 490))
boom5 = Boom((640, 400))
boom6 = Boom((640, 490))
boom7 = Boom((385, 100))
boom8 = Boom((455, 100))
tudou42 = Potato((455, 300), potato_img, boom0)
tudou22 = Potato((330, 300), potato_img, boom1)
tudou04 = Potato((200, 500), potato_img, boom2)
tudou83 = Potato((710, 400), potato_img, boom3)
tudou84 = Potato((715, 490), potato_img, boom4)
tudou73 = Potato((645, 400), potato_img, boom5)
tudou74 = Potato((645, 490), potato_img, boom6)
tudou30 = Potato((385, 100), potato_img, boom7)
tudou40 = Potato((455, 100), potato_img, boom8)
Potato.potato_list.extend([tudou04, tudou22, tudou30, tudou40, tudou42, tudou73, tudou74, tudou83, tudou84])

# 红线
win_rect = pygame.Rect(0, 0, 155, 600)

# 设置僵尸初始位置
if set_pos():
    jiangshi.rect.topleft = set_pos()

# 游戏主循环
while True:
    print(pygame.mouse.get_pos())  # 打印鼠标位置坐标

    show_bac(n)  # 显示背景、植物、子弹
    # 显示坚果
    for i in Nut.nut_list:
        i.display(n)

    key_control()  # 按键控制

    if pengzhuang:
        z += 1
        if z == 0:
            boom = Potato.potato_list[k].boom
            Potato.potato_list.pop(k)
        elif z < 30:
            boom.display(z)
            for i in Potato.potato_list:
                i.display()
        else:
            for i in Potato.potato_list:
                i.display()
            game = "lose"
            screen.blit(defeat_img, (200, 100))
            break
    else:
        for i in Potato.potato_list:
            i.display()
        move(jiangshi, anjian)

    # 如果子弹碰撞到僵尸,结束
    for item in Bullet.bullet_list:
        if (pygame.sprite.collide_mask(jiangshi, item)):
            game = "lose"
    # 判断是否碰到炸弹
    for i in range(len(Potato.potato_list)):
        if jiangshi.rect.colliderect(Potato.potato_list[i].rect):
            pengzhuang = True
            k = i
    n += 1
    if game:
        break
    else:
        jiangshi.display(n)
    if jiangshi.rect.colliderect(win_rect):
        game = "win"

    clock.tick(15)  # 每秒15帧
    pygame.display.update()
# 切换声音
if game == "lose":
    pygame.mixer.music.stop()
    defeat_sound.play()
elif game == "win":
    pygame.mixer.music.stop()
    victory_sound.play()

while True:
    clock.tick(25)  # 每秒25帧
    if game == "lose":
        screen.blit(defeat_img, (200, 100))
    elif game == "win":
        screen.blit(victory_img, (200, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
