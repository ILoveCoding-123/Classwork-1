import turtle

screen = turtle.Screen()
screen.bgcolor("white")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("black")
my_turtle.speed(3)

for i in range(4):
    my_turtle.forward(100)
my_turtle.right(90)

screen.exitonclick()