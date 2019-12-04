import turtle,random
turtle.mode("logo")
turtle.shape("turtle")
turtle.speed(0)
turtle.bgcolor(0,0,0)
turtle.pensize(8)
turtle.colormode(255)
for j in range(10):
    for i in range(2):
        r = random.randint(230,255)
        g = random.randint(0,150)
        b = 0
        turtle.pencolor(r,g,b)
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
    turtle.right(36)
turtle.done()
