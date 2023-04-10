from turtle import Turtle, Screen

my_screen = Screen()
my_turtle = Turtle()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def move_left():
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)


def move_right():
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)


def clear_all():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=move_left)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="c", fun=clear_all)

my_screen.exitonclick()
