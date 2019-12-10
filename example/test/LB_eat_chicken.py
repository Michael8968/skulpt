#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pygame, sys, time,random
from pygame.locals import *
from LB_set import *
from pygame import Rect
pygame.mixer.init()
pygame.init()  # 初始化
screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("绝地求生2D版")
#############变量#############################
selectImg1List = []
selectImg2List = []
selectImg3List = []
peopleNoGunImgList = []
peopleNoGunImgList2 = []
peopleNoGunImgList3 = []
peopleHaveGunImgList = []
peopleHaveGunImgList1 = []
peopleHaveGunImgList2 = []
peopleHaveGunImgList3 = []
peoplePickGunImgList = []
peoplePickGunImgList2 = []
peoplePickGunImgList3 = []
sceneChangeImgList = []
enemyImg1List = []
enemyImg2List = []
enemyImg3List = []
scoreImgList = []
timeImgList = []
signImgList = []
n = 0  # 控制图片
k = 0  # 控制转场弹窗遮罩的横坐标
m = 0  # 控制弹窗上遮罩的横坐标
aa = 0 # 控制转场图片切换
bb = 0 # 控制转场图片切换
mm = 0 # 控制飞机
time_1 = 0 # 用于计时
time_2 = 0
time_out = 0 # 倒计时结束的标志
anjian1 = 0
anjian = 0
clothColor = 0
enemyPos = None
Music1 = "lessonB/music/bac1.mp3"
Music2 = "lessonB/music/bac3.ogg"
tanchuang = False # 弹窗
load = False # 加载页面
zhuanchang = '军事基地' # 切换场景
current_time = -1
old_time = -1
shoot = False
score = 0
game = None
sign = False
Fullscreen = False
mouseMotion = False
restart = False
Shoot = True
clock = pygame.time.Clock()
##################image################
bac = pygame.image.load("lessonB/image/beijing.png")
bac = pygame.transform.smoothscale(bac, (960, 720))
littleRoomImg = pygame.image.load("lessonB/image/fangwuxiao.png")
littleRoomImg = pygame.transform.smoothscale(littleRoomImg, (248, 158))
bigRoomImg = pygame.image.load("lessonB/image/fangwuda.png")
bigRoomImg = pygame.transform.smoothscale(bigRoomImg, (376, 222))
horizontalWallImg = pygame.image.load("lessonB/image/qiangheng.png")
horizontalWallImg = pygame.transform.smoothscale(horizontalWallImg, (398, 48))
longitudinalWallImg = pygame.image.load("lessonB/image/qiangshu.png")
longitudinalWallImg = pygame.transform.smoothscale(longitudinalWallImg, (28, 330))
towerImg = pygame.image.load("lessonB/image/liaowangta.png")
towerImg = pygame.transform.smoothscale(towerImg, (136, 218))
carImg = pygame.image.load("lessonB/image/qiche.png")
carImg = pygame.transform.smoothscale(carImg, (200, 110))
frameImg = pygame.image.load("lessonB/image/mujia.png")
frameImg = pygame.transform.smoothscale(frameImg, (166, 146))
oilDrumImg = pygame.image.load("lessonB/image/youtong.png")
oilDrumImg = pygame.transform.smoothscale(oilDrumImg, (62, 68))
sandBagImg = pygame.image.load("lessonB/image/shadai.png")
sandBagImg = pygame.transform.smoothscale(sandBagImg, (134, 74))
fireBucketImg = pygame.image.load("lessonB/image/huotong.png")
fireBucketImg = pygame.transform.smoothscale(fireBucketImg, (52, 78))
packageImg = pygame.image.load("lessonB/image/bujixiang.png")
packageImg = pygame.transform.smoothscale(packageImg, (90, 94))
buttonImg = pygame.image.load("lessonB/image/anniu.png")
buttonImg = pygame.transform.smoothscale(buttonImg, (368, 170))
buttonImg1 = pygame.image.load("lessonB/image/anniu2.png")
buttonImg1 = pygame.transform.smoothscale(buttonImg1, (368, 170))
bac0 = pygame.image.load("lessonB/image/bac.png")
bac0 = pygame.transform.smoothscale(bac0, (960, 720))
bac1 = pygame.image.load("lessonB/image/changjing2/beijing22.png")
bac1 = pygame.transform.smoothscale(bac1, (960, 720))
propImg = pygame.image.load("lessonB/image/changjing2/daoju2.png")
propImg = pygame.transform.smoothscale(propImg, (960, 720))
peopleBulletImg = pygame.image.load("lessonB/image/changjing2/wanjiazidan.png")
peopleBulletImg = pygame.transform.smoothscale(peopleBulletImg, (28, 16))
enemyBulletImg = pygame.image.load("lessonB/image/changjing2/direnzidan.png")
enemyBulletImg = pygame.transform.flip(enemyBulletImg, True, False)
enemyBulletImg = pygame.transform.smoothscale(enemyBulletImg, (18, 12))
winImg = pygame.image.load("lessonB/image/win.png")
winImg = pygame.transform.smoothscale(winImg, (960, 720))
loseImg = pygame.image.load("lessonB/image/lose.png")
loseImg = pygame.transform.smoothscale(loseImg, (960, 720))
signImg1 = pygame.image.load("lessonB/image/biaozhi1.png")
signImg1 = pygame.transform.smoothscale(signImg1, (134, 154))
signImg2 = pygame.image.load("lessonB/image/biaozhi2.png")
signImg2 = pygame.transform.smoothscale(signImg2, (134, 154))
signImgList.append(signImg1)
signImgList.append(signImg2)
scoreImg = pygame.image.load("lessonB/image/score/score.png")
scoreImg = pygame.transform.smoothscale(scoreImg, (240, 58))
timeoutImg =  pygame.image.load("lessonB/image/timeout.png")
replayImg = pygame.image.load("lessonB/image/replay.png")
replayImg = pygame.transform.smoothscale(replayImg, (274, 94))
replayImg1 = pygame.transform.smoothscale(replayImg, (294, 114))
replayImg2 = pygame.image.load("lessonB/image/replay1.png")
replayImg2 = pygame.transform.smoothscale(replayImg2, (274, 94))
replayImg3 = pygame.transform.smoothscale(replayImg2, (294, 114))
replayImg3 = pygame.transform.smoothscale(replayImg2, (294, 114))
tipImg1 = pygame.image.load("lessonB/image/tishi1.png")
#tipImg1 = pygame.transform.smoothscale(tipImg1, (960, 720))
tipImg2 = pygame.image.load("lessonB/image/tishi2.png")
#tipImg2 = pygame.transform.smoothscale(tipImg2, (960, 720))
tipImg3 = pygame.image.load("lessonB/image/tishi3.png")
#tipImg3 = pygame.transform.smoothscale(tipImg3, (960, 720))
for i in range(4):
    sceneChangeImg = pygame.image.load("lessonB/image/zhuanchang/" + str(i+1) + ".png")
    sceneChangeImg = pygame.transform.smoothscale(sceneChangeImg, (960, 720))
    sceneChangeImgList.append(sceneChangeImg)
