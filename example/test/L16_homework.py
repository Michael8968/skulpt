import pygame

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("homework")

###############写课后作业################
        
    




###############写课后作业###############



shouce={ '小傲':{ '性别':'男孩',
                 '身高': 1.6,
                 '爱好':'足球',
                },
         '小梦':{ '性别':'女孩',
                 '身高': 1.3,
                 '爱好':'看电视',
                
                },
         '果果':{ '性别':'男孩',
                 '身高': 1.5,
                 '爱好':'拯救世界',
                 'image':a,
                },
         '小米':{ '性别':'男孩',
                 '身高': 1,
                 '爱好':'玩游戏',
                },
}


while True:
    screen.fill((255,255,255))
    
    ###############写课后作业################
        
    




    ###############写课后作业###############
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
