import turtle
screen = turtle.Screen()
screen.setup(900, 800)
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()
circle.goto(0, 350)
circle.stamp()
k = 0
for i in range(1, 20):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x, -y+350)
        square.stamp()
        square.goto(-x, -y+350)
        square.stamp()
    if i % 4 == 0:
        x = 30*(j+1)
        circle.color('red')
        circle.goto(-x, -y+350)
        circle.stamp()
        circle.goto(x, -y+350)
        circle.stamp()
        k += 2
    if i % 4 == 3:
        x = 30*(j+1)
        circle.color('yellow')
        circle.goto(-x, -y+350)
        circle.stamp()
        circle.goto(x, -y+350)
        circle.stamp()
square.color('brown')
for i in range(20, 23):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x, -y+350)
        square.stamp()
        square.goto(-x, -y+350)
        square.stamp()
turtle.exitonclick()
