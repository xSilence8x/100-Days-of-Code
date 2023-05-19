from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.title("My Snake game")
screen.bgcolor("black")
screen.tracer(0) # turns off animation of Turtle object

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

    
game_is_on = True

while game_is_on:
    # screen is updating every 0.1 s -> snake's move is smooth
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

