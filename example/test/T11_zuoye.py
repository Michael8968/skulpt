import turtle        
turtle.mode("logo")   #改坐标系
turtle.shape("turtle")  #改形状

#开始画花的轮廓
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.circle(20,180)
    turtle.right(108)
turtle.end_fill()


#开始画花心
turtle.pu()
turtle.goto(-21,-26)
turtle.pd()
turtle.pencolor("yellow")
turtle.dot(20)
turtle.hideturtle()

turtle.done()               #结束