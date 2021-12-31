from turtle import Turtle
import random

COLORS = ['red', 'yellow', 'green', 'purple', 'orange', 'gray', 'brown']


class Cars:
    def __init__(self):
        self.all_cars = []
        self.move_distance = 10
        self.create_cars()

    def create_cars(self):
        reduce_cars = random.randint(1, 6)
        if reduce_cars == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-280, 280)
            new_car.goto(350, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_speed_cars(self):
        self.move_distance += 5







