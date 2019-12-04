import turtle
import random
turtle.mode("logo")
turtle.shape("turtle")
a = 100
b = 30

turtle.pu()
turtle.goto(20, random.randint(80, 100))
turtle.pd()
turtle.pencolor('green')
turtle.forward(a)
turtle.dot(random.randint(30, 50))

turtle.pu()
turtle.goto(0, -10)
turtle.pd()
turtle.pencolor('red')
turtle.forward(a)
turtle.dot(random.randint(30, 50))

turtle.pu()
turtle.goto(-30, 50)
turtle.pd()
turtle.pencolor('blue')
turtle.forward(a)
turtle.dot(random.randint(30, 50))

turtle.pu()
turtle.goto(random.randint(30, 100), 80)
turtle.pd()
turtle.pencolor('orange')
turtle.forward(a)
turtle.dot(random.randint(30, 50))
turtle.done()
