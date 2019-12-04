import turtle

turtle.tracer(20)
#turtle.speed(0.2)
colors=['red','yellow','blue','green']

c=0

for h in range(10):
    for j in range(6):
        turtle.pu()
        turtle.goto(0,0)
        turtle.seth(10*h)
        turtle.right(60*j)
        turtle.forward(30+18*h)
        turtle.pd()
 
        for i in range(30):
            turtle.pencolor(colors[i%4])
            turtle.forward(7+i+c)    
            turtle.right(91)
    c+=10
turtle.done()