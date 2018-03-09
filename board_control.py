from graphics import Rectangle
from xy import XY

class BoardControl:
	def __init__(self,board, position = XY(0,0), scale = 5, image_class = Rectangle):
		self.board = board
		self.image_class= image_class
		self.position = position
		self.scale = scale
		self.bounds = XY(position.x + scale * board.size, position.y + scale * board.size)

	def draw(self, window):
		# for i, row in enumerate(self.board.cells):
			# for j, cell in enumerate(row):
		print('start')
		for i in range(self.board.size):
			for j in range(self.board.size):
				position = XY(self.position.x+ i * self.scale, self.position.y + j * self.scale)
				bounds = XY(self.position.x+ (i + 1) * self.scale, self.position.y + (j+ 1) * self.scale)
				box = self.image_class(position, bounds)
				box.setFill('red' if self.board.cells[i][j].is_alive == True else 'grey')
				box.draw(window)
		print('finish')

	def update(self):
		self.board.update()

	def click(self,pos):
		if self._within_bounds(pos):
			self.board.toggle(XY(int((pos.x-self.position.x)//self.scale),int((pos.y-self.position.y)//self.scale)))

	def _within_bounds(self,pos):
		return pos.x > self.position.x and pos.y > self.position.y \
				and pos.x < self.bounds.x and pos.y < self.bounds.y