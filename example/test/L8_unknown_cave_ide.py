import random 

choice=int(input('你发现了一个山洞，有一头沉睡的狮子，选择1:从左侧走；选择2:从右侧走： '))
lion=random.randint(1,2)
weapon=random.randint(1,2)

if choice==lion:
    print("你安全地走出山洞。")
    if choice==weapon:
        print('前方出现了一个魔王，但是你不怕！因为刚才你已经拿到了一把武器！')
    else:
        print('前方出现了一个魔王，你手上还没有武器！只能被魔王吃掉了！')
else:
    print('狮子突然醒了！你被吃掉了')