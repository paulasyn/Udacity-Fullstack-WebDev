import turtle

def draw():
     # create brad and draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.shapesize(outline=10)
    brad.color("yellow")
    brad.speed(15)
    for i in range(1,30):
        draw_square(20, brad)
        brad.right(10)

def draw_square(end, some_turtle):
    # create some_turtle and draw square
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.shape("arrow")
    some_turtle.color("blue")
    some_turtle.circle(100) 


window = turtle.Screen()
window.bgcolor("red")
draw()
window.exitonclick()