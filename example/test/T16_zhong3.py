import turtle
import random
from datetime import datetime
turtle.tracer(False)
turtle.mode("logo")
turtle.colormode(255)


def clock():

    turtle.clear()
    turtle.bgcolor("black")
    shijian = datetime.now()
    hh = shijian.hour
    mm = shijian.minute
    ss = shijian.second

    turtle.goto(0, 0)
    turtle.pensize(20)
    turtle.pd()
    turtle.pencolor("lightgreen")
    turtle.seth(0)
    turtle.right(360/12*hh)
    turtle.forward(110)#时针

    turtle.pu()
    turtle.goto(0,0)
    turtle.pensize(10)
    turtle.pd()
    turtle.pencolor("lightskyblue")
    turtle.seth(0)
    turtle.right(360/60*mm)
    turtle.forward(150) # 分针

    turtle.pu()
    turtle.goto(0,0)
    turtle.pensize(7)
    turtle.pd()
    turtle.pencolor("gold")
    turtle.seth(0)
    turtle.right(360/60*ss)

    turtle.circle(49, 180)

    turtle.dot(20)# 秒针

    for i in range(12):

        turtle.pensize(10)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.seth(0)
        turtle.goto(0, 0)
        turtle.right(i*30)
        turtle.pu()
        turtle.forward(257)
        turtle.right(ss*60)
        turtle.forward(10)
        turtle.pd()
        turtle.forward(22)
        turtle.pu()
        # 12个刻度

    turtle.update()
    turtle.ontimer(clock, 1000)


clock()
turtle.done()

