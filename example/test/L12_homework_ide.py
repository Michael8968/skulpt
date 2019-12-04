import turtle
turtle.tracer(20)

colors=['red','yellow','orange','green','blue','purple']
turtle.pensize(8)


for j in range(5):
    turtle.pu()
    turtle.goto(-475,60*j)
    turtle.pd()
    for i in range(40):
        turtle.pencolor(colors[j%6])
        turtle.seth(90)
        for h in range(3):
            turtle.forward(30+4*j)
            turtle.right(90)
        turtle.left(180)
        turtle.forward(30+4*j)
        
turtle.done()