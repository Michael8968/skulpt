
#2先画棍子再画糖葫芦
import turtle
turtle.mode('logo')
turtle.tracer(False)
turtle.shape("turtle")
colors=['red','green','yellow','blue','gray','white']

turtle.forward(100)

for i in range(6):
    turtle.seth(90)
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.circle(10,360)
    turtle.end_fill()
    turtle.left(90)
    turtle.pu()
    turtle.forward(20)
    turtle.pd()
turtle.hideturtle()
turtle.update() 
turtle.done()