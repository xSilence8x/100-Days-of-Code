from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

my_screen = Screen()
my_screen.setup(height=600, width=800)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()


my_screen.listen()
my_screen.onkey(right_paddle.go_up, "Up")
my_screen.onkey(right_paddle.go_down, "Down")
my_screen.onkey(left_paddle.go_up, "w")
my_screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    my_screen.update()


my_screen.exitonclick()
