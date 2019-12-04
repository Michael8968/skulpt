import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.colormode(255)
turtle.bgcolor(0, 0, 0)
turtle.pensize(6)
turtle.pencolor("aqua")
for j in range(10):
    for i in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)

    turtle.right(36)

turtle.done()
