#1先画糖葫芦再画棍子
import turtle
turtle.mode('logo')
turtle.tracer(False)
turtle.shape("turtle")
colors=['red','green','yellow','blue','gray','white']

for i in range(6):
    turtle.pu()
    turtle.seth(0)
    turtle.forward(30)
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(15,360)
    turtle.end_fill()

turtle.pu()
turtle.goto(-15,14)
turtle.seth(180)
turtle.pd()
turtle.forward(100)
turtle.hideturtle()
turtle.update()
turtle.done()
