import turtle

def draw_square():
    # create brad and draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.shapesize(outline=10)
    brad.color("yellow")
    brad.speed(3)
    
    count = 0
    while (count < 4):
        brad.forward(100)
        brad.right(90)
        count+=1

def draw_circle():
    # create angie and draw circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100) 

window = turtle.Screen()
window.bgcolor("red")
draw_square() 
draw_circle()
window.exitonclick()