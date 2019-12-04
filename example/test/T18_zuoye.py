import turtle
def bijiao(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return 'equal'
c=bijiao(4,3)
turtle.write(c)
turtle.done()
