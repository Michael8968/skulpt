import pygame,random,math,sys

from pygame.locals import *
from pygame import Rect

def print_text(font, x, y, text, color=(0,0,0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))



pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("test")

font = pygame.font.Font(None, 18)
font_zh = pygame.font.Font('simhei.ttf', 18)
font_zh2 = pygame.font.Font('simhei.ttf', 35)
font_zh3 = pygame.font.Font('simhei.ttf', 22)
font_zh4 = pygame.font.Font('simhei.ttf', 25)
font_zh5 = pygame.font.Font('simhei.ttf', 20)




bac1 = pygame.image.load('lesson16/image/bac1.png').convert_alpha()
bac1 = pygame.transform.smoothscale(bac1, (600,800))
bac2 = pygame.image.load('lesson16/image/bac2.png').convert_alpha()
bac2 = pygame.transform.smoothscale(bac2, (600,800))

#fruit
grape = pygame.image.load('lesson16/image/fruit/grape.png').convert_alpha()
grape1 = pygame.transform.smoothscale(grape, (140, 110))
grape2 = pygame.transform.smoothscale(grape, (600, 460))
grapefruit = pygame.image.load('lesson16/image/fruit/grapefruit.png').convert_alpha()
grapefruit1 = pygame.transform.smoothscale(grapefruit, (140, 110))
grapefruit2 = pygame.transform.smoothscale(grapefruit, (600, 460))
kiwifruit = pygame.image.load('lesson16/image/fruit/kiwifruit.png').convert_alpha()
kiwifruit1 = pygame.transform.smoothscale(kiwifruit, (140, 110))
kiwifruit2 = pygame.transform.smoothscale(kiwifruit, (600, 460))
lemon = pygame.image.load('lesson16/image/fruit/lemon.png').convert_alpha()
lemon1 = pygame.transform.smoothscale(lemon, (140, 110))
lemon2 = pygame.transform.smoothscale(lemon, (600, 460))
orange = pygame.image.load('lesson16/image/fruit/orange.png').convert_alpha()
orange1 = pygame.transform.smoothscale(orange, (140, 110))
orange2 = pygame.transform.smoothscale(orange, (600, 460))
pitaya = pygame.image.load('lesson16/image/fruit/pitaya.png').convert_alpha()
pitaya1 = pygame.transform.smoothscale(pitaya, (140, 110))
pitaya2 = pygame.transform.smoothscale(pitaya, (600, 460))
strawberry = pygame.image.load('lesson16/image/fruit/strawberry.png').convert_alpha()
strawberry1 = pygame.transform.smoothscale(strawberry, (140, 110))
strawberry2 = pygame.transform.smoothscale(strawberry, (600, 460))
tangerine = pygame.image.load('lesson16/image/fruit/tangerine.png').convert_alpha()
tangerine1 = pygame.transform.smoothscale(tangerine, (140, 110))
tangerine2 = pygame.transform.smoothscale(tangerine, (600, 460))



#vegetable
cabbage = pygame.image.load('lesson16/image/vegetable/cabbage.png').convert_alpha()
cabbage1 = pygame.transform.smoothscale(cabbage, (140, 110))
cabbage2 = pygame.transform.smoothscale(cabbage, (600, 460))
cauliflower = pygame.image.load('lesson16/image/vegetable/cauliflower.png').convert_alpha()
cauliflower1 = pygame.transform.smoothscale(cauliflower, (140, 110))
cauliflower2 = pygame.transform.smoothscale(cauliflower, (600, 460))
celery = pygame.image.load('lesson16/image/vegetable/celery.png').convert_alpha()
celery1 = pygame.transform.smoothscale(celery, (140, 110))
celery2 = pygame.transform.smoothscale(celery, (600, 460))
eggplant = pygame.image.load('lesson16/image/vegetable/eggplant.png').convert_alpha()
eggplant1 = pygame.transform.smoothscale(eggplant, (140, 110))
eggplant2 = pygame.transform.smoothscale(eggplant, (600, 460))
grlic = pygame.image.load('lesson16/image/vegetable/grlic.png').convert_alpha()
grlic1 = pygame.transform.smoothscale(grlic, (140, 110))
grlic2 = pygame.transform.smoothscale(grlic, (600, 460))
mushroom = pygame.image.load('lesson16/image/vegetable/mushroom.png').convert_alpha()
mushroom1 = pygame.transform.smoothscale(mushroom, (140, 110))
mushroom2 = pygame.transform.smoothscale(mushroom, (600, 460))
spinage = pygame.image.load('lesson16/image/vegetable/spinage.png').convert_alpha()
spinage1 = pygame.transform.smoothscale(spinage, (140, 110))
spinage2 = pygame.transform.smoothscale(spinage, (600, 460))
tomato = pygame.image.load('lesson16/image/vegetable/tomato.png').convert_alpha()
tomato1 = pygame.transform.smoothscale(tomato, (140, 110))
tomato2 = pygame.transform.smoothscale(tomato, (600, 460))

