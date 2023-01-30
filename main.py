from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def flash():
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
while game_is_running:
    screen.update()
    jake.move()
    time.sleep(0.1)
    score.keep_score()
    if jake.head.distance(food) < 15:
        food.move_food()
        jake.grow_snake()
        score.add_point()
        screen.update()
    game_is_running = jake.check_snake()
flash()
screen.exitonclick()
