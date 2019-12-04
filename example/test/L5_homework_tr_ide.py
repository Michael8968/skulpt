import turtle

turtle.colormode(255)
#第一个点的颜色80，50，200
size=10
r=80
g=50
b=200

for i in range(15):
    turtle.pencolor(r,g,b)
    turtle.pu()
    turtle.goto(0,0)
    turtle.forward(40)
    turtle.pd()
    turtle.dot(size)
    turtle.right(30)

    size=size+1
    b=b-10
    g=g+10
    r=r+3


turtle.done()