#seafood
carp = pygame.image.load('lesson16/image/seafood/carp.png').convert_alpha()
carp1 = pygame.transform.smoothscale(carp, (140, 110))
carp2 = pygame.transform.smoothscale(carp, (600, 460))
cooked_crab = pygame.image.load('lesson16/image/seafood/cooked_crab.png').convert_alpha()
cooked_crab1 = pygame.transform.smoothscale(cooked_crab, (140, 110))
cooked_crab2 = pygame.transform.smoothscale(cooked_crab, (600, 460))
crab = pygame.image.load('lesson16/image/seafood/crab.png').convert_alpha()
crab1 = pygame.transform.smoothscale(crab, (140, 110))
crab2 = pygame.transform.smoothscale(crab, (600, 460))
fillet = pygame.image.load('lesson16/image/seafood/fillet.png').convert_alpha()
fillet1 = pygame.transform.smoothscale(fillet, (140, 110))
fillet2 = pygame.transform.smoothscale(fillet, (600, 460))
grasscrap = pygame.image.load('lesson16/image/seafood/grasscrap.png').convert_alpha()
grasscrap1 = pygame.transform.smoothscale(grasscrap, (140, 110))
grasscrap2 = pygame.transform.smoothscale(grasscrap, (600, 460))
mussel = pygame.image.load('lesson16/image/seafood/mussel.png').convert_alpha()
mussel1 = pygame.transform.smoothscale(mussel, (140, 110))
mussel2 = pygame.transform.smoothscale(mussel, (600, 460))
prawn = pygame.image.load('lesson16/image/seafood/prawn.png').convert_alpha()
prawn1 = pygame.transform.smoothscale(prawn, (140, 110))
prawn2 = pygame.transform.smoothscale(prawn, (600, 460))
yellow_fin_tuna = pygame.image.load('lesson16/image/seafood/yellow-fin_tuna.png').convert_alpha()
yellow_fin_tuna1 = pygame.transform.smoothscale(yellow_fin_tuna, (140, 110))
yellow_fin_tuna2 = pygame.transform.smoothscale(yellow_fin_tuna, (600, 460))



#poultry
egg = pygame.image.load('lesson16/image/poultry/egg.png').convert_alpha()
egg1 = pygame.transform.smoothscale(egg, (140, 110))
egg2 = pygame.transform.smoothscale(egg, (600, 460))
salted_egg = pygame.image.load('lesson16/image/poultry/salted_egg.png').convert_alpha()
salted_egg1 = pygame.transform.smoothscale(salted_egg, (140, 110))
salted_egg2 = pygame.transform.smoothscale(salted_egg, (600, 460))
spiced_corned_egg = pygame.image.load('lesson16/image/poultry/spiced_corned_egg.png').convert_alpha()
spiced_corned_egg1 = pygame.transform.smoothscale(spiced_corned_egg, (140, 110))
spiced_corned_egg2 = pygame.transform.smoothscale(spiced_corned_egg, (600, 460))
chicken_breast = pygame.image.load('lesson16/image/poultry/chicken_breast.png').convert_alpha()
chicken_breast1 = pygame.transform.smoothscale(chicken_breast, (140, 110))
chicken_breast2 = pygame.transform.smoothscale(chicken_breast, (600, 460))
dunk = pygame.image.load('lesson16/image/poultry/dunk.png').convert_alpha()
dunk1 = pygame.transform.smoothscale(dunk, (140, 110))
dunk2 = pygame.transform.smoothscale(dunk, (600, 460))
hen = pygame.image.load('lesson16/image/poultry/hen.png').convert_alpha()
hen1 = pygame.transform.smoothscale(hen, (140, 110))
hen2 = pygame.transform.smoothscale(hen, (600, 460))
sprint_chicken = pygame.image.load('lesson16/image/poultry/sprint_chicken.png').convert_alpha()
sprint_chicken1 = pygame.transform.smoothscale(sprint_chicken, (140, 110))
sprint_chicken2 = pygame.transform.smoothscale(sprint_chicken, (600, 460))
wing = pygame.image.load('lesson16/image/poultry/wing.png').convert_alpha()
wing1 = pygame.transform.smoothscale(wing, (140, 110))
wing2 = pygame.transform.smoothscale(wing, (600, 460))



