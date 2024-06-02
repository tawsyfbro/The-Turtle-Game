from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.screen_text = Turtle()

    def game_over(self):
        self.screen_text.clear()
        self.screen_text.write("Game Over!", font=FONT)

    def game_level(self, level_value):
        self.screen_text.ht()
        self.screen_text.penup()
        self.screen_text.goto(-250, 250)
        self.screen_text.pendown()
        self.screen_text.clear()
        self.screen_text.write(f"Level {level_value}", font=FONT)
