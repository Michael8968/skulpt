import turtle
turtle.mode("logo")
turtle.shape("turtle")
h=turtle.numinput("","your height?")
if h<1.2:
    turtle.write("free")
elif h>=1.2 or h<1.5:
    turtle.write("half")
elif h>=1.5:
    turtle.write("money")
turtle.done()
