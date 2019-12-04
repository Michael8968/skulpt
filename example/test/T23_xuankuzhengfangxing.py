import time,turtle,random
turtle.mode("logo")
turtle.shape("turtle")
turtle.colormode(255)
turtle.tracer(False)
turtle.pensize(8)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

color =(r,g,b) 


def square(a,b,s):
    turtle.pencolor(color)
    turtle.pu()
    turtle.seth(b)
    turtle.goto(0,100+a)
    turtle.left(90)
    turtle.pd()
    turtle.forward(25+a)
    for i in range(4):
        turtle.left(90)
        turtle.forward(50+2*a)


flag = True
d = 0


def all_square():
    global d,flag
    turtle.clear()
    square(5,d,20)
    square(20,d/2,35)
    square(35,d/3,50)
    square(50,d/4,65)
    #square(65, d/5, 80)
    if d>30 or d<-30:
        flag=not flag
   #//设置标示

    if flag==True:
        d=d+1
   #//当标示为true

    if flag == False:
        d=d-1
    # }//当标示为false
    turtle.update()
    turtle.ontimer(all_square,10)


#//画出4个正方形并且扭来扭去
all_square()

turtle.done()
