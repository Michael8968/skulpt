import turtle
from datetime import datetime
turtle.tracer(False)
turtle.mode("logo")
def clock():
    turtle.clear()
    
    shijian = datetime.now()
    hh = shijian.hour
    mm = shijian.minute
    ss = shijian.second
    
    turtle.pensize(20)
    turtle.pencolor("lightgreen")
    turtle.pu()
    turtle.goto(0,0)
    turtle.seth(0)
    turtle.right(30 * hh)
    turtle.pd() 
    turtle.forward(100)
    
    turtle.pensize(10)
    turtle.color("lightskyblue")
    turtle.pu()
    turtle.goto(0,0)
    turtle.seth(0)
    turtle.right(6 * mm )
    turtle.pd() 
    turtle.forward(120)
    
    turtle.pensize(7)
    turtle.color("gold")
    turtle.pu()
    turtle.goto(0,0)
    turtle.seth(0)
    turtle.right(6 * ss)
    turtle.pd() 
    turtle.forward(180)
    
    turtle.update()
    turtle.ontimer(clock,1000)   
clock()
turtle.done()
    
    
    
