class Button:
	def __init__(self, position, size, text, function):
		self.size = size
		self.position = position
		self.text = text
		self.function = function

	def click(self, position):
		if self.__within_bounds(position):
			self.function()

	def __within_bounds(self, position):
		return position.x > self.position.x and position.y > self.position.y \
			   and position.x < self.position.x + self.size.x and position.y < self.position.y + self.size.y
