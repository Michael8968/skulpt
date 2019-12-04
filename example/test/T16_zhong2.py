import turtle
import random
from datetime import datetime
turtle.tracer(False)
turtle.mode("logo")
turtle.colormode(255)


def clock():
    turtle.clear()

    shijian = datetime.now()
    hh = shijian.hour
    mm = shijian.minute
    ss = shijian.second

    turtle.pensize(20)
    turtle.pencolor("lightgreen")
    turtle.pu()
    turtle.goto(0,0)
    turtle.seth(0)
    turtle.right(30*hh)
    turtle.pd() 
    turtle.forward(100)
    
    turtle.pensize(10)
    turtle.pencolor("lightskyblue")
    turtle.pu()
    turtle.goto(0,0)
    turtle.seth(0)
    turtle.right(6*mm)
    turtle.pd() 
    turtle.forward(120)
    
    turtle.pensize(7)
    turtle.pencolor("gold")
    turtle.pu()
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.right(6*ss)
    turtle.pd() 
    turtle.forward(180)

    for i in range(12):
        turtle.pu()
        turtle.pensize(10)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor(r, g, b)

        turtle.seth(0)
        turtle.goto(0, 0)
        turtle.right(i*30)

        turtle.forward(240)
        turtle.forward(10)
        turtle.pd()
        turtle.forward(22)
        turtle.pu()

    turtle.update()
    turtle.ontimer(clock, 1000)


clock()
turtle.done()
