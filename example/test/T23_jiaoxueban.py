import turtle

turtle.mode("logo")
turtle.tracer(False)
turtle.shape("turtle")
turtle.colormode(255)
angle = 0
dict = 'shun'


def rect(angle, n):
    turtle.goto(0, 0)
    turtle.seth(angle)
    turtle.pu()
    turtle.forward(100)
    turtle.pd()
    turtle.right(90)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)


def shan(angle):
    turtle.pencolor('green')
    turtle.goto(0, 0)
    if angle > 0:
        turtle.seth(angle)
        turtle.forward(141)
        turtle.left(90)
        turtle.circle(141,angle)
        turtle.left(90)
        turtle.forward(141)

    else:
        turtle.seth(0)
        turtle.forward(141)
        turtle.left(90)
        turtle.circle(141,-angle)
        turtle.left(90)
        turtle.forward(141)

    turtle.goto(0, 0)
    turtle.fillcolor('gray')
    turtle.begin_fill()
    if angle > 0:
        turtle.seth(angle)
        turtle.forward(30)
        turtle.left(90)
        turtle.circle(30,angle)
        turtle.left(90)
        turtle.forward(30)

    else:
        turtle.seth(0)
        turtle.forward(30)
        turtle.left(90)
        turtle.circle(30, -angle)
        turtle.left(90)
        turtle.forward(30)

    turtle.end_fill()
    turtle.pencolor(0, 0, 0)


def zhun():
    global angle, dict
    if angle == 30:
        angle -= 1
        dict = 'ni'

    elif angle == -30:
        angle += 1
        dict = 'shun'

    else:
        if dict == 'shun':
            angle += 1
        else:
            angle -= 1

    turtle.clear()
    rect(angle, 1)
    shan(angle)
    turtle.write(angle)
    turtle.update()
    turtle.ontimer(zhun, 100)


zhun()
turtle.done()
