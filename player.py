from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        super().__init__()
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.left(90)

    def move_fd(self):
        self.turtle.fd(MOVE_DISTANCE)

    def move_bw(self):
        self.turtle.backward(MOVE_DISTANCE)

    def return_xcor(self):
        return self.turtle.pos()

    def return_ycor(self):
        return self.turtle.ycor()

    def go_to_origina(self):
        self.turtle.goto(STARTING_POSITION)
