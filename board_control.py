from graphics import Rectangle
from xy import XY

class BoardControl:
	def __init__(self,board, position = XY(0,0), scale = 5, image_class = Rectangle):
		self.board = board
		self.image_class= image_class
		self.position = position
		self.scale = scale

	def draw(self, window):
		# for i, row in enumerate(self.board.cells):
			# for j, cell in enumerate(row):
		print('start')
		for i in range(self.board.size):
			for j in range(self.board.size):
				position = XY(self.position.x+ i * self.scale, self.position.y + j * self.scale)
				bounds = XY(self.position.x+ (i + 1) * self.scale, self.position.y + (j+ 1) * self.scale)
				box = self.image_class(position, bounds)
				box.draw(window)
		print('finish')
