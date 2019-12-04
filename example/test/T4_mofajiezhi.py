import turtle

turtle.shape("turtle")
turtle.mode("logo")
# 圆环
turtle.pencolor('red')
turtle.dot(200)
turtle.pencolor("white")
turtle.dot(160)
# 移动
turtle.pu()
turtle.goto(-35,70)
turtle.pd()
# 六边形
turtle.pensize(5)
turtle.pencolor("blue")
turtle.right(90)
turtle.fillcolor("white")
turtle.begin_fill()
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.end_fill()


turtle.done()
