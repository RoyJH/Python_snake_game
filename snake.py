from turtle import Turtle, Screen

    snake = Turtle("square")
    snake.color("white")

def move_up(snake):
    snake.setheading(90)
    snake.forward(1)
def move_down(snake):
    snake.setheading(270)
    snake.forward(1)
def move_left(snake):
    snake.setheading(180)
    snake.forward(1)
def move_right(snake):
    snake.setheading(0)
    snake.forward(1)
