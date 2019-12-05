from L18_demo4def import *


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

            "huodui" : 1,    #火堆
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
    times.tick(15)
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
                    suf.set_alpha(210)
                elif suf:
                    suf = ''
            elif suf and Rect(145,100,50,50).collidepoint(event.pos):
                iwant = 'dahuoshi'
            iwant = colli(suf,craft,iwant,event.pos)

            if suf and Rect(555, 350, 100, 60).collidepoint(event.pos):
                make = True


    if suf:
        drawing(suf,items)
        #################################################################半成品中的核心代码部分
        #注释部分是学生可以写出来的
        if iwant in craft :
            suf.blit(eval(iwant), (480,125))
            num = 0
            for i in craft[iwant]:
                suf.blit(eval(i), (392+num*60,225))
                print_text(suf, 392+num*60, 225, str(craft[iwant][i]))
                num += 1
            #kaiguan = True
            #for i in craft[iwant]:
                #if craft[iwant][i] > items[i]:
                    #kaiguan = False
                    #break

            #if kaiguan and make:
                #for i in craft[iwant]:
                    #items[i] -= craft[iwant][i]
                #items[iwant] += 1

                print("iwant crafted\n")


            #if items["zhangpeng"] >= 1 and items["huodui"] >= 1:
                #final = pygame.image.load('image/cunhuo.png').convert_alpha()
                #final = pygame.transform.smoothscale(final, (700,500))
                #suf.blit(final,(8,12))
        ########################################################################半成品中的核心代码部分

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()
