import turtle
turtle.mode("logo")
turtle.tracer(False)
turtle.shape("turtle")
turtle.colormode(255)

# 画栅栏
def zhalan(x,y,chang,gao):
    turtle.pu()
    turtle.seth(0)
    turtle.goto(x,y)
    turtle.pd()
    turtle.fillcolor(255,255,255)
    turtle.begin_fill()
    turtle.forward(gao)
    turtle.right(90)
    turtle.forward(chang)
    turtle.right(90)
    turtle.forward(gao)
    turtle.right(90)
    turtle.forward(chang)
    turtle.end_fill()
    

def zhalan_all( ):
    zhalan(-216,-10,130,15)
    zhalan(-216,-40,130,15)
    zhalan(-190,-60,15,80)
    zhalan(-160,-60,15,80)
    zhalan(-130,-60,15,80)
 

# 画云
def yun(x,y):
    
    #turtle.bgcolor(0,255,255)
    
    # 背景，用bgcolor 会闪
    turtle.goto(-480,-60)
    turtle.seth(90)
    turtle.fillcolor(0,255,255)
    turtle.begin_fill()
    turtle.pd()
    turtle.forward(960)
    turtle.left(90)
    turtle.forward(470)
    turtle.left(90)
    turtle.forward(960)
    turtle.left(90)
    turtle.forward(470)
    turtle.end_fill()    
    
    turtle.pu()
    turtle.seth(0)
    turtle.pencolor("white")
    turtle.goto(x,y)
    turtle.fillcolor(255,255,255)
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(30, 90)
    turtle.right(90)
    turtle.circle(30, 180)  
    turtle.right(90)
    turtle.circle(30, 90)       
    turtle.left(90)
    turtle.goto(x,y) 
    turtle.end_fill()
    turtle.pensize(1)



# 画地面
def dimian():
    turtle.pu()
    turtle.seth(0)
    turtle.pensize(0)
    turtle.goto(-480,-60)
    turtle.fillcolor(255,144,48)
    turtle.begin_fill()
    turtle.pd()
    turtle.right(90)
    turtle.forward(960)
    turtle.right(90)
    turtle.forward(340)
    turtle.right(90)
    turtle.forward(960)
    turtle.right(90)
    turtle.forward(340)
    turtle.end_fill()
    turtle.pu()
    turtle.pencolor("black")
    for i in range(10):
        turtle.goto(30+i*i,-59.5)
        turtle.pd()
        turtle.dot(5)





# 画身体
def shenti():
    turtle.pu()
    turtle.seth(90)
    turtle.goto(100,-45) 
    turtle.pensize(1)
    turtle.fillcolor(255,255,96)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(30,360)
    turtle.end_fill()


# 画左脚
def left(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.seth(195)
    turtle.pd()
    turtle.forward(15)



# 画右脚
def right(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.seth(165)
    turtle.forward(15)


# 画头
def bgpic():
    
    yun(42,205)
    zhalan_all()
    dimian()
    shenti()
    left(90,-43)
    right(105,-45)

def head(x,y):
    turtle.pu()
    turtle.seth(330)
    turtle.goto(x,y)
    turtle.pd()
    turtle.fillcolor(255,255,96)
    turtle.begin_fill()
    turtle.circle(15,360)
    turtle.end_fill()


# 画嘴
def mouth(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.fillcolor(192,96,48)
    turtle.begin_fill()   
    turtle.seth(165)
    turtle.forward(18)
    turtle.seth(15)
    turtle.forward(18)
    turtle.end_fill()   


# 画眼睛
def eye(x,y):
    turtle.pu()
    turtle.seth(90)
    turtle.goto(x,y)
    turtle.fillcolor(0,0,0)
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(1,360)
    turtle.end_fill()



# 低头
def ditou():
    turtle.clear()
    bgpic()
    head(68,-21)
    mouth(51,-42)
    eye(52,-30)
    turtle.hideturtle()
    turtle.update()

# 抬头
def taitou():
    turtle.clear()
    bgpic()
    head(68,-10)
    mouth(47,-31)
    eye(53,-15)
    turtle.hideturtle()
    turtle.update()



taitou()

# 按键交互
turtle.onkeypress(ditou, 'space')
turtle.onkeyrelease(taitou, 'space')
turtle.listen()
turtle.done()
