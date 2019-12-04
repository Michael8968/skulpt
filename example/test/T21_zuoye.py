import turtle
turtle.tracer(False)
turtle.mode('logo')
turtle.shape('turtle')
i = 0
colors = ['red', 'green', 'yellow', 'blue']
x = turtle.getcanvas().winfo_width()/2
y = turtle.getcanvas().winfo_height()/2


def square(a, b, color):
    turtle.clear()
    turtle.pu()
    turtle.goto(a, b)
    turtle.pd()
    turtle.pensize(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.update()


def draw_square(event):
    square(event.x-x, y-event.y, colors[i])


def change(x, y):
    global i
    i += 1
    if i > len(colors) - 1:
        i = 0
    square(x, y, colors[i])


cv = turtle.getcanvas()
cv.bind("<Motion>", draw_square)

turtle.onscreenclick(change, btn=1)
turtle.done()
