from turtle import Turtle
import random

COLORS = ["blue", "green", "red", "cyan", "pink", "orange", "purple", "yellow"]
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 15

		# 300 (y)
# -300 (x)		# 300 (x)	
		# -300 (y)

class CarManager:
	def __init__(self):
		self.all_cars = []
		self.car_speed = STARTING_MOVE_DIST

	def create_car(self):
		random_chance = random.randint(1,6)
		if random_chance == 1:
			new_car = Turtle("square")
			new_car.penup()
			new_car.shapesize(stretch_wid=1,stretch_len=2)
			new_car.color(random.choice(COLORS))
			y_pos = random.randrange(-280, 280, 1)
			new_car.goto(310, y_pos)
			self.all_cars.append(new_car)

	def move_cars(self):
		for car in self.all_cars: 
			car.backward(self.car_speed)

	def level_up(self): 
		self.car_speed += MOVE_INCREMENT




