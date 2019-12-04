import turtle
turtle.speed(30)

color=['red','yellow','blue','green']
for i in range(120):
	turtle.pencolor(color[i%4])
	turtle.pu()
	turtle.setpos(0,0)
	
	turtle.forward(100)
	turtle.pd()
	turtle.dot(30)
	turtle.right(3)

turtle.done()