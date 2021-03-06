class Cell:

	def __init__(self):
		self.is_alive = False
		self.__next = False 
		self.changed = True

	def set_surrounders(self,surrounders):
		self.__surrounders = surrounders
		
	def prep(self):
		surrounders_alive = [cell.is_alive for cell in self.__surrounders].count(True)

		if self.is_alive == False and surrounders_alive == 3:
			self.__next = True
		elif self.is_alive and (surrounders_alive == 2 or surrounders_alive == 3):
			self.__next = True
		else:
			self.__next = False

	def update(self):
		self.changed = (True if self.is_alive != self.__next else False)
		self.is_alive = self.__next

	def toggle(self):
		self.is_alive = not self.is_alive
		self.changed = True


