import turtle#导入turtle模块
turtle.seth(90)#海龟头朝向北方

turtle.forward(100)#向前移动100，画出气球线
turtle.dot(80,'red')#画出大小是80，颜色是红色的气球

turtle.pu()#抬笔
turtle.goto(-200,-100)#移动到坐标是(-200,-100)
turtle.pd()#落笔
turtle.forward(100)#向前移动100，画出气球线
turtle.dot(80,'pale green')#画出大小是80，颜色是绿色的气球

turtle.done()#按下x关闭窗口