#meat
beef = pygame.image.load('lesson16/image/meat/beef.png').convert_alpha()
beef1 = pygame.transform.smoothscale(beef, (140, 110))
beef2 = pygame.transform.smoothscale(beef, (600, 460))
beef_slices = pygame.image.load('lesson16/image/meat/beef_slices.png').convert_alpha()
beef_slices1 = pygame.transform.smoothscale(beef_slices, (140, 110))
beef_slices2 = pygame.transform.smoothscale(beef_slices, (600, 460))
beef_tenderloin = pygame.image.load('lesson16/image/meat/beef_tenderloin.png').convert_alpha()
beef_tenderloin1 = pygame.transform.smoothscale(beef_tenderloin, (140, 110))
beef_tenderloin2 = pygame.transform.smoothscale(beef_tenderloin, (600, 460))
ham = pygame.image.load('lesson16/image/meat/ham.png').convert_alpha()
ham1 = pygame.transform.smoothscale(ham, (140, 110))
ham2 = pygame.transform.smoothscale(ham, (600, 460))
mutton_slices = pygame.image.load('lesson16/image/meat/mutton_slices.png').convert_alpha()
mutton_slices1 = pygame.transform.smoothscale(mutton_slices, (140, 110))
mutton_slices2 = pygame.transform.smoothscale(mutton_slices, (600, 460))
pork = pygame.image.load('lesson16/image/meat/pork.png').convert_alpha()
pork1 = pygame.transform.smoothscale(pork, (140, 110))
pork2 = pygame.transform.smoothscale(pork, (600, 460))
silverside = pygame.image.load('lesson16/image/meat/silverside.png').convert_alpha()
silverside1 = pygame.transform.smoothscale(silverside, (140, 110))
silverside2 = pygame.transform.smoothscale(silverside, (600, 460))
steak = pygame.image.load('lesson16/image/meat/steak.png').convert_alpha()
steak1 = pygame.transform.smoothscale(steak, (140, 110))
steak2 = pygame.transform.smoothscale(steak, (600, 460))






fruit = {
    'grape':{
        'name': '夏黑葡萄',
        'image': grape1,
        'big_image': grape2,
        'price': '￥39.9',
        'made_in': '云南红河',
        'standard' : '500g',
        'sold': '14163',
        'packaging': '份',
        'describe': '富含花青素',
        },
    'grapefruit':{
        'name': '南非葡萄柚',
        'image': grapefruit1,
        'big_image': grapefruit2,
        'price': '￥29',
        'made_in': '南非',
        'standard' : '1个',
        'sold': '23546',
        'packaging': '份',
        'describe': '富含维他命C',
        },
    'kiwifruit':{
        'name': '新西兰奇异果',
        'image': kiwifruit1,
        'big_image': kiwifruit2,
        'price': '￥59',
        'made_in': '新西兰',
        'standard' : '10个',
        'sold': '23623',
        'packaging': '份',
        'describe': '营养丰富',
        },
    'lemon':{
        'name': '四川安岳黄柠檬',
        'image': lemon1,
        'big_image': lemon2,
        'price': '￥9.9',
        'made_in': '四川',
        'standard' : '8个',
        'sold': '87695',
        'packaging': '份',
        'describe': '果皮光滑无果斑',
        },
    'orange':{
        'name': '精选冰糖橙',
        'image': orange1,
        'big_image': orange2,
        'price': '￥28.8',
        'made_in': '湖南黔阳',
        'standard' : '3个',
        'sold': '125423',
        'packaging': '份',
        'describe': '味浓香甜、果皮薄',
        },
    'pitaya':{
        'name': '越南红心火龙果',
        'image': pitaya1,
        'big_image': pitaya2,
        'price': '￥28.9',
        'made_in': '越南',
        'standard' : '2个',
        'sold': '35347',
        'packaging': '份',
        'describe': '富含花青素',
        },
    'strawberry':{
        'name': '奉贤大草莓',
        'image': strawberry1,
        'big_image': strawberry2,
        'price': '￥33',
        'made_in': '上海奉贤',
        'standard' : '公斤',
        'sold': '236324',
        'packaging': '份',
        'describe': '个大味甜',
        },
    'tangerine':{
        'name': '精选帝王柑',
        'image': tangerine1,
        'big_image': tangerine2,
        'price': '￥49.9',
        'made_in': '广东',
        'standard' : '6个',
        'sold': '135347',
        'packaging': '份',
        'describe': '想象不到的好吃',
        },

    }

