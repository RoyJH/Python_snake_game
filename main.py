from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def flash():
    score.game_over()
    for _ in range(0, 5):
        for segment in jake.segments:
            segment.hideturtle()
        screen.update()
        time.sleep(0.1)
        for segment in jake.segments:
            segment.showturtle()
        screen.update()
        time.sleep(0.1)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

jake = Snake()
score = Scoreboard()
food = Food()

screen.listen()
screen.onkey(fun=jake.up, key="Up")
screen.onkey(fun=jake.down, key="Down")
screen.onkey(fun=jake.left, key="Left")
screen.onkey(fun=jake.right, key="Right")
game_is_running = True
# reset_game = False
while game_is_running:
    screen.update()
    score.keep_score()
    jake.move()
    time.sleep(0.1)
    if jake.head.distance(food) < 15:
        food.move_food()
        jake.grow_snake()
        score.add_point()
        screen.update()
    reset_game = jake.check_snake()
    if reset_game:
        flash()
        time.sleep(1)
        score.reset_scoreboard()
        jake.snake_reset()
screen.exitonclick()
