import turtle,random

string=input()

a = ord(string[random.randint(0,len(string)-1)])
b = ord(string[random.randint(0,len(string)-1)])
c = ord(string[random.randint(0,len(string)-1)])

turtle.colormode(255)
turtle.pensize(4)
print(a,b,c)
for i in range(4):
    turtle.color(200,int(c),random.randint(0,a))
    turtle.forward(b)
    turtle.right(c)

turtle.done()
