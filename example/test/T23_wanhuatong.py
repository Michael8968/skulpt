import turtle, random

turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)
turtle.colormode(255)


def tri(e):
    turtle.pensize(0)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.fillcolor(r, g, b)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(10 + e)
        turtle.right(120)
    turtle.end_fill()


# //画1个三角形

def diamond(e):
    tri(e)
    turtle.forward(10 + e)
    turtle.right(180)
    tri(e)


# }//画两个三角形组成一个菱形

a = 0
b = 30
e = 1


def circle(a, b, e):
    for i in range(18):
        turtle.pu()
        turtle.goto(0, 0)
        turtle.seth(0)
        turtle.right(20 + a)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(5 + e / 2)
        turtle.left(180)
        turtle.pd()
        diamond(e)
        a = a + 20


# //画一圈菱形
def all_diamond():
    turtle.bgcolor('black')
    circle(0, 30, 3)
    circle(10, 60, 8)
    circle(0, 100, 13)
    circle(10, 150, 18)
    circle(0, 210, 23)
    circle(10, 280, 28)
    turtle.update()
    turtle.ontimer(all_diamond, 1000)


# 画很多圈菱形

all_diamond()
turtle.done()
