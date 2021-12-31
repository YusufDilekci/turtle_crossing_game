from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
OVER_ALIGNMENT = 'center'
OVER_FONT = ('Rockwell', 17, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.penup()
        self.goto(-300, 240)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'LEVEL: {self.level} ', False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f'GAME OVER', False, align=OVER_ALIGNMENT, font=OVER_FONT)

