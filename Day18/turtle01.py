from turtle import Turtle, Screen
from random import randint


my_screen = Screen()
my_screen.colormode(255)

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.pensize(10)


def randomColorSelector():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return r, g, b


def drawGeometry(corners):
    r, g, b = randomColorSelector()
    my_turtle.pencolor(r, g, b)
    degree = 360 / corners
    for _ in range(corners):
        my_turtle.forward(100)
        my_turtle.right(degree)


for number in range(3, 9):
    drawGeometry(number)


my_screen.exitonclick()
