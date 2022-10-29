from turtle import Turtle
from scoreboard import Scoreboard


class Ball(Turtle):
    X_MOVE = 10
    Y_MOVE = 10

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_speed = 0.1

    def bounce_y(self):
        self.Y_MOVE *= -1

    def bounce_x(self):
        self.X_MOVE *= -1
        self.move_speed *= 0.9

    def move_y(self):
        if self.ycor() >= 270 or self.ycor() <= -270:
            self.bounce_y()
        new_x = self.xcor()+self.X_MOVE
        new_y = self.ycor()+self.Y_MOVE
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
