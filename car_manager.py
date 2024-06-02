from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):

        self.all_cars = []

    def create_cars(self):
        self.cars = Turtle()
        self.cars.shape("square")
        self.cars.color(COLORS[random.randint(0, 5)])
        self.cars.penup()
        self.cars.left(180)
        self.cars.speed(10)
        self.cars.shapesize(stretch_len=2)
        self.cars.goto(280, random.randint(-200, 280))

        self.all_cars.append(self.cars)

    def move_s(self, speed):

        for self.cars in self.all_cars:

            self.cars.fd(speed)

    def return_xcor_car(self):
        return self.cars.pos()
