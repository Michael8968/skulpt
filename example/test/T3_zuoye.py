import turtle
import random
turtle.mode("logo")

a = random.randint(3,18)
turtle.pensize(a)

turtle.pencolor("orange")
turtle.right(90)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)

turtle.pu()
turtle.goto(0,-58)
turtle.pd()
turtle.pencolor("blue")

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)


turtle.done()
