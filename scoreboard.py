from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        super().__init__()
        self.score = 0
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

    def keep_score(self):
        score = self.score
        self.sety(280)
        self.write(arg=f"Score: {score}", align="center", font=("Centaur", 14, "normal"))

    def add_point(self):
        self.clear()
        self.score += 1
        self.keep_score()

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=("Centaur", 14, "bold"))

