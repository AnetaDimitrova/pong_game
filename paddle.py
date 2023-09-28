import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()


        self.penup()
        self.create_paddle(x, y)

        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("green")

    def create_paddle(self, x, y):
        self.setposition(x, y)




    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)



    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



