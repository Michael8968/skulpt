import turtle

turtle.mode("logo")
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.hideturtle()
turtle.pensize(12)
turtle.colormode(255)

s = 50
a = 0
for i in range(10):
    turtle.pencolor(200-a, a, 100)
    turtle.pu()
    turtle.goto(25*i, 0)
    turtle.pd()
    turtle.forward(s)
    a = a + 20
    s = s + 10


turtle.done()
