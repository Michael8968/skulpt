import turtle        
turtle.mode("logo")   #改坐标系
turtle.shape("turtle")  #改形状
turtle.speed(0) #速度范围(0-10), 0最快,1最慢,2-10依次加快
#开始黑色的龙卷风
for i in range(100):
    turtle.circle(i,180)
    turtle.right(90)

turtle.done()               #结束