vegetable = {
    'cabbage':{
        'name': '精选本地卷心菜',
        'image': cabbage1,
        'big_image': cabbage2,
        'price': '￥7.8',
        'made_in': '上海',
        'standard' : '600g',
        'sold': '23523',
        'packaging': '份',
        'describe': '口感鲜嫩',
        },
    'cauliflower':{
        'name': '有机花椰菜',
        'image': cauliflower1,
        'big_image': cauliflower2,
        'price': '￥13.9',
        'made_in': '上海',
        'standard' : '300g',
        'sold': '23555',
        'packaging': '份',
        'describe': '有机蔬菜',
        },
    'celery':{
        'name': '精选西芹',
        'image': celery1,
        'big_image': celery2,
        'price': '￥9.9',
        'made_in': '上海',
        'standard' : '700g',
        'sold': '42974',
        'packaging': '份',
        'describe': '健康鲜蔬',
        },
    'eggplant':{
        'name': '有机茄子',
        'image': eggplant1,
        'big_image': eggplant2,
        'price': '￥13.5',
        'made_in': '浙江',
        'standard' : '350g',
        'sold': '52525',
        'packaging': '份',
        'describe': '有机蔬菜',
        },
    'grlic':{
        'name': '精选大蒜头',
        'image': grlic1,
        'big_image': grlic2,
        'price': '￥5.9',
        'made_in': '四川',
        'standard' : '200g',
        'sold': '25326',
        'packaging': '份',
        'describe': '调味必备',
        },
    'mushroom':{
        'name': '新鲜平菇',
        'image': mushroom1,
        'big_image': mushroom2,
        'price': '￥9.8',
        'made_in': '金华',
        'standard' : '250g',
        'sold': '64375',
        'packaging': '份',
        'describe': '新鲜采摘',
        },
    'spinage':{
        'name': '精选菠菜',
        'image': spinage1,
        'big_image': spinage2,
        'price': '￥5.9',
        'made_in': '苏州',
        'standard' : '250g',
        'sold': '34654',
        'packaging': '份',
        'describe': '新鲜营养',
        },
    'tomato':{
        'name': '精选西红柿',
        'image': tomato1,
        'big_image': tomato2,
        'price': '￥9.9',
        'made_in': '奉贤',
        'standard' : '600g',
        'sold': '25366',
        'packaging': '份',
        'describe': '营养新鲜',
        },
    }

