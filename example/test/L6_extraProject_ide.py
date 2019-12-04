import turtle,random
string = input()
turtle.speed(0.3)

a = ord(string[random.randint(0,len(string)-1)])
b = ord(string[random.randint(0,len(string)-1)])
c = ord(string[random.randint(0,len(string)-1)])
d = ord(string[random.randint(0,len(string)-1)])
e = ord(string[random.randint(0,len(string)-1)])

turtle.colormode(255)
turtle.pensize(30)
print(a,b,c,d,e)

for i in range(int(a/4)):

    turtle.pensize(4)
    turtle.pencolor(random.randint(0,a),int(c*0.8),random.randint(0,c))
    turtle.forward(a)
    turtle.left(b)
    turtle.forward(e)
    turtle.left(d-30)
    turtle.forward(c)
    turtle.left(d)

turtle.done()
