class Cell:
	is_alive = False
	def __init__(self,surrounders):
		self.__surrounders = surrounders

	def prep(self):
		surrounders_alive = [cell.is_alive for cell in self.__surrounders].count(True)

		if self.is_alive == False and  surrounders_alive == 3:
			self.__next = True

	def update(self):
		self.is_alive = self.__next
