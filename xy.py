class XY:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	#so it can be used as a point:
	def clone(self):
		return self