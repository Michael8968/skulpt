import random
import turtle

turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)
turtle.colormode(255)
turtle.bgcolor(0, 0, 0)
turtle.setup(600, 600)

turtle.penup()
turtle.goto(-240, 240)
turtle.pencolor('yellow')
turtle.pendown()
turtle.dot(50)

turtle.penup()
turtle.pencolor('blue')
turtle.goto(-100, -80)
turtle.pendown()
turtle.pensize(3)
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(2):
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)

turtle.end_fill()

turtle.pensize(4)
y = 160
for j in range(12):
    turtle.penup()
    turtle.goto(300, y)
    turtle.pendown()
    y = y-10
    for i in range(5):
        r = 0
        g = random.randint(0, 150)
        b = random.randint(230, 255)
        turtle.pencolor(r, g, b)
        turtle.circle(30, 180)
        turtle.circle(-30, 180)
turtle.update()
turtle.done()
