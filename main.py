from turtle import Turtle, Screen
import random
import time

f_xy = []
for num in range(-280, 281):
    if num % 20 == 0:
        f_xy.append(num)


def make_snake():
    head = Turtle("square")
    head.color("white")
    head.penup()
    head.setpos(x=20, y=0)
    head.speed("fastest")
    body.append(head)
    new = add_segment(head)
    new.setpos(x=0, y=0)
    new = add_segment(new)
    new.setpos(x=-20, y=0)
    screen.update()
    return head


def move_up():
    start = head.pos()
    head.setheading(90)
    direction = head.heading()
    screen.update()
    # head.forward(20)
    move_body()


def move_down():
    start = head.pos()
    head.setheading(270)
    direction = head.heading()
    screen.update()
    # head.forward(20)
    move_body()


def move_left():
    start = head.pos()
    head.setheading(180)
    direction = head.heading()
    screen.update()
    # head.forward(20)
    move_body()


def move_right():
    start = head.pos()
    head.setheading(0)
    direction = head.heading()
    screen.update()
    # head.forward(20)
    move_body()


def add_segment(last):
    new = Turtle("square")
    new.speed("fastest")
    new.hideturtle()
    new.penup()
    new.setpos(last.pos())
    new.showturtle()
    new.color("white")
    body.append(new)
    return new


def spawn_fruit():
    fruit = Turtle("circle")
    fruit.penup()
    fruit.speed("fastest")
    fruit.setpos(x=random.choice(f_xy), y=random.choice(f_xy))
    fruit.color("red")
    return fruit


def move_body():
    check_snake()
    current = 0
    # head.forward(20)
    # start = head.pos()
    screen.update()
    for segment in body:
        if current > 0:
            end = body[current].pos()
            body[current].setpos(start)
            start = end
        elif current == 0:
            check_snake()
            start = head.pos()
            head.forward(20)
            check_snake()
        # screen.update()
        time.sleep(0.1)
        if current <= len(body):
            current += 1


def check_snake():
    for segment in body:
        if segment.pos() == head.pos() and segment != body[0]:
            print("You ate yourself...")
            global game_is_running
            game_is_running = False
        elif segment.xcor() < -300 or segment.xcor() > 300:
            print("You've gone out of bounds....")
            # global game_is_running
            game_is_running = False
        if segment.pos() == fruit.pos():
            add_segment(body[len(body)-1])
            fruit.setpos(x=random.choice(f_xy), y=random.choice(f_xy))


body = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
head = make_snake()
fruit = spawn_fruit()
screen.update()
game_is_running = True

screen.listen()
screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")
screen.onkey(fun=move_left, key="Left")
screen.onkey(fun=move_right, key="Right")
while game_is_running:
    screen.update()
    for segment in body:
        move_body()
    screen.update()
screen.exitonclick()
