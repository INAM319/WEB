import turtle
turtle.bgcolor('black')
p=turtle.Turtle()
wn = turtle.Screen()
p.pencolor('red')
p.hideturtle()
#curve01
def curve01(a,d):
    for i in range(d):
        p.right(a)
        p.forward(1)