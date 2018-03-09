class XY:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	#so it can be used as a point:
	def clone(self):
		return self

	#equality:
	def __eq__(self,other):
		return self.x == other.x and self.y == other.y