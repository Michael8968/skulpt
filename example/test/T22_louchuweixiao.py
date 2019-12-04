import turtle
turtle.tracer(False)
turtle.mode('logo')
turtle.shape('turtle')



j = 7
flag = True


def head():
    turtle.pu()
    turtle.goto(0,50)
    turtle.pd()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.seth(-90)
    turtle.circle(80,360)
    turtle.end_fill()
    # 定义画脸函数


def mouth():
    global flag, j
    turtle.pu()
    turtle.goto(0, -65)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(40, 20+j)
    turtle.pu()
    turtle.goto(0, -65)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(40, -20-j)
    if j>50 or j<5:
        flag = not flag
    
    if flag==True:
        j = j + 3
    else:
        j=j-3
# 定义画嘴巴函数


def eye():
    turtle.pu()
    turtle.goto(-20,0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 左眼眶
    
    turtle.pu()
    turtle.goto(50,0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 右眼眶
    
    turtle.pu()
    turtle.goto(-35,0)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.goto(35,0)
    turtle.pd()
    turtle.dot(3)# 左眼珠+右眼珠


def emoji(x,y):
    turtle.clear()
    head()
    mouth()
    eye()# 定义整体函数


def emoji1(event):
    turtle.clear()
    head()
    mouth()
    eye()  # 定义整体函数
    turtle.update()


emoji("", "")
turtle.update()
turtle.hideturtle()
turtle.onscreenclick(emoji, btn=1)# 单机


cv = turtle.getcanvas()
cv.bind("<Motion>", emoji1) # 移动


turtle.done()