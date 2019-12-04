import turtle,random
turtle.mode("logo")
turtle.colormode(255)
turtle.tracer(False)
r1 = 200
def func():
    turtle.goto(0,0)
    turtle.fillcolor((random.randint(0,100),random.randint(200,255),random.randint(200,255)))
    turtle.begin_fill()
    turtle.pd()
    turtle.right(random.randint(0,360))
    turtle.forward(r1)
    turtle.left(90)
    turtle.circle(r1,30)
    turtle.left(90)
    turtle.forward(r1)
    turtle.end_fill()
    turtle.update()

def funleft():
    global r1
    func()
    r1 = r1 - 2
def funright():
    global r1
    func()
    r1 = r1 + 2
turtle.update()
turtle.onkeypress(funleft, "Left")
turtle.onkeypress(funright, 'Right')
turtle.listen()
turtle.done()
