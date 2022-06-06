import turtle

L_str = input("Value of L ? ")
L = int(L_str)
angle = 360/L

my_turtle = turtle.Turtle()

for index in range(L):
    my_turtle.forward(50)
    my_turtle.right(angle)

turtle.done()