seafood = {
    'carp':{
        'name': '家养鲤鱼',
        'image': carp1,
        'big_image': carp2,
        'price': '￥29.9',
        'made_in': '奉贤',
        'standard' : '300g',
        'sold': '3243',
        'packaging': '份',
        'describe': '新鲜甜美',
        },
    'cooked_crab':{
        'name': '北海道熟螃蟹',
        'image': cooked_crab1,
        'big_image': cooked_crab2,
        'price': '￥49.9',
        'made_in': '北海道',
        'standard' : '300g',
        'sold': '2352',
        'packaging': '份',
        'describe': '方便烹饪',
        },
    'crab':{
        'name': '广东大青蟹',
        'image': crab1,
        'big_image': crab2,
        'price': '￥49.9',
        'made_in': '广东',
        'standard' : '400g',
        'sold': '3524',
        'packaging': '份',
        'describe': '个大味美',
        },
    'fillet':{
        'name': '美威三味鱼',
        'image': fillet1,
        'big_image': fillet2,
        'price': '￥45.8',
        'made_in': '智利',
        'standard' : '250g',
        'sold': '5232',
        'packaging': '包',
        'describe': '简单料理',
        },
    'grasscrap':{
        'name': '奉贤草鱼',
        'image': grasscrap1,
        'big_image': grasscrap2,
        'price': '￥19.9',
        'made_in': '奉贤',
        'standard' : '400g',
        'sold': '3466',
        'packaging': '条',
        'describe': '鲜活美味',
        },
    'mussel':{
        'name': '新西兰青口贝',
        'image': mussel1,
        'big_image': mussel2,
        'price': '￥59.9',
        'made_in': '新西兰',
        'standard' : '1kg',
        'sold': '2355',
        'packaging': '盒',
        'describe': '原装进口',
        },
    'prawn':{
        'name': '厄瓜多尔白虾',
        'image': prawn1,
        'big_image': prawn2,
        'price': '￥128',
        'made_in': '厄瓜多尔',
        'standard' : '1.8kg',
        'sold': '23525',
        'packaging': '盒',
        'describe': '嫩滑少刺',
        },
    'yellow_fin_tuna':{
        'name': '国联黄花鱼',
        'image': prawn1,
        'big_image': prawn2,
        'price': '￥39.9',
        'made_in': '浙江杭州',
        'standard' : '700g',
        'sold': '2352',
        'packaging': '包',
        'describe': '嫩滑少刺',
        },

    }

meat = {
    'beef_tenderloin':{
        'name': '恒都牛里脊',
        'image': beef_tenderloin1,
        'big_image': beef_tenderloin2,
        'price': '￥49.9',
        'made_in': '重庆丰都',
        'standard' : '1kg',
        'sold': '23522',
        'packaging': '包',
        'describe': '肉质鲜嫩',
        },
    'beef':{
        'name': '澳洲牛肉',
        'image': beef1,
        'big_image': beef2,
        'price': '￥49.9',
        'made_in': '澳大利亚',
        'standard' : '600g',
        'sold': '2352',
        'packaging': '份',
        'describe': '原切',
        },
    'beef_slices':{
        'name': '恒都肥牛卷',
        'image': beef_slices1,
        'big_image': beef_slices2,
        'price': '￥39.9',
        'made_in': '重庆丰都',
        'standard' : '500g',
        'sold': '2525',
        'packaging': '包',
        'describe': '原切',
        },
    'ham':{
        'name': '特级金华火腿',
        'image': ham1,
        'big_image': ham2,
        'price': '￥99.9',
        'made_in': '金华',
        'standard' : '1kg',
        'sold': '2352',
        'packaging': '份',
        'describe': '口味醇厚',
        },
    'mutton_slices':{
        'name': '恒都羊肉卷',
        'image': mutton_slices1,
        'big_image': mutton_slices2,
        'price': '￥26.9',
        'made_in': '重庆',
        'standard' : '350g',
        'sold': '52241',
        'packaging': '份',
        'describe': '肉质紧实',

        },
    'pork':{
        'name': '家佳康猪廋肉',
        'image': pork1,
        'big_image': pork2,
        'price': '￥22.2',
        'made_in': '江苏',
        'standard' : '450g',
        'sold': '2352',
        'packaging': '份',
        'describe': '谷物饲养',
        },
    'silverside':{
        'name': '加拿大牛腿肉',
        'image': silverside1,
        'big_image': silverside2,
        'price': '￥69.9',
        'made_in': '加拿大',
        'standard' : '1kg',
        'sold': '2365',
        'packaging': '份',
        'describe': '谷物饲养',
        },
    'steak':{
        'name': '澳洲嫩肩牛排',
        'image': steak1,
        'big_image': steak2,
        'price': '￥ 29.9',
        'made_in': '澳大利亚',
        'standard' : '200g',
        'sold': '23525',
        'packaging': '包',
        'describe': '原切',
        },

    }

