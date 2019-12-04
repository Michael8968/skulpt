import turtle
turtle.tracer(False)
a = 90
def aa():
    global a
    turtle.goto(0,0)
    turtle.clear()
    for i in range(100):
    
        if(i % 4 ==1):
            turtle.pencolor("red")
     
        elif (i % 4 == 2):
            turtle.pencolor("green")
          
        elif ( i  % 4 == 3):
            turtle.pencolor("yellow")
          
        elif ( i  % 4 == 0):
            turtle.pencolor("blue")
         
        turtle.circle(i,180)
        turtle.right(a)
       
        a=a+1
        if(a==96):
            a=90
            
    turtle.update()
    turtle.ontimer(aa, 1000)

aa()
turtle.done()
