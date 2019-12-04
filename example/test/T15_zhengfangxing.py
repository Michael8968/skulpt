import turtle,random
turtle.tracer(False)
turtle.mode("logo")
turtle.shape('turtle')
def super_square(color):
    turtle.pencolor(color)
    turtle.colormode(255)
    turtle.pensize(7)
    for j in range(5):
        a = random.randint(-200,200)
        b = random.randint(-200,200)
        turtle.penup()
        turtle.goto(a,b)
        turtle.pendown()
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)

super_square('red')
turtle.update()
turtle.done()
