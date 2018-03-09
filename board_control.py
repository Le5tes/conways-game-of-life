from graphics import Rectangle, Point

class BoardControl:
	def __init__(self,board,window, position = Point(0,0), scale = Point(5,5), image_class = Rectangle):
		self.board = board
		self.window = window
		self.image_class= image_class
		self.position = position
		self.scale = scale

	def draw(self):
		for row in self.board.cells:
			for cell in row:
				position = Point(0,0)
				bounds = Point(0,0)
				box = self.image_class(position, bounds)
				box.draw(self.window)
