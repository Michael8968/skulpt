import turtle
turtle.speed(20)

turtle.colormode(255)
a=10
b=50
c=250

turtle.pensize(2)

for i in range(60):
    turtle.pencolor(a,b,c)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    turtle.right(6)
    a=a+3
    c=c-3

turtle.done()