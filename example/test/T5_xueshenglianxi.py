import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.colormode(255)
# 三角形：
turtle.pu()
turtle.goto(-200, 114)
turtle.pd()
turtle.fillcolor('gray')
turtle.begin_fill()
turtle.right(180)
turtle.forward(70)
turtle.left(120)
turtle.forward(70)
turtle.left(120)
turtle.forward(70)
turtle.left(120)
turtle.end_fill()

# 正方形：
turtle.pu()
turtle.goto(-88, -142)
turtle.pd()
turtle.fillcolor(0, 0, 0)
turtle.begin_fill()
turtle.forward(55)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.end_fill()

# 六边形：
turtle.pu()
turtle.goto(98, 36)
turtle.pd()
turtle.fillcolor('red')
turtle.begin_fill()
for i in range(6):
    turtle.forward(45)
    turtle.right(60)

turtle.end_fill()


turtle.done()
