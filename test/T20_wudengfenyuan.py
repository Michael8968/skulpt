import turtle
turtle.mode('logo')
turtle.tracer(False)
colors=['red','green','yellow','blue','gray']
#colors = list(reversed(colors))

for i in range(len(colors)):
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(100,360/len(colors))
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.right(180)
    turtle.update()

turtle.done()
