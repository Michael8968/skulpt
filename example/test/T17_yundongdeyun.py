import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)
turtle.colormode(255)
x=0
def cloud():
    global x
    turtle.clear()
    turtle.bgcolor(0,255,255)
    turtle.pu()
    turtle.seth(0)
    turtle.goto(-300+x*40,205)
    turtle.pencolor("white")
    turtle.fillcolor(255,255,255)
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(30, 90)
    turtle.right(90)
    turtle.circle(30, 180)
    turtle.right(90)
    turtle.circle(30, 90)
    turtle.left(90)
    turtle.goto(-300+x*40,205)
    turtle.end_fill()
    x=x+1;
    if x>20:
        x = 0

    turtle.hideturtle()
    turtle.update()
    turtle.ontimer(cloud,1000)
cloud()
turtle.done()
