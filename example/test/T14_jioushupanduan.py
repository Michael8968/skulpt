import turtle
import random
turtle.mode("logo")
turtle.shape("turtle")
a=turtle.numinput("","number?")

if a%2!=0:
    rand1=random.randint(-300,0)
    rand2=random.randint(-300,300)
    turtle.penup()
    turtle.goto(rand1,rand2)
    turtle.pendown()
    turtle.circle(50)
elif a%2==0 and a!=0:
    rand3 = random.randint(0,300)
    rand4 = random.randint(-300,300)
    turtle.penup()
    turtle.goto(rand3,rand4)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
else:
    turtle.write("zero")
    turtle.hideturtle()
turtle.done()
