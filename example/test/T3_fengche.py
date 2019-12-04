import turtle

turtle.mode("logo")
turtle.shape("turtle")          # 让画笔变成海龟(turtle)
turtle.hideturtle()               # 隐藏画笔

turtle.pencolor("orange")
turtle.pensize(4)



# 第1个风车扇叶
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.right(120)



# 第2个风车扇叶
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.right(120)



# 第3个风车扇叶
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.right(120)


# 风车柄
turtle.right(180)
turtle.forward(200)


turtle.done()
