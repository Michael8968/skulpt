import turtle
turtle.mode("logo")
turtle.hideturtle()
turtle.pencolor("blue")
turtle.pensize(5)
a = 5
for i in range(6):
    turtle.pu()
    turtle.goto(a, 0)
    turtle.pd()
    turtle.circle(a)
    a = a+10
turtle.done()
