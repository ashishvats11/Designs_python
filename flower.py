import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red","blue","green","purple","orange"]

for i in range(100):
    t.pencolor(colors[i % 5])
    t.circle(80)
    t.left(360/10)

turtle.done()