for i in range(16):
    peopleNoGunImg = pygame.image.load("lessonB/image/jiaose/wuqiang/" + str(i + 1) + ".png")
    peopleNoGunImg = pygame.transform.smoothscale(peopleNoGunImg, (56, 77))
    peopleNoGunImgList.append(peopleNoGunImg)
for i in range(16):
    peopleNoGunImg2 = pygame.image.load("lessonB/image/jiaose/wuqiang2/" + str(i + 1) + ".png")
    peopleNoGunImg2 = pygame.transform.smoothscale(peopleNoGunImg2, (56, 77))
    peopleNoGunImgList2.append(peopleNoGunImg2)
for i in range(16):
    peopleNoGunImg3 = pygame.image.load("lessonB/image/jiaose/wuqiang3/" + str(i + 1) + ".png")
    peopleNoGunImg3 = pygame.transform.smoothscale(peopleNoGunImg3, (56, 77))
    peopleNoGunImgList3.append(peopleNoGunImg3)
for i in range(4):
    peopleHaveGunImg = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng/" + str(i + 1) + ".png")
    peopleHaveGunImg = pygame.transform.smoothscale(peopleHaveGunImg, (100, 100))
    peopleHaveGunImgList.append(peopleHaveGunImg)
for i in range(4):
    peopleHaveGunImg2 = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng2/" + str(i + 1) + ".png")
    peopleHaveGunImg2 = pygame.transform.smoothscale(peopleHaveGunImg2, (100, 100))
    peopleHaveGunImgList2.append(peopleHaveGunImg2)
for i in range(4):
    peopleHaveGunImg3 = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng3/" + str(i + 1) + ".png")
    peopleHaveGunImg3 = pygame.transform.smoothscale(peopleHaveGunImg3, (100, 100))
    peopleHaveGunImgList3.append(peopleHaveGunImg3)
for i in range(4):
    peopleHaveGunImg0 = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng/" + str(i + 1) + ".png")
    peopleHaveGunImg0 = pygame.transform.smoothscale(peopleHaveGunImg0, (80, 80))
    peopleHaveGunImgList1.append(peopleHaveGunImg0)
for i in range(4):
    peoplePickGunImg = pygame.image.load("lessonB/image/jiaose/jiandaoqiang/" + str(i + 1) + ".png")
    peoplePickGunImg = pygame.transform.smoothscale(peoplePickGunImg, (82, 70))
    peoplePickGunImgList.append(peoplePickGunImg)
