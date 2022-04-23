from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 15
FINISH_Y_POSITION = 300

class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.color("black")
		self.left(90)
		self.penup()
		self.reset_position()
		self.level = 1

	def move_up(self):
		self.setheading(90)
		self.forward(MOVE_DISTANCE)

	def move_down(self):
		self.setheading(-90)
		self.forward(MOVE_DISTANCE)
	
	def move_left(self):
		self.setheading(180)
		self.forward(MOVE_DISTANCE)
	
	def move_right(self):
		self.setheading(0)
		self.forward(MOVE_DISTANCE)

	def reset_position(self):
		self.goto(STARTING_POSITION)

	def is_finished(self):
		if self.ycor() > FINISH_Y_POSITION:
			return True
		else:
			return False



