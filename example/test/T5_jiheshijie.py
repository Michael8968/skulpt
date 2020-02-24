import turtle, random
turtle.mode("logo")
turtle.shape("turtle")
turtle.colormode(255)
turtle.tracer(False)
turtle.seth(0)
height = 250


def move(x, y):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()


turtle.pensize(0)
move(-285, 300)
turtle.fillcolor(122, 122, 122)
turtle.begin_fill()
turtle.seth(180)
turtle.forward(height)
turtle.circle(30, 60)
turtle.right(180)
turtle.circle(40, 360)
turtle.circle(40, 60)
turtle.right(180)
turtle.circle(30, 60)
turtle.forward(height)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
move(-290, -9)
turtle.pencolor('white')
turtle.pensize(1)
turtle.dot(66)
turtle.pencolor(0, 0, 0)
turtle.dot(24)

turtle.pensize(0)
move(-285, -300)
turtle.fillcolor(122, 122, 122)
turtle.begin_fill()
turtle.seth(0)
turtle.forward(10)
turtle.circle(20, 60)
turtle.right(180)
turtle.circle(30, 360)
turtle.circle(30, 60)
turtle.right(180)
turtle.circle(20, 60)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
move(-280, -246)
turtle.pencolor('white')
turtle.pensize(1)
turtle.dot(50)
#三角形
turtle.pensize(10)
turtle.pencolor(0, 0, 0)
move(-165,- 300)
turtle.seth(0)
turtle.forward(400)
move(-225, 100)
turtle.seth(90)
turtle.forward(120)
turtle.left(120)
turtle.forward(120)
turtle.left(120)
turtle.forward(120)

#正方形
move(-60, 300)
turtle.pensize(10)
turtle.pencolor('gray')
turtle.seth(180)
turtle.forward(430)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(40)
turtle.pensize(0)


turtle.pensize(0)
move(20, 300)
turtle.fillcolor(0, 0, 0)
turtle.begin_fill()
turtle.seth(180)
turtle.forward(200)
turtle.circle(15,60)
turtle.right(180)
turtle.circle(20, 360)
turtle.circle(20, 60)
turtle.right(180)
turtle.circle(15, 60)
turtle.forward(200)
turtle.right(90)
turtle.forward(2.5)
turtle.end_fill()
move(16, 71)
turtle.pencolor('white')
turtle.pensize(1)
turtle.dot(30)
turtle.pencolor(122, 122, 122)
turtle.dot(24)

turtle.pensize(0)
move(200, 300)
turtle.fillcolor(122, 122, 122)
turtle.begin_fill()
turtle.seth(180)
turtle.forward(30)
turtle.circle(20, 60)
turtle.right(180)
turtle.circle(30, 360)
turtle.circle(30, 60)
turtle.right(180)
turtle.circle(20,60)
turtle.forward(30)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
move(195, 228)
turtle.pencolor('white')
turtle.pensize(1)
turtle.dot(50)
turtle.pencolor(0, 0, 0)
turtle.dot(40)
#六边形
move(120, 300)
turtle.seth(-180)
turtle.pensize(15)
turtle.forward(250)
turtle.right(90)
move(150, 50)
for i in range(6):
    turtle.forward(60)
    turtle.left(60)


turtle.pencolor('gray')
move(120, -68)
turtle.pensize(15)
turtle.seth(180)
turtle.forward(240)

turtle.pensize(0)
move(230, -300)
turtle.fillcolor(122, 122, 122)
turtle.begin_fill()
turtle.seth(0)
turtle.forward(10)
turtle.circle(20, 60)
turtle.right(180)
turtle.circle(30, 360)
turtle.circle(30, 60)
turtle.right(180)
turtle.circle(20,60)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
move(235, -246)
turtle.pencolor('white')
turtle.pensize(1)
turtle.dot(50)
turtle.pencolor('red')
turtle.dot(40)
turtle.pensize(0)
turtle.update()
turtle.done()