for i in range(4):
    peoplePickGunImg2 = pygame.image.load("lessonB/image/jiaose/jiandaoqiang2/" + str(i + 1) + ".png")
    peoplePickGunImg2 = pygame.transform.smoothscale(peoplePickGunImg2, (82, 70))
    peoplePickGunImgList2.append(peoplePickGunImg2)
for i in range(4):
    peoplePickGunImg3 = pygame.image.load("lessonB/image/jiaose/jiandaoqiang3/" + str(i + 1) + ".png")
    peoplePickGunImg3 = pygame.transform.smoothscale(peoplePickGunImg3, (82, 70))
    peoplePickGunImgList3.append(peoplePickGunImg3)
for i in range(21):
    digitalImg = pygame.image.load("lessonB/image/score/"+str(i) + ".png")
    scoreImgList.append(digitalImg)
for i in range(11):
    timeImg = pygame.image.load("lessonB/image/time/"+str(i) + ".png")
    timeImgList.append(timeImg)

for i in range(4):
    enemyImg1 = pygame.image.load("lessonB/image/jiaose/diren4/" + str(i + 1) + ".png")
    enemyImg1 = pygame.transform.flip(enemyImg1, True, False)
    enemyImg1 = pygame.transform.smoothscale(enemyImg1, (108, 92))
    enemyImg1List.append(enemyImg1)
for i in range(4):
    enemyImg2 = pygame.image.load("lessonB/image/jiaose/diren5/" + str(i + 1) + ".png")
    enemyImg2 = pygame.transform.flip(enemyImg2, True, False)
    enemyImg2 = pygame.transform.smoothscale(enemyImg2, (108, 92))
    enemyImg2List.append(enemyImg2)
for i in range(4):
    enemyImg3 = pygame.image.load("lessonB/image/jiaose/diren3/fanzhuan/" + str(i + 1) + ".png")
    enemyImg3 = pygame.transform.smoothscale(enemyImg3, (114, 92))
    enemyImg3List.append(enemyImg3)
for i in range(4):
    selectImg1 = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng/" + str(i + 1) + ".png")
    selectImg1 = pygame.transform.smoothscale(selectImg1, (128, 132))
    selectImg1List.append(selectImg1)
    selectImg2 = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng2/" + str(i + 1) + ".png")
    selectImg2 = pygame.transform.smoothscale(selectImg2, (128, 132))
    selectImg2List.append(selectImg2)
    selectImg3 = pygame.image.load("lessonB/image/jiaose/hengbanjuediqiusheng3/" + str(i + 1) + ".png")
    selectImg3 = pygame.transform.smoothscale(selectImg3, (128, 132))
    selectImg3List.append(selectImg3)

planeImg1 = pygame.image.load("lessonB/image/plane1.png")
planeImg1 = pygame.transform.smoothscale(planeImg1, (472, 366))
planeImg2 = pygame.image.load("lessonB/image/plane2.png")
planeImg2 = pygame.transform.smoothscale(planeImg2, (472, 366))
parachuteImg = pygame.image.load("lessonB/image/Parachute.png")
parachuteImg = pygame.transform.smoothscale(parachuteImg, (260, 266))
#####################music##################################
footstepsSound = pygame.mixer.Sound('lessonB/music/footOnSand.wav')
#footstepsSound.set_volume(0.2)
shootSound = pygame.mixer.Sound('lessonB/music/shoot.wav')
#shootSound.set_volume(0.3)


# 障碍
class Father(pygame.sprite.Sprite):

    def __init__(self, image, topleft):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def display(self):
        screen.blit(self.image, self.rect)


