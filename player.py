from turtle import Turtle
STARTING_POSITION = (0, -270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('blue')
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move_fd(self):
        self.forward(10)

    def move_bk(self):
        self.backward(10)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
