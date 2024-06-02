import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
cars = CarManager()
scoreboard_text = Scoreboard()

game_is_on = True

i = 0
initial_speed = 5
level = 0
generation_value = 4

while game_is_on:
    time.sleep(0.1)
    if i % generation_value == 0:
        cars.create_cars()
    cars.move_s(initial_speed)
    scoreboard_text.game_level(level)

    for car in cars.all_cars:
        if car.distance(timmy.return_xcor()) < 20:
            scoreboard_text.game_over()
            game_is_on = False

    if timmy.return_ycor() > 280:
        timmy.go_to_origina()
        level += 1
        scoreboard_text.game_level(level)
        initial_speed += 2
        generation_value -= 1

    i += 1
    screen.onkeypress(fun=timmy.move_fd, key="w")
    screen.onkeypress(fun=timmy.move_bw, key="s")
    screen.listen()
    screen.update()

screen.exitonclick()
