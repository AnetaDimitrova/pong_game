import time
from turtle import Screen, Turtle
from paddle import Paddle
from middle import Middle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("yellow")
screen.tracer(0)



middle = Middle()
ball = Ball()
right_paddle = Paddle(-350, 0)
left_paddle = Paddle(350, 0)
right_paddle_score = Scoreboard((-50, 240))
left_paddle_score = Scoreboard((50, 240))





screen.listen()
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")


while True:
    screen.update()
    time.sleep(0.01)

    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()


    if ball.distance(right_paddle)< 50:
         right_paddle_score.right_score()
         ball.reset_position()


    if ball.distance(left_paddle)< 50:
        left_paddle_score.left_score()
        ball.reset_position()














    print(ball.position())
    print(ball.distance(left_paddle))









screen.exitonclick()
