from turtle import Turtle, Screen
import random

def make_snake():
    head = Turtle("square")
    head.color("white")
    head.penup()
    head.setpos(x=20, y=0)
    new = add_segment(head)
    new.setpos(x=0, y=0)
    body.append(new)
    new = add_segment(new)
    new.setpos(x=-20, y=0)
    body.append(new)
    return head


def move_up():
    current = head.pos()
    head.setheading(90)
    head.forward(20)
    move_body()


def move_down():
    current = head.pos()
    head.setheading(270)
    head.forward(20)
    move_body()


def move_left():
    current = head.pos()
    head.setheading(180)
    head.forward(20)
    move_body()


def move_right():
    current = head.pos()
    head.setheading(0)
    head.forward(20)
    move_body()


def add_segment(last):
    new = Turtle("square")
    new.color("white")
    new.penup()
    new.setpos(last.pos())
    body.append(new)
    return new


def spawn_fruit():
    pass

s
def move_body():
    current = 0
    start = head.pos()
    end = body[current].pos()
    body[current].setpos(start)
    current += 1
    segments = len(body)
    for segment in body:
        current = segment.pos()

        #last = segment.pos()


body = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
head = make_snake()

screen.listen()
screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")
screen.onkey(fun=move_left, key="Left")
screen.onkey(fun=move_right, key="Right")
screen.exitonclick()
