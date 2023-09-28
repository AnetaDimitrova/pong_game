from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.color("red")
        self.speed("slow")
        self.x_move=random.randint(3,8)
        self.y_move=random.randint(3,8)
        self.penup()

    def move_ball(self):
        y_cor = self.ycor()+self.y_move
        x_cor = self.xcor()+self.x_move


        self.goto(x_cor, y_cor)



    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move *= -1


    def reset_position(self):


        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()







