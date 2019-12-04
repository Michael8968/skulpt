import turtle
import random
turtle.mode("logo")#设置乌龟模式（“standard”，“logo”或“world”）并执行重置
turtle.showturtle()#显示乌龟
turtle.shape("turtle")#返回或设置形状，最初有以下形状：“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”。
turtle.penup()
turtle.goto(-251,-100)
turtle.pendown()
turtle.speed(1)
turtle.pensize(10)
for j in range(4):
    length =5
    flag=True
    for i in range(21):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        turtle.colormode(255)#先使用这行代码将默认状态下turtle.colormode(1.0)切换turtle.colormode(255)
        turtle.pencolor(r,g,b)
        turtle.penup()
        if j==0:
            turtle.goto(-200+i*15,-100)
        elif j==1:
            turtle.goto(100,-100+i*15)
        elif j==2:
            turtle.goto(100-i*15,200)
        elif j==3:
            turtle.goto(-200,200-i*15)
        turtle.pendown()
        turtle.forward(length)
        if length>=105 or length<5:
            flag=not flag
            print(flag)
        if flag==True:
            length=length+10
        elif flag==False:
            length=length-10
    turtle.left(90)
turtle.done()
