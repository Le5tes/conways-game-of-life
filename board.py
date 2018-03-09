from cell import Cell

class Board:

	def __init__(self,size, cell_class = Cell):
		self.cells = [[cell_class() for _ in range(size)] for _ in range(size)]
		self.size = size
		for x in range(size):
			for y in range(size):
				# print(str(self.cells[x][y]))
				self.cells[x][y].set_surrounders(self.__get_surrounders(x,y,size))

	def update(self):
		for row_of_cells in self.cells:
			for cell in row_of_cells:
				cell.prep()
			for cell in row_of_cells:
				cell.update()

	def toggle(self, pos):
		self.cells[pos.x][pos.y].toggle()

	def __get_surrounders(self,x,y,size):
		return [self.cells[p][q] 
				for p in range(x-1, x+2)
				for q in range(y-1, y+2)
				if p >= 0 and q >= 0 and p < size and q < size and (p != x or q!= y)]
