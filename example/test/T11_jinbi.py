#a装每一块砖撞出的金币,sum装金币总和
import turtle

a = 1
sum = 0
for i in range(4):
    sum = sum+a
    a = a+2
turtle.write(sum)
turtle.done()