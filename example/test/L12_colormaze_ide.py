import turtle

turtle.tracer(30)
colors=['red','yellow','blue','green']

for i in range(20):
	turtle.pensize(3)
	turtle.pencolor(colors[i%4])
	turtle.forward(80+4*i)
	turtle.right(91)


turtle.done()