import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.hideturtle()
turtle.pensize(12)
s = 15
for i in range(15):
    turtle.pencolor("red")
    turtle.pu()
    turtle.goto(25*i, 0)
    turtle.pd()
    turtle.forward(s)
    s = s * 2
turtle.done()
