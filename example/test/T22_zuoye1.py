import turtle
turtle.tracer(False)
turtle.mode('logo')
turtle.shape('turtle')
i = 0
a = -35
b = 0
colors = ['red', 'yellow', 'green', 'blue']# 定义颜色数组
x = turtle.getcanvas().winfo_width()/2
y = turtle.getcanvas().winfo_height()/2


def head(color):
    turtle.pu()
    turtle.goto(0, 50)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pd()
    turtle.seth(-90)
    turtle.circle(80, 360)
    turtle.end_fill()# 定义画脸函数


j = 7
flag = True


def mouth():
    global j, flag
    turtle.pu()
    turtle.goto(0, -65)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(40, 20 + j)
    turtle.pu()
    turtle.goto(0, -65)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(40, -20-j)
    if j > 50 or j < 5:
        flag = not flag
    if flag == True:
        j = j + 3
    else:
        j = j - 3
# 定义画嘴巴函数


def eye(a, b):
    turtle.pu()
    turtle.goto(-20, 0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 左眼眶
    
    turtle.pu()
    turtle.goto(50, 0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 右眼眶
    
    turtle.pu()
    turtle.goto(a, b)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.goto(a+70, b)
    turtle.pd()
    turtle.dot(3)# 左眼珠+右眼珠


def emoji(color, a, b):
    turtle.clear()
    head(color)
    mouth()
    eye(a, b)# 定义整体函数
    turtle.update()

def change(x, y):
    global i
    i += 1
    if i > len(colors) - 1:
        i = 0
    emoji(colors[i], a, b)
    #print(x,y)


def change_eye(event):

    if event.x-x > -300 and event.x-x< -100:
        if y-event.y>100:
            emoji(colors[i], -45, 2)
        elif y-event.y<-100:
            emoji(colors[i], -45, -2)
        else:
            emoji(colors[i], -45, 0)
    elif event.x-x > 100 and event.x-x < 300:
        if y - event.y > 100:
            emoji(colors[i], -25, 2)
        elif y-event.y < -100:
            emoji(colors[i], -25, -2)
        else:
            emoji(colors[i], -25, 0)
    else:
        if y - event.y > 100:
            emoji(colors[i], -35, 5)
        elif y-event.y < -100:
            emoji(colors[i], -35, -5)
        else:
            emoji(colors[i], -35, 0)
    turtle.update()


emoji(colors[i], -35, 0)
turtle.update()
turtle.hideturtle()
turtle.onscreenclick(change, btn=1)
# 点击鼠标后调用函数emoji

cv = turtle.getcanvas()
cv.bind("<Motion>", change_eye)

turtle.done()