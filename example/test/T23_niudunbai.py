import turtle
turtle.mode("logo")
turtle.shape("turtle")
turtle.tracer(False)

aa = 60
turn_left = True


def ball(x, y, a):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.seth(a)
    turtle.forward(80)
    turtle.right(90)
    turtle.circle(10)
     # 定义画1条挂绳 + 小球的函数


def bai():
    global aa, turn_left
    turtle.clear()
    if aa >= 0 and aa <= 60:
        if aa == 60:
            turn_left = not turn_left
        # 设置标示
        if turn_left == True:
            aa += 1 # 左边小球上升
        else:
            aa -= 1
              # 左边小球下落
        ball(-120, 100, 180 + aa)
        ball(-20, 100, 180)
     # 左边小球摆动
    if aa >= -60 and aa < 0:
        if aa == -60:
            turn_left = not turn_left
         # 设置标示
        if turn_left == True:
            aa += 1
         # 右边小球下降
        else:
            aa -= 1
              # 右边小球上升
        ball(-120, 100, 180)
        ball(-20, 100, 180 + aa)
     # 右边小球摆动
    ball(-100, 100, 180)
    ball(-80, 100, 180)
    ball(-60, 100, 180)
    ball(-40, 100, 180) # 剩下的四个不动的球
    turtle.write(aa)
    turtle.hideturtle()
    turtle.update()
    turtle.ontimer(bai, 10)



bai()

turtle.done()
