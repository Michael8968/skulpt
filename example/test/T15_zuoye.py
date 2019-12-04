import turtle,random
turtle.shape('turtle')
turtle.mode("logo")
def sanjiao(num, color):
    for i in range(num):
        a=random.randint(-300,300)
        b=random.randint(-300,300)
        turtle.pu()
        turtle.goto(a,b)
        turtle.pd()
        turtle.pencolor(color)
        for j in range(3):
            turtle.forward(100)
            turtle.right(120)
sanjiao(3,'red')
turtle.done()
