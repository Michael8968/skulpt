import sys, random, time, pygame
from pygame.locals import*
import time
'''
def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
'''

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Piano")

bac = pygame.image.load('lesson7/bac.png').convert_alpha()
bac = pygame.transform.smoothscale(bac, (800,600))
124


#加载声音
sound = []
for i in range(8):
    sound.append(pygame.mixer.Sound('lesson7/'+str(i)+'.wav'))


#加载图片
img = []
for i in range(8):
    aa = pygame.image.load('lesson7/ren/a' + str(i+1) + '.png')
    aa = pygame.transform.smoothscale(aa, (120,200))
    img.append(aa)

img2 = []
for i in range(8):
    bb = pygame.image.load('lesson7/ren/b' + str(i+1) + '.png')
    bb = pygame.transform.smoothscale(bb, (120,200))
    img2.append(bb)



pu = []
pu1 = pygame.image.load('lesson7/pu1.png').convert_alpha()
pu1 = pygame.transform.smoothscale(pu1, (800,600))
pu2 = pygame.image.load('lesson7/pu2.png').convert_alpha()
pu2 = pygame.transform.smoothscale(pu2, (800,600))
pu3 = pygame.image.load('lesson7/pu3.png').convert_alpha()
pu3 = pygame.transform.smoothscale(pu3, (800,600))
pu.append(pu1)
pu.append(pu2)
pu.append(pu3)
puNum = 0

img3 = img.copy()
flag = 0
count = 0

while True:
    time.sleep(0.01)
    keys = pygame.key.get_pressed()
    screen.blit(bac,(0,0))

    screen.blit(pu[puNum],(0,0))
    for i in range(8):
        screen.blit(img3[i],(60+i*80, 300))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_1:
            #print(keys)
            sound[1].play()
            flag = 1
            img3[0] = img2[0]

        if event.type == KEYDOWN and event.key == K_2:
            sound[2].play() #第二个声音播放
            flag = 1
            img3[1] = img2[1]   #图片替换
        if event.type == KEYDOWN and event.key == K_3:
            sound[3].play()
            flag = 1
            img3[2] = img2[2]
        if event.type == KEYDOWN and event.key == K_4:
            sound[4].play()
            flag = 1
            img3[3] = img2[3]
        if event.type == KEYDOWN and event.key == K_5:
            sound[5].play()
            flag = 1
            img3[4] = img2[4]
        if event.type == KEYDOWN and event.key == K_6:
            sound[6].play()
            flag = 1
            img3[5] = img2[5]
        if event.type == KEYDOWN and event.key == K_7:
            sound[7].play()
            flag = 1
            img3[6] = img2[6]
        if event.type == KEYDOWN and event.key == K_8:
            sound[0].play()
            flag = 1
            img3[7] = img2[7]



        if event.type == KEYDOWN and event.key == K_SPACE:
            if puNum <= 1:
                puNum += 1
            elif puNum == 2:
                puNum = 0




    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 11
    if flag == 1:
        count += 1
        if count == 60:
            #print(1)
            #print(img3)
            img3 = img.copy()

            count = 0
            flag = 0



        clock_start = time.clock()




    pygame.display.update()
