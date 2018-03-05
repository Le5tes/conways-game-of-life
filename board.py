from cell import Cell

class Board:

	def __init__(self,size):
		self.cells = [Cell([]) for _ in range(size)]

	def update(self):
		for cell in self.cells:
			cell.prep()
		for cell in self.cells:
			cell.update()