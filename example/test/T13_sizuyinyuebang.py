import turtle
import random
turtle.mode("logo")
turtle.shape("turtle")
turtle.penup()
turtle.goto(-251,-100)
turtle.pendown()
turtle.speed(1)
turtle.pensize(10)
for j in range(4):
    length =5
    for i in range(20):
        rand1=random.randint(0,255)
        rand2=random.randint(0,255)
        rand3=random.randint(0,255)
        turtle.colormode(255)
        turtle.pencolor(rand1,rand2,rand3)
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
        length=length+5
    turtle.left(90)
turtle.done()
