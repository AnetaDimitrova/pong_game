from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()

        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.goto(position)
        self.write(f"{self.r_score}", font=("Courier", 40, "bold"))
        self.write(f"{self.l_score}", font=("Courier", 40, "bold"))
        self.hideturtle()



    def right_score(self):
        self.clear()
        self.r_score += 1
        self.write(f"{self.r_score}", font=("Courier", 40, "bold"))





    def left_score(self):

        self.clear()
        self.l_score += 1
        self.write(f"{self.l_score}", font=("Courier", 40, "bold"))






