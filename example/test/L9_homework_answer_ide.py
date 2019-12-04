import turtle

turtle.colormode(255)
turtle.speed(30)

color=[]
plus=1

a=10,20,50
color.append(a)
b=40,20,80
color.append(b)
c=70,20,110
color.append(c)
d=100,20,140
color.append(d)

'''for i in range(4):
	a=10+30*i,20,50+30*i
	color.append(a)'''



for i in range(90):
    turtle.pencolor(color[i%4])
    turtle.pu()
    turtle.setpos(0,0)
	
    turtle.forward(100)
    turtle.pd()
    turtle.dot(30)
    turtle.right(4)

turtle.done()