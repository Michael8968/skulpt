import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.speed(9)
turtle.setup(600, 600)
y = 160
for j in range(12):
    turtle.penup()
    turtle.goto(300, y)
    turtle.pendown()
    y = y-10
    for i in range(5):
        turtle.circle(30, 180)
        turtle.circle(-30, 180)
turtle.done()
