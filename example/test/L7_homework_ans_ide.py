import random 

name=input('输入你的名字: ')

answer=int(input(name+', 现在你发现前方有2个山洞，你打算进入哪一个山洞？请输入1或者2： '))

cave=random.randint(1,2)

if answer==cave:
    print('你被吃掉了！')
    print('游戏结束')

if answer!=cave:
    print('你走出了山洞，发现了村庄')
    print('游戏结束')
