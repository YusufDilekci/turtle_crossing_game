import time
from turtle import Screen
from player import Player
from cars import Cars
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
cars = Cars()
score_board = ScoreBoard()


screen.listen()
screen.onkey(player.move_fd, key='Up')
screen.onkey(player.move_bk, key='Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    #Detect successful crossing
    if player.ycor() > 280:
        player.go_to_start()
        score_board.increase_level()
        cars.increase_speed_cars()

    #Detect collision between car and player
    for car in cars.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()