import random
import turtle

turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)
turtle.colormode(255)
turtle.bgcolor(0, 0, 0)
turtle.pensize(6)

for j in range(12):

    for i in range(3):
        r = random.randint(230, 255)
        g = random.randint(0, 150)
        b = 0
        turtle.pencolor(r, g, b)
        turtle.circle(30-6*i, 180)
        turtle.right(180)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.right(30)
turtle.update()
turtle.done()
