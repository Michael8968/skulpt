import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)
turtle.colormode(255)
turtle.bgcolor(0, 0, 0)
turtle.pencolor('yellow')
turtle.pensize(2)
for i in range(100):
    turtle.circle(30+i)
    turtle.right(10)

turtle.update()
turtle.done()
