import turtle

def draw_rectangle(shape, color, x, y, dx=100, dy=150, fill=True):
    shape.penup()
    shape.goto(x, y)
    shape.pendown()
    shape.color(color)

    if fill:
        shape.begin_fill()
    
    for i in range(2):
        shape.forward(dx)
        shape.left(90)
        shape.forward(dy)
        shape.left(90)

    if fill:
        shape.end_fill()


def draw_flag(shape, width, color_list):
    draw_rectangle(shape, color_list[0], 0, 0, width, 200)
    draw_rectangle(shape, color_list[1], width, 0, width, 200)
    draw_rectangle(shape, color_list[2], 2*width, 0, width, 200)
    draw_rectangle(shape, "black", 0, 0, 3*width, 200, fill=False)  


my_turtle = turtle.Turtle()
draw_flag(my_turtle, 100, ["blue","white","red"])
turtle.done()