import pygame,sys,random
from pygame.locals import *
from L19_picture import sun

'''
def building(screen):
    x = random.randint(0, 600)
    y = random.randint(290, 350)
    pygame.draw.rect(screen, (0,51,70), (x, y, 150, 300))
    pygame.draw.rect(screen, (71,103,106), (x + 15, y + 30, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 15, y + 60, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 40, y + 60, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 90, y + 60, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 65, y + 90, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 65, y + 120, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 115, y + 120, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 90, y + 150, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 15, y + 150, 15, 15))
    pygame.draw.rect(screen, (71,103,106), (x + 15, y + 180, 15, 15))
'''
'''
def sun(screen):
    x = random.randint(0,600)
    y = random.randint(0,400)
    pic = pygame.image.load('lesson19/sun.png')#.convert_alpha()
    pic1 = pygame.transform.smoothscale(pic, (160,160))
    pic2 = pygame.transform.smoothscale(pic, (140,140))
    pic3 = pygame.transform.smoothscale(pic, (120,120))
    pic4 = pygame.image.load('lesson19/sun2.png')#.convert_alpha()
    pic4 = pygame.transform.smoothscale(pic4, (100,100))
    screen.blit(pic1, (x,y))
    screen.blit(pic2, (x+10,y+10))
    screen.blit(pic3, (x+20,y+20))
    screen.blit(pic4, (x+30,y+30))
'''


pygame.init()
screen = pygame.display.set_mode((700, 700),NOFRAME)
pygame.display.set_caption("simple")

simple = pygame.image.load('lesson19/simple.png')
#simple2 = pygame.image.load('simple2.png')




screen.blit(simple, (0,0))
#######################
'''
x = random.randint(0, 600)
y = random.randint(290, 350)
pygame.draw.rect(screen, (0,51,70), (x, y, 150, 300))
pygame.draw.rect(screen, (71,103,106), (x + 15, y + 30, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 15, y + 60, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 40, y + 60, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 90, y + 60, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 65, y + 90, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 65, y + 120, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 115, y + 120, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 90, y + 150, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 15, y + 150, 15, 15))
pygame.draw.rect(screen, (71,103,106), (x + 15, y + 180, 15, 15))
#########################
building(screen)
building(screen)
'''
x = random.randint(0,600)
y = random.randint(0,400)
pic = pygame.image.load('lesson19/sun.png')#.convert_alpha()
pic1 = pygame.transform.smoothscale(pic, (160,160))
pic2 = pygame.transform.smoothscale(pic, (140,140))
pic3 = pygame.transform.smoothscale(pic, (120,120))
pic4 = pygame.image.load('lesson19/sun2.png')#.convert_alpha()
pic4 = pygame.transform.smoothscale(pic4, (100,100))
screen.blit(pic1, (x,y))
screen.blit(pic2, (x+10,y+10))
screen.blit(pic3, (x+20,y+20))
screen.blit(pic4, (x+30,y+30))

sun(screen)
sun(screen)
sun(screen)
sun(screen)
sun(screen)
sun(screen)
sun(screen)

#screen.blit(simple2, (0,0))
pygame.display.update()
times = pygame.time.Clock()

while True:
    times.tick(12)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
