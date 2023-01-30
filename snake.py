from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
f_xy = []
for num in range(-280, 281):
    if num % 20 == 0:
        f_xy.append(num)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_bounds(self):
        for segment in self.segments:
            if segment.xcor() < -300 or segment.xcor() > 300 or segment.ycor() < -300 or segment.ycor() > 300:
                print("You've gone out of bounds....")
                game_is_running = False
                return game_is_running
            else:
                return True

    def grow_snake(self):
        position = self.segments[len(self.segments)-1].pos()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def check_self(self):
        for segment in self.segments:
            if segment.distance(self.head.pos()) < 2:
                if segment == self.head:
                    pass
                elif segment != self.head:
                    print("You ate yourself...")
                    game_is_running = False
                    return game_is_running
                else:
                    print("This shouldn't happen")

    def check_snake(self):
        myself = self.check_self()
        bounds = self.check_bounds()
        if myself is False or bounds is False:
            return False
        else:
            return True
