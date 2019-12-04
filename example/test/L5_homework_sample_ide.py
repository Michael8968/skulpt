import turtle

turtle.colormode(255)
a=80
b=50
c=200

for i in range (20):
	turtle.pencolor(a,b,c)
	turtle.pu()
	turtle.forward(30)
	turtle.pd()
	turtle.dot(10+i)
	turtle.right(30)
	b=b+10
	
turtle.done()

