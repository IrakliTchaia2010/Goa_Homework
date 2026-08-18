import turtle
x=turtle.Turtle()
y=turtle.Turtle()

x.pendown()
y.pendown()
x.color("red")
y.color("blue")

x.left(0)
y.left(90)
x.forward(100)
y.forward(100)

x.penup()
y.penup()
x.goto(0,0)
y.goto(0,0)

x.left(180)
y.left(180)
x.pendown()
y.pendown()
x.forward(100)
y.forward(100)

turtle.exitonclick()