import turtle

turtle.tracer(20) 

colors=['red','yellow','blue','green','orange','purple']



for j in range(10):
    for i in range(6):
        turtle.pu()
        turtle.goto(0,0)
        turtle.seth(0)
        turtle.right(60*i)
        turtle.forward(30+18*j)
        turtle.pd()
        turtle.pencolor(colors[i%6])
        turtle.dot(2+j*3)

turtle.done()