# 主角
class People(pygame.sprite.Sprite):

    def __init__(self, img1, img2, img3, topleft, footstepsSound):
        pygame.sprite.Sprite.__init__(self)
        self.peopleNoGunImgList = img1
        self.peopleHaveGunImgList = img2
        self.peoplePickGunImgList = img3
        self.noGunUp = self.peopleNoGunImgList[:4]
        self.noGunDown = self.peopleNoGunImgList[12:16]
        self.noGunLeft = self.peopleNoGunImgList[8:12]
        self.noGunRight = self.peopleNoGunImgList[4:8]
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.transformSpeed = 3 # 图片切换速度控制
        self.block = 10 # 单次移动像素
        self.direction = 0 # 方向
        self.tmp = 0 # 变量，用于人物边界问题
        self.image = self.noGunDown[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.footstepsSound = footstepsSound

    def display(self):
        screen.blit(self.image, self.rect)

    # 人物和场景一中的障碍碰撞
    def is_collide(self):
        for i in group.sprites():
            if pygame.sprite.collide_mask(self, i):
                return True
        return False

    def change_cloth(self, img1, img2, img3):
        self.peopleNoGunImgList = img1
        self.peopleHaveGunImgList = img2
        self.peoplePickGunImgList = img3
        self.noGunUp = self.peopleNoGunImgList[:4]
        self.noGunDown = self.peopleNoGunImgList[12:16]
        self.noGunLeft = self.peopleNoGunImgList[8:12]
        self.noGunRight = self.peopleNoGunImgList[4:8]
        self.image = self.noGunDown[0]

    # 用于场景二，更新位置和图片
    def update(self, num):
        #move = False
        if self.up:
            #move = True
            self.direction = "up"
            self.image = self.noGunUp[num % 4]
            #screen.blit(self.noGunUp[2],(0,0))
            if self.rect.top - self.block < 0:
                self.tmp = self.rect.top
                self.rect.top = 0
                if self.is_collide():
                    self.rect.top = self.tmp
            else:
                self.rect.top -= self.block
                if self.is_collide():
                    self.rect.top += self.block
        elif self.down:
            #move = True
            self.direction = "down"
            self.image = self.noGunDown[num % 4]
            if self.rect.bottom + self.block > 720:
                self.tmp = self.rect.bottom
                self.rect.bottom = 720
                if self.is_collide():
                    self.rect.bottom = self.tmp
            else:
                self.rect.bottom += self.block
                if self.is_collide():
                    self.rect.bottom -= self.block
        elif self.left:
            #move = True
            self.direction = "left"
            self.image = self.noGunLeft[num % 4]
            if self.rect.left - self.block < 0:
                self.tmp = self.rect.left
                self.rect.left = 0
                if self.is_collide():
                    self.rect.left = self.tmp
            else:
                self.rect.left -= self.block
                if self.is_collide():
                    self.rect.left += self.block
        elif self.right:
            #move = True
            self.direction = "right"
            self.image = self.noGunRight[num % 4]
            if self.rect.right + self.block > 960:
                self.tmp = self.rect.right
                self.rect.right = 960
                if self.is_collide():
                    self.rect.right = self.tmp
            else:
                self.rect.right += self.block
                if self.is_collide():
                    self.rect.left -= self.block
        # if move:
        #     self.play_sound()

    # 用于场景三，更新位置和图片
    def update1(self, num):
        if self.up:
            self.image = self.peopleHaveGunImgList[num // self.transformSpeed % 4]
            if self.rect.top - self.block < 30:
                self.rect.top = 30
            else:
                self.rect.top -= self.block
        elif self.down:
            self.image = self.peopleHaveGunImgList[num // self.transformSpeed % 4]
            if self.rect.bottom + self.block > 720:
                self.rect.bottom = 720
            else:
                self.rect.bottom += self.block
        elif self.left:
            self.image = self.peopleHaveGunImgList[num // self.transformSpeed % 4]
            if self.rect.left - self.block < 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.block
        elif self.right:
            self.image = self.peopleHaveGunImgList[num // self.transformSpeed % 4]
            if self.rect.right + self.block > 333:
                self.rect.right = 333
            else:
                self.rect.right += self.block

    def play_sound(self):
        self.footstepsSound.play(0, 200)

    def moveup(self):
        self.up = True

    def movedown(self):
        self.down = True

    def moveleft(self):
        self.left = True

    def moveright(self):
        self.right = True


# 子弹
class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, pos, top, left, block):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.rect.top += top
        self.rect.left += left
        self.block = block # 子弹移动像素

    def update(self, n):
        self.rect.left = self.rect.left + self.block
        if self.rect.left < 0 and self in enemyBulletGroup.sprites():
            enemyBulletGroup.remove(self)
        if self.rect.left > 960 and self in peopleBulletGroup.sprites():
            peopleBulletGroup.remove(self)


# 敌人
class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, num=1):
        pygame.sprite.Sprite.__init__(self)
        self.enemyImg = img
        self.image = self.enemyImg[0]
        self.rect = self.image.get_rect()
        self.transformSpeed = 3 # 敌人图片切换速度
        # 划分五个格子，敌人出现位置
        if num:
            num -= 1
        else:
            num = 0
        if num == 0:
            self.rect.topleft = (960, 32)
        elif num == 1:
            self.rect.topleft = (960, 148)
        elif num == 2:
            self.rect.topleft = (960, 264)
        elif num == 3:
            self.rect.topleft = (960, 380)
        elif num == 4 :
            self.rect.topleft = (960, 496)
        self.block = 3  # 敌人移动像素
        self.step = random.randint(30, 60)
        self.a = -1
        self.oldTime = time.time()
        self.currentTime = 0
    def update(self, num):
        if self.step:
            self.step -= 1
            if self.rect.bottom < 370:
                if self.rect.left - self.block < 310:
                    self.rect.left = 310
                else:
                    self.rect.left -= self.block
            else:
                if self.rect.left - self.block < 333:
                    self.rect.left = 333
                else:
                    self.rect.left -= self.block
            if self.step == 0:  # 确定站立图片
                self.image = self.enemyImg[0]
            else:
                self.image = self.enemyImg[num // self.transformSpeed % 4]
        else:
            self.a += 1
            if self.a == 0:
                self.oldTime = time.time()
            self.currentTime = time.time()
            if self.currentTime - self.oldTime > 1.5:
                enemyBullet = Bullet(enemyBulletImg, self.rect.topleft, 65, 0, -20)
                enemyBulletGroup.add(enemyBullet)
                self.oldTime =self.currentTime
                self.step = random.randint(30, 60)
                self.a = -1
            # if self.a == 30:
            #     enemyBullet = Bullet(enemyBulletImg, self.rect.topleft, 65, 0, -20)
            #     enemyBulletGroup.add(enemyBullet)
            # if not self.a:
            #     self.step = random.randint(30, 60)
            #     self.a = 50

    def display(self):
        screen.blit(self.image, self.rect)


# 我方子弹和敌人碰撞
def if_collide(group1, group2):
    return len(pygame.sprite.groupcollide(group1, group2, True, True))


# 敌方子弹与我碰撞
def is_collide(spider, group):
    return pygame.sprite.spritecollide(spider, group, True)


def tip_collide(rect1, rect2, img):
    if pygame.Rect.colliderect(rect1, rect2):
        screen.blit(img, (318, 677))


def popup(rect1, rect2, n):
    rectX = n
    if pygame.Rect.colliderect(rect1, rect2):
        rectX += 10
        if not time_out:
            screen.blit(buttonImg1, (310, 254))
        if rectX < 233:
            pygame.draw.rect(screen, (190, 195, 209), (359 + rectX, 314, 272 - rectX, 40), 0)
        return rectX
    else:
        rectX = 0
        return rectX


def draw(n):
    # 绘制背景和道具
    screen.blit(bac1, (0, 0))
    screen.blit(propImg, (0, 0))
    # 更新并绘制敌人
    enemyGroup.update(n)
    enemyGroup.draw(screen)
    # 更新并绘制敌人子弹
    enemyBulletGroup.update(n)
    enemyBulletGroup.draw(screen)
    # 更新主角子弹
    peopleBulletGroup.update(n)
    # 绘制子弹
    peopleBulletGroup.draw(screen)
    # 绘制分数
    #screen.blit(scoreImg, (250, 632))
    screen.blit(scoreImgList[score], (444, 632))
    # 更新主角
    people.update1(n)
    # 绘制主角
    people.display()


def play_music(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)


def choose_cloth(anjian, go, hero):
    if anjian == 1:
        go = "军事基地"
        hero = "black"
    if anjian == 2:
        go = "军事基地"
        hero = "red"
    if anjian == 3:
        go = "军事基地"
        hero = "blue"

    return go, hero

# 播放背景音乐
#play_music(Music1)

littleRoom = Father(littleRoomImg, (710, 15))
bigRoom = Father(bigRoomImg, (320, 503))
horizontalWall = Father(horizontalWallImg, (310, 454))
longitudinalWall = Father(longitudinalWallImg, (125, 79))
tower = Father(towerImg, (350, 70))
car = Father(carImg, (740, 280))
frame = Father(frameImg, (720, 400))
package = Father(packageImg, (20, 575))
oilDrum = Father(oilDrumImg, (742, 400))
sandBag = Father(sandBagImg, (8, 395))
fireBucket = Father(fireBucketImg, (15, 285))
prop = Father(propImg, (0, 0))
packageRect = pygame.Rect(0, 560, 120, 160)  # 空投的外圈，用于判定是否在空投附近
roomRect = pygame.Rect(738, 138, 67, 45)
towerRect = pygame.Rect(388, 274, 60, 35)
carRect = pygame.Rect(865, 250, 55, 47)

people = People(peopleNoGunImgList, peopleHaveGunImgList, peoplePickGunImgList,(570, 25), footstepsSound)
group = pygame.sprite.Group()
group.add((littleRoom, bigRoom, horizontalWall, longitudinalWall, tower, car, frame, oilDrum, sandBag,
          fireBucket))
enemyGroup = pygame.sprite.Group()
peopleBulletGroup = pygame.sprite.Group()
enemyBulletGroup = pygame.sprite.Group()

while True:

#    print(pygame.mouse.get_pos())
    # if not pygame.mixer.music.get_busy() and restart:
    #     play_music(Music1)
    if not game:
        n += 1
        restart = False
        '''
        # 场景一
        if zhuanchang == 1:
            screen.blit(bac0, (0,0))
            screen.blit(selectImg1List[n//4 % 4], (216,332))
            screen.blit(selectImg2List[n//4 % 4], (437, 332))
            screen.blit(selectImg3List[n//4 % 4], (660, 332))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            screen = pygame.display.set_mode((960, 720), FULLSCREEN, 32)
                        else:
                            screen = pygame.display.set_mode((960, 720), 0, 32)
                    if event.key == K_1 or event.key == K_KP1:
                        anjian1 = 1
                        #zhuanchang = 2

                    elif event.key == K_2 or event.key == K_KP2:
                        anjian1 = 2
                        #zhuanchang = 2

                    elif event.key == K_3 or event.key == K_KP3:
                        anjian1 = 3
                       # zhuanchang = 2
                zhuanchang, clothColor = choose_cloth(anjian1,zhuanchang, clothColor)

                if clothColor == "black":
                    people.change_cloth(peopleNoGunImgList, peopleHaveGunImgList, peoplePickGunImgList)
                elif clothColor == "red":
                    people.change_cloth(peopleNoGunImgList2, peopleHaveGunImgList2, peoplePickGunImgList2)
                elif clothColor == "blue":
                    people.change_cloth(peopleNoGunImgList3, peopleHaveGunImgList3, peoplePickGunImgList3)
          '''
        # 场景二
        if zhuanchang == "军事基地":
            # 补给箱的信号图
            # if not sign:
            #     if n%30 == 0:
            #         screen.blit(signImgList[0], (0, 545))
            #     else:
            #         screen.blit(signImgList[1], (0, 545))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if not tanchuang:
                    if event.type == KEYDOWN:
                        if event.key == K_f:
                            Fullscreen = not Fullscreen
                            if Fullscreen:
                                screen = pygame.display.set_mode((960, 720), FULLSCREEN, 32)
                            else:
                                screen = pygame.display.set_mode((960, 720), 0, 32)
                        if event.key == K_SPACE and pygame.Rect.colliderect(people.rect, packageRect) and not time_out:

                            people.left = False
                            people.up = False
                            people.right = False
                            people.down = False
                           # sign = True
                            #if bbb():
                            if people.direction == "up":
                                people.image = people.peoplePickGunImgList[0]
                            elif people.direction == "down":
                                people.image = people.peoplePickGunImgList[1]
                            elif people.direction == "left":
                                people.image = people.peoplePickGunImgList[2]
                            elif people.direction == "right":
                                people.image = people.peoplePickGunImgList[3]
                            tanchuang = True
                        elif (event.key == K_UP or event.key == K_w) and not time_out:

                            anjian = "up"
                            #move(anjian, people)
                            #people.up = True
                        elif (event.key == K_DOWN or event.key == K_s) and not time_out:
                            anjian = "down"
                            #move(anjian, people)
                            #people.down = True
                        elif (event.key == K_LEFT or event.key == K_a) and not time_out:
                            anjian = "left"
                            #move(anjian, people)
                            #people.left = True
                        elif (event.key == K_RIGHT or event.key == K_d) and not time_out:
                            anjian = "right"
                           # move(anjian, people)
                            #people.right = True

                    elif event.type == KEYUP and not time_out:
                        if event.key == K_UP or event.key == K_w:
                            anjian = 0
                            if people.up:
                                people.image = people.noGunUp[0]
                            if people.down:
                                people.image = people.noGunDown[0]
                            people.up = False
                            people.down = False
                            people.left = False
                            people.right = False
                            #people.image = people.noGunUp[0]
                        elif event.key == K_DOWN or event.key == K_s:
                            anjian = 0
                            if people.up:
                                people.image = people.noGunUp[0]
                            if people.down:
                                people.image = people.noGunDown[0]
                            people.up = False
                            people.down = False
                            people.left = False
                            people.right = False
                            #people.image = people.noGunDown[0]
                        elif event.key == K_LEFT or event.key == K_a:
                            anjian = 0
                            if people.left:
                                people.image = people.noGunLeft[0]
                            if people.right:
                                people.image = people.noGunRight[0]
                            people.up = False
                            people.down = False
                            people.left = False
                            people.right = False
                            #people.image = people.noGunLeft[0]
                        elif event.key == K_RIGHT or event.key == K_d:
                            anjian = 0
                            if people.left:
                                people.image = people.noGunLeft[0]
                            if people.right:
                                people.image = people.noGunRight[0]
                            people.up = False
                            people.down = False
                            people.left = False
                            people.right = False
                            #people.image = people.noGunRight[0]
            move(anjian, people)
            screen.blit(bac, (0, 0))
            group.draw(screen)
            tip_collide(people.rect, roomRect, tipImg1)
            tip_collide(people.rect, towerRect, tipImg3)
            tip_collide(people.rect, carRect, tipImg2)

            if mm == 200:
                time_1 = time.time()
            if mm > 200:
                time_2 = time.time()
                if not time_out:
                    people.update(n)
                else:
                    #screen.blit(scoreImgList[10], (50, 50))
                    if not tanchuang:
                        screen.blit(timeoutImg, (210, 230))
                people.display()
                #if time_2-time_1 >= 1:
                if int(time_2-time_1)<11:
                    if not tanchuang:
                        screen.blit(timeImgList[int(time_2-time_1)], (50, 50))
                else:
                    time_out = True

            # people.update(n)
            # people.display()
            mm += 1
            if mm < 146:
                if mm % 2 == 0:
                    screen.blit(planeImg1, (244, 720 - 8 * mm))
                else:
                    screen.blit(planeImg2, (244, 720 - 8 * mm))
            # elif 146 <= mm < 228:
            #     screen.blit(parachuteImg, (350-5*(mm-146), -266 + 8 * (mm-146)))
            else:
                if package not in group.sprites():
                    group.add(package)
                # 弹窗
                m = popup(people.rect, packageRect, m)
            if tanchuang:
                group.remove(package)
                k += 10
                screen.blit(buttonImg, (310, 254))
                if k < 233:
                    pygame.draw.rect(screen, (190, 195, 209), (359 + k, 314, 272 - k, 40), 0)
                else:
                    if not load:
                        keys = pygame.key.get_pressed()
                        if keys[K_SPACE]:
                            load = True
                    if load:
                        pygame.mixer.music.fadeout(3000)
                        if k//3 % 10 == 0:
                            aa += 1
                        screen.blit(sceneChangeImgList[aa % 4], (0, 0))
                        if k//3 % 5 == 0:
                            bb += 1
                        screen.blit(peopleHaveGunImgList1[bb % 4], (256,396))
                        current_time = pygame.time.get_ticks()
                        if old_time == -1:
                            old_time = current_time
                        else:
                            if current_time - old_time > 3000:
                                people.image = people.peopleHaveGunImgList[0]
                                people.rect = people.image.get_rect()
                                people.rect.topleft = (100, 300)
                                zhuanchang = 3
                                #pygame.mixer.music.stop()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        # 场景三
        else:
            # if not pygame.mixer.music.get_busy():
            #     play_music(Music2)
            if n % 60 == 0:
                a, enemyPos = set_enemy(enemyImg1List, enemyImg2List, enemyPos)
                if a:
                    enemy = Enemy(a, enemyPos)
                    enemyGroup.add(enemy)
                # for i in range(5):
                #     ran = random.randint(0, 3)
                #     if ran == 0:
                #         #a = random.choice((enemyImg1List, enemyImg2List, enemyImg3List))
                #         a = set_enemy(enemyImg1List, enemyImg2List, enemyImg3List)
                #         enemy = Enemy(a, i)
                #         enemyGroup.add(enemy)
            if is_collide(people, enemyBulletGroup):
                game = "lose"
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            screen = pygame.display.set_mode((960, 720), FULLSCREEN, 32)
                        else:
                            screen = pygame.display.set_mode((960, 720), 0, 32)
                    if event.key == K_UP or event.key == K_w:
                        people.up = True
                        people.direction = "up"
                    elif event.key == K_DOWN or event.key == K_s:
                        people.down = True
                        people.direction = "down"
                    elif event.key == K_LEFT or event.key == K_a:
                        people.left = True
                        people.direction = "left"
                    elif event.key == K_RIGHT or event.key == K_d:
                        people.right = True
                        people.direction = "right"
                    elif event.key == K_SPACE:
                        shoot = True
                        peopleBullet = Bullet(peopleBulletImg, people.rect.topleft, 53, 92, 20)
                        peopleBulletGroup.add(peopleBullet)
                        if Shoot:
                            shootSound.play(0)
                elif event.type == KEYUP:
                    people.image = people.peopleHaveGunImgList[0]
                    if event.key == K_UP or event.key == K_w:
                        people.up = False
                    elif event.key == K_DOWN or event.key == K_s:
                        people.down = False
                    elif event.key == K_LEFT or event.key == K_a:
                        people.left = False
                    elif event.key == K_RIGHT or event.key == K_d:
                        people.right = False
                    elif event.key == K_SPACE:
                        shoot = False
                        shootSound.stop()
            if shoot:
                shoot = not shoot
            score += if_collide(peopleBulletGroup, enemyGroup)
            if score >= 20:
                # score = 20
                game = "win"
            if score >= 20:
                score = 20
            draw(n)
    elif game == "win":
        pygame.mixer.music.stop()
        screen.blit(winImg, (0, 0))
        if mouseMotion:
            screen.blit(replayImg3, (660, 580))
        else:
            screen.blit(replayImg2, (670, 590))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == KEYDOWN and event.key == K_r:
            #     n = 0  # 控制图片
            #     k = 0  # 控制转场弹窗遮罩的横坐标
            #     m = 0  # 控制弹窗上遮罩的横坐标
            #     aa = 0  # 控制转场图片切换
            #     bb = 0  # 控制转场图片切换
            #     tanchuang = False  # 弹窗
            #     load = False  # 加载页面
            #     zhuanchang = False  # 切换场景
            #     current_time = -1
            #     old_time = -1
            #     shoot = False
            #     score = 0
            #     game = None
            #     sign = False
            #     del people
            #     people = People(peopleNoGunImgList, peopleHaveGunImgList, (570, 25), footstepsSound)
            #     group = pygame.sprite.Group()
            #     group.add(littleRoom, bigRoom, horizontalWall, longitudinalWall, tower, car, frame, package, oilDrum,
            #               sandBag,
            #               fireBucket)
            #     enemyGroup = pygame.sprite.Group()
            #     peopleBulletGroup = pygame.sprite.Group()
            #     enemyBulletGroup = pygame.sprite.Group()
            if event.type == MOUSEMOTION:
                if Rect(670, 590, 274, 94).collidepoint(event.pos):
                    mouseMotion = True
                else:
                    mouseMotion = False
            if event.type == MOUSEBUTTONDOWN:
                if Rect(670, 590 , 274, 94).collidepoint(event.pos):
                    n = 0  # 控制图片
                    k = 0  # 控制转场弹窗遮罩的横坐标
                    m = 0  # 控制弹窗上遮罩的横坐标
                    aa = 0  # 控制转场图片切换
                    bb = 0  # 控制转场图片切换
                    mm = 0 # 控制飞机
                    time_1 = 0  # 用于计时
                    time_2 = 0
                    time_out = 0  # 倒计时结束的标志
                    tanchuang = False  # 弹窗
                    load = False  # 加载页面
                    zhuanchang = '军事基地'  # 切换场景
                    anjian1 = 0
                    clothColor = 0
                    enemyPos = None
                    current_time = -1
                    old_time = -1
                    shoot = False
                    score = 0
                    game = None
                    sign = False
                    restart = True
                    del people
                    people = People(peopleNoGunImgList, peopleHaveGunImgList, peoplePickGunImgList, (570, 25), footstepsSound)
                    group = pygame.sprite.Group()
                    group.add((littleRoom, bigRoom, horizontalWall, longitudinalWall, tower, car, frame, oilDrum,
                              sandBag,fireBucket))
                    enemyGroup = pygame.sprite.Group()
                    peopleBulletGroup = pygame.sprite.Group()
                    enemyBulletGroup = pygame.sprite.Group()
    elif game == "lose":
        pygame.mixer.music.stop()
        screen.blit(loseImg, (0, 0))
        if mouseMotion:
            screen.blit(replayImg1, (675, 580))
        else:
            screen.blit(replayImg, (685, 590))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == KEYDOWN and event.key == K_r:
            if event.type == MOUSEMOTION:
                if Rect(675, 580, 274, 94).collidepoint(event.pos):
                    mouseMotion = True
                else:
                    mouseMotion = False
            if event.type == MOUSEBUTTONDOWN:
                if Rect(675, 580, 274, 94).collidepoint(event.pos):
                    n = 0  # 控制图片
                    k = 0  # 控制转场弹窗遮罩的横坐标
                    m = 0  # 控制弹窗上遮罩的横坐标
                    aa = 0  # 控制转场图片切换
                    bb = 0  # 控制转场图片切换
                    mm = 0  # 控制飞机
                    time_1 = 0  # 用于计时
                    time_2 = 0
                    time_out = 0  # 倒计时结束的标志
                    tanchuang = False  # 弹窗
                    load = False  # 加载页面
                    zhuanchang = '军事基地' # 切换场景
                    anjian1 = 0
                    clothColor = 0
                    enemyPos = None
                    current_time = -1
                    old_time = -1
                    shoot = False
                    score = 0
                    game = None
                    sign = False
                    restart = True
                    del people
                    people = People(peopleNoGunImgList, peopleHaveGunImgList, peoplePickGunImgList, (570, 25), footstepsSound)
                    group = pygame.sprite.Group()
                    group.add((littleRoom, bigRoom, horizontalWall, longitudinalWall, tower, car, frame, oilDrum,
                              sandBag,fireBucket))
                    enemyGroup = pygame.sprite.Group()
                    peopleBulletGroup = pygame.sprite.Group()
                    enemyBulletGroup = pygame.sprite.Group()
    pygame.display.update()
    clock.tick(18)
