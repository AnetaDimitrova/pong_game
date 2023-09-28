from turtle import Turtle
class Middle:
    def __init__(self):
        self.middle = Turtle()
        self.middle.penup()
        self.middle.setposition(0, 350)
        self.middle.setheading(270)
        self.middle.pencolor("green")
        self.create_midle(6, 8)

    def create_midle(self, space, x):
        print()

        for i in range(x):
            for j in range(x):
                self.middle.pendown()
                self.middle.forward(10)
                self.middle.penup()
                self.middle.forward(space)
                self.middle.penup()