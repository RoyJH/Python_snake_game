from turtle import Turtle, Screen
from snake import Snake
import time
# f_xy = []
# for num in range(-280, 281):
#     if num % 20 == 0:
#         f_xy.append(num)
body = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
jake = Snake()
jake.create_snake()
screen.update()
game_is_running = True

screen.listen()
screen.onkey(fun=jake.up, key="Up")
screen.onkey(fun=jake.down, key="Down")
screen.onkey(fun=jake.left, key="Left")
screen.onkey(fun=jake.right, key="Right")
while game_is_running:
    screen.update()
    jake.move()
    time.sleep(0.1)
screen.exitonclick()
