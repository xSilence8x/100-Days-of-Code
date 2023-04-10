from turtle import Turtle, Screen
from random import randint

race_is_on = False
colors = ["yellow", "orange", "red", "purple", "blue", "green"]

my_screen = Screen()
my_screen.setup(width=500, height=400)


def draw_lines(x, y):
    a_turtle = Turtle("arrow")
    a_turtle.penup()
    a_turtle.setpos(x, y)
    a_turtle.pendown()
    a_turtle.right(90)
    a_turtle.forward(300)

draw_lines(-200, 150)
draw_lines(200, 150)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []

i = 0
for color in colors:
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(color)
    my_turtle.setpos(x=-200, y=-100 + i)
    i += 30
    turtles.append(my_turtle)

if user_bet:
    race_is_on = True  

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 200:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color ==  user_bet:
                print(f"You have won! The {winning_color} is the winner!")
            else:
                print(f"You have lost! The {winning_color} is the winner!")
        speed = randint(0, 10)
        turtle.forward(speed)




my_screen.exitonclick()
