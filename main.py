from turtle import Screen, Turtle
from car import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()

# create display
display = Screen()
display.bgcolor("white")
display.setup(width=600, height = 600)
display.title("Turtle Crossing")
display.tracer(0)

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

display.listen()
display.onkey(player.move_up, "Up")
display.onkey(player.move_down, "Down")
display.onkey(player.move_left, "Left")
display.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	display.update()
	car_manager.create_car()
	car_manager.move_cars()

	for car in car_manager.all_cars:
		if car.distance(player) < 20:
			scoreboard.game_over()
			game_is_on = False

	if player.is_finished() == True:
		player.reset_position()
		car_manager.level_up()
		scoreboard.increase_level()






display.exitonclick()