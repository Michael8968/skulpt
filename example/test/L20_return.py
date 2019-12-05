import turtle

def scale(a,b,c):
	a = a*c
	b = b*c 

	return a,b

h,w=scale(4,8,20)

for i in range(2):
	turtle.forward(h)
	turtle.right(90)
	turtle.forward(w)
	turtle.right(90)

turtle.done()


