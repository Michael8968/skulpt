import random
import turtle

turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)
turtle.colormode(255)
turtle.pensize(8)

for j in range(12):
    for i in range(4):
        r = random.randint(230,255)
        g = random.randint(0,100)
        b = 0
        turtle.pencolor(r,g,b)
        turtle.forward(150)
        turtle.right(90)
    turtle.right(30)
turtle.update()
turtle.done()
