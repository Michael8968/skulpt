import turtle,random
turtle.mode("logo")
turtle.shape("turtle")
turtle.colormode(255)
#turtle.speed(0.3)


def tri(e):
    turtle.pensize(3)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.fillcolor(r, g, b)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(10+e)
        turtle.right(120)
    turtle.end_fill()
  #画1个三角形


def diamond(d,e,f):
    turtle.pu()
    turtle.goto(0,0)
    turtle.seth(f)
    turtle.left(90)
    turtle.pd()
    tri(d)
    turtle.forward(10+d)
    turtle.right(180)
    tri(d)

    #画两个三角形组成一个菱形


d = 40
e = 50
f = 0
diamond(d,e,f)
turtle.done()
