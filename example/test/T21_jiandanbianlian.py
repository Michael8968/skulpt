import turtle
turtle.tracer(False)
turtle.mode('logo')
turtle.shape('turtle')
i = 0
colors=['red', 'yellow', 'green', 'blue']# 定义颜色数组


def head(color):
    turtle.pu()
    turtle.goto(0, 50)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pd()
    turtle.seth(-90)
    turtle.circle(80, 360)
    turtle.end_fill()# 画脸


def mouth():
    turtle.pu()
    turtle.goto(-20, -60)
    turtle.pd()
    turtle.seth(120)
    turtle.circle(40, 60)# 画嘴巴


def eye():
    turtle.pu()
    turtle.goto(-20, 0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 左眼
    
    turtle.pu()
    turtle.goto(50, 0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 右眼
    
    turtle.pu()
    turtle.goto(-35, 0)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.goto(35, 0)
    turtle.pd()
    turtle.dot(3)# 左眼珠+右眼珠


def emoji(color):
    turtle.clear()
    head(color)
    mouth()
    eye()# 定义整体函数


def change(x, y):
    global i
    i += 1
    if i > len(colors) - 1:
        i = 0
    emoji(colors[i])
    turtle.update()

#点击鼠标左键后调用函数emoji
turtle.onscreenclick(change, btn=1)

turtle.done()
