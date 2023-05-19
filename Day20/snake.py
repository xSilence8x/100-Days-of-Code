from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # CONST
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake() # calls func to create a Snake
        self.head = self.snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(position)
            self.snake.append(snake_part)
        
    
    def move(self):
        # move 3rd segment to place of 2nd and 2nd to place of 1st,...
        for segment in range(len(self.snake) - 1, 0, -1): # start=2, stop=0, step=-1
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)


