import turtle

# get width and height
x_str = input("Rectangle width ? ") 
x = float(x_str)
y_str = input("Rectangle height ? ") 
y = float(y_str)

# create the turtle
my_turtle = turtle.Turtle()
my_turtle.forward(x)
my_turtle.right(90)
my_turtle.forward(y)
my_turtle.right(90)
my_turtle.forward(x)
my_turtle.right(90)
my_turtle.forward(y)
my_turtle.right(90)

turtle.done()