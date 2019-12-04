import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.colormode(255)
def cloud():

    turtle.bgcolor(0,255,255)
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(70, 90)
    turtle.right(90)
    turtle.circle(70, 180)
    turtle.right(90)
    turtle.circle(70, 90)
    turtle.left(90)
    turtle.goto(0,0)
    turtle.end_fill()

cloud()
turtle.done()
