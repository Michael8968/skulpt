import turtle
turtle.mode("logo")
turtle.shape("turtle")
h = turtle.numinput("","your height?")
if h<1.2:
    turtle.write("free!")
else:
    turtle.write("ticket!")
turtle.hideturtle()
turtle.done()             
