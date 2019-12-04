import turtle
turtle.tracer(False)
turtle.mode('logo')
turtle.shape('turtle')

x = turtle.getcanvas().winfo_width()/2
y = turtle.getcanvas().winfo_height()/2


def square(a, b):
    turtle.pencolor("black")
    turtle.clear()
    turtle.pu()
    turtle.goto(a, b)
    turtle.pd()    
    for i in range(4):
        turtle.forward(50)        
        turtle.right(90)
    turtle.update()


def draw_square(event):
    square(event.x - x, y - event.y)
    # if y-event.y > 0:
    #     square(event.x-x, y-event.y)
    # if event.x-x > 0:
    #     square(event.x-x, y-event.y)
    #


cv = turtle.getcanvas()
cv.bind("<Motion>", draw_square)


turtle.done()
