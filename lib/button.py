from graphics import *

class Button:
	def __init__(self, position, size, text, function, point_class = Point):
		self.size = size
		self.position = position
		self.text = text
		self.function = function
		self.bounds = point_class(self.position.x + self.size.x, self.position.y + self.size.y)

	def click(self, position):
		if self.__within_bounds(position):
			self.function()

	def __within_bounds(self, position):
		return position.x > self.position.x and position.y > self.position.y \
			   and position.x < self.bounds.x and position.y < self.bounds.y

	def draw(self,window):
		Rectangle(self.position, self.bounds).draw(window)
		Text(self.position, self.text).draw(window)
