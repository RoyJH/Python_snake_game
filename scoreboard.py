from turtle import Turtle


def set_high_score(new_high):
    with open("stored_high.txt", mode="w") as file:
        high_score = file.write(new_high)
        return high_score

def get_high_score():
    with open("stored_high.txt") as file:
        high_score = file.read()
        return high_score


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(get_high_score())
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

    def keep_score(self):
        score = self.score
        high_score = self.high_score
        self.clear()
        self.sety(270)
        self.setx(-100)
        self.write(arg=f"Score: {score}", align="center", font=("Centaur", 16, "normal"))
        self.setx(100)
        self.write(arg=f"High Score: {high_score}", align="center", font=("Centaur", 16, "normal"))

    def add_point(self):
        self.score += 1
        self.keep_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_high = str(self.high_score)
            set_high_score(new_high)
        self.score = 0

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=("Centaur", 14, "bold"))

