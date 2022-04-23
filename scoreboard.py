from turtle import Turtle

FONT = ("Sans Serif", 20, "bold")
START = (-250, 250)

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.color = "Red"
		self.current_level = 1
		self.reset_score()


	def reset_score(self):
		self.clear()
		self.goto(START)
		self.current_level = 1
		self.write("Level: {}".format(self.current_level), align="left", font=FONT)


	def increase_level(self):
		self.clear()
		self.current_level += 1
		self.write("Level: {}".format(self.current_level), align="left", font=FONT)


	def game_over(self):
		self.clear()
		self.goto(0,0)
		self.write("GAME OVER", align="center", font=FONT)
		




		

		


		