poultry = {
    'egg':{
        'name': '散养土鸡蛋',
        'image': egg1,
        'big_image': egg2,
        'price': '￥20.9',
        'made_in': '安徽',
        'standard' : '15枚',
        'sold': '23525',
        'packaging': '盒',
        'describe': '谷饲鸡蛋',
        },
    'salted_egg':{
        'name': '绿水沱咸鸭蛋',
        'image': salted_egg1,
        'big_image': salted_egg2,
        'price': '￥15.9',
        'made_in': '江苏',
        'standard' : '6枚',
        'sold': '2352',
        'packaging': '份',
        'describe': '无铅工艺',
        },
    'spiced_corned_egg':{
        'name': '凤翔卤蛋',
        'image': spiced_corned_egg1,
        'big_image': spiced_corned_egg2,
        'price': '￥19.9',
        'made_in': '凤翔',
        'standard' : '8枚',
        'sold': '23525',
        'packaging': '份',
        'describe': 'Q弹入味',
        },
    'wing':{
        'name': '凤祥鸡翅中',
        'image': wing1,
        'big_image': wing2,
        'price': '￥49.9',
        'made_in': '山东',
        'standard' : '1kg',
        'sold': '12351',
        'packaging': '包',
        'describe': '不用激素',
        },
    'sprint_chicken':{
        'name': '苏北童子鸡',
        'image': sprint_chicken1,
        'big_image': sprint_chicken2,
        'price': '￥19.9',
        'made_in': '江苏',
        'standard' : '600g',
        'sold': '23521',
        'packaging': '份',
        'describe': '谷物饲养',
        },
    'hen':{
        'name': '苏北散养老母鸡',
        'image': hen1,
        'big_image': hen2,
        'price': '￥49.9',
        'made_in': '江苏',
        'standard' : '950g',
        'sold': '23525',
        'packaging': '只',
        'describe': '林间散养',
        },
    'dunk':{
        'name': '崇明草鸭',
        'image': dunk1,
        'big_image': dunk2,
        'price': '￥39.9',
        'made_in': '上海',
        'standard' : '900g',
        'sold': '23523',
        'packaging': '只',
        'describe': '农家散养',
        },
    'chicken_breast':{
        'name': '泰森去皮鸡胸',
        'image': chicken_breast1,
        'big_image': chicken_breast2,
        'price': '￥11.9',
        'made_in': '南通',
        'standard' : '454g',
        'sold': '25235',
        'packaging': '袋',
        'describe': '国际品牌',
        },

    }



show = 0
suf1 = ''

