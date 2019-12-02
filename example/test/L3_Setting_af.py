import random


#设置字母颜色初始值
def setcolor():  #课堂练习1
    r=0
    g=0
    b=200
    return r,g,b


#设置字母位置初始值
def setpos():    #课堂练习2
    setx = random.uniform(170,500)
    sety = random.uniform(170,250)
    return setx,sety
