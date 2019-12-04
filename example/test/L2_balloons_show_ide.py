import turtle


turtle.seth(90)#海龟头朝向北方


a=100#声明变量a
b=80#声明变量b

turtle.forward(a)
turtle.dot(b,'red')#第一个气球

turtle.pu()
turtle.goto(-200,-100)
turtle.pd()
turtle.forward(a)
turtle.dot(b,'pale green')#第二个气球

turtle.pu()
turtle.goto(-300,100)
turtle.pd()
turtle.forward(a)
turtle.dot(b,'pink')#第三个气球

turtle.pu()
turtle.goto(100,-100)
turtle.pd()
turtle.forward(a)
turtle.dot(b,'light blue')#第四个气球

turtle.done()#按下x关闭窗口