show_dict = fruit
show_list = list(show_dict.keys())
show_details = ''
time = pygame.time.Clock()
while True:

    if show == 0:
        show_dict = fruit
    elif show == 1:
        show_dict = vegetable

    elif show == 2:
        show_dict = seafood
    elif show == 3:
        show_dict = meat
    elif show == 4:
        show_dict = poultry
    show_list = list(show_dict.keys())

    #screen.fill((100,100,100))
    screen.blit(bac1, (0,0))

    #pygame.draw.rect(screen, (0,255,0), (show*113 + 18, 390,113,3), 3)
    #pygame.draw.rect(screen, (0,255,0), (show*120 + 20, 390,80,3), 3)
    pygame.draw.rect(screen, (60,170,80), (show*120 + 20, 390,80,3), 3)

    n = 0
    '''
    for a in show_dict:
        if n < 4:
            screen.blit(show_dict[a]['image'], (n*150, 250))
            print_text(font_zh, n*150, 400, show_dict[a]['name'], color=(0,0,0))
            print_text(font, n*150, 420, show_dict[a]['price'], color=(0,0,0))
        else:
            screen.blit(value['image'], ((n-4)*150, 450))
            print_text(font_zh, (n-4)*150, 600, show_dict[a]['name'], color=(0,0,0))
            print_text(font, (n-4)*150, 620, show_dict[a]['price'], color=(0,0,0))

        n += 1
    '''
    for value in show_dict.values():
        if n < 4:
            print(value['image'])
            screen.blit(value['image'], (n*140 + 20, 405),Rect(0,0,100,100))
            print_text(font_zh, n*140 + 25, 525, value['name'], color=(0,0,0))
            print_text(font_zh, n*140 + 25, 550, value['price'], color=(255,0,0))
        else:
            screen.blit(value['image'], ((n-4)*140 + 20, 600),Rect(0,0,100,100))
            print_text(font_zh, (n-4)*140 + 25, 720, value['name'], color=(0,0,0))
            print_text(font_zh, (n-4)*140 + 25, 745, value['price'], color=(255,0,0))
        n += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if not suf1:
                if Rect(18, 300, 113, 93).collidepoint(event.pos):
                    print(1)
                    show = 0
                if Rect(131, 300, 113, 93).collidepoint(event.pos):
                    print(2)
                    show = 1
                if Rect(244, 300, 113, 93).collidepoint(event.pos):
                    print(3)
                    show = 2
                if Rect(357, 300, 113, 93).collidepoint(event.pos):
                    print(4)
                    show = 3
                if Rect(470, 300, 113, 93).collidepoint(event.pos):
                    print(5)
                    show = 4

                if Rect(20, 395, 140, 180).collidepoint(event.pos):
                    if len(show_list) >= 1:
                        show_details = show_list[0]
                        suf1 = pygame.Surface((600, 800))

                if Rect(160, 395, 140, 180).collidepoint(event.pos):
                    print(22)
                    if len(show_list) >= 2:
                        show_details = show_list[1]
                        suf1 = pygame.Surface((600, 800))
                if Rect(300, 395, 140, 180).collidepoint(event.pos):
                    print(33)
                    if len(show_list) >= 3:
                        show_details = show_list[2]
                        suf1 = pygame.Surface((600, 800))
                if Rect(440, 395, 140, 180).collidepoint(event.pos):
                    print(44)
                    if len(show_list) >= 4:
                        show_details = show_list[3]
                        suf1 = pygame.Surface((600, 800))
                if Rect(20, 590, 140, 180).collidepoint(event.pos):
                    print(55)
                    if len(show_list) >= 5:
                        show_details = show_list[4]
                        suf1 = pygame.Surface((600, 800))
                if Rect(160, 590, 140, 180).collidepoint(event.pos):
                    print(66)
                    if len(show_list) >= 6:
                        show_details = show_list[5]
                        suf1 = pygame.Surface((600, 800))
                if Rect(300, 590, 140, 180).collidepoint(event.pos):
                    print(77)
                    if len(show_list) >= 7:
                        show_details = show_list[6]
                        suf1 = pygame.Surface((600, 800))
                if Rect(440, 590, 140, 180).collidepoint(event.pos):
                    print(88)
                    if len(show_list) >= 8:
                        show_details = show_list[7]
                        suf1 = pygame.Surface((600, 800))
            elif suf1:
                if Rect(10,10,40,40).collidepoint(event.pos):
                    suf1 = ''


    if suf1:
        screen.blit(bac2, (0,0))
        screen.blit(show_dict[show_details]['big_image'], (0,0))
        print_text(font_zh, 50, 400, show_dict[show_details]['standard'] + '装', color=(100,100,100))
        print_text(font_zh2, 12, 555, show_dict[show_details]['price'], color=(255,69,0))
        print_text(font_zh4, 16, 595, show_dict[show_details]['name'], color=(0,0,0))
        print_text(font_zh3, 17, 635, show_dict[show_details]['standard'] + '*1' + show_dict[show_details]['packaging'], color=(50,50,50))
        print_text(font_zh5, 17, 665, '规格', color=(180,180,180))

        print_text(font_zh3, 187, 635, show_dict[show_details]['describe'], color=(50,50,50))
        print_text(font_zh5, 187, 665, '产品特点', color=(180,180,180))

        print_text(font_zh3, 357, 635, show_dict[show_details]['made_in'], color=(50,50,50))
        print_text(font_zh5, 357, 665, '产地', color=(180,180,180))

        print_text(font_zh3, 18, 720, '满88包邮(10kg内)                        月销 ' + str(show_dict[show_details]['sold']) + '笔', color=(180,180,180))

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    time.tick(15)
    pygame.display.update()
