from graphics import *
from button import Button
from board_control import BoardControl
from board import Board
from timer import Timer

class CGOLWindow:
	def __init__(self,sizex, sizey, boardsize, title="Conway's Game of Life!", graphwin_class=GraphWin, button_class = Button):
		print(title)
		self.window = graphwin_class(title, sizex, sizey, autoflush = False)
		self.board_control = BoardControl(Board(boardsize),Point(30,30),5)
		self.freq = 0.2
		self.__running = False
		self.buttons = [button_class(Point(10,10), Point(50,20), 'Close', self.window.close),
						button_class(Point(80,10), Point(50,20), 'Next..', self.board_control.update),
						button_class(Point(140,10),Point(50,20), 'Run', self.__timed_update_start_stop)]

	def click(self,mouseclick):
		for button in self.buttons:
			button.click(mouseclick)
		self.board_control.click(mouseclick)

	def draw(self):
		for button in self.buttons:
			button.draw(self.window)
		self.board_control.draw(self.window)

	def update(self):
		self.board_control.draw(self.window)
		self.window.update()

	def getMouse(self):
		return self.window.getMouse()

	def closed(self):
		return self.window.closed

	def __timed_update_start_stop(self):
		print('start timer')
		if not self.__running:
			self.__timer = Timer(self.freq,self.__on_tick)
			self.__timer.start()  
		else:
			self.__timer.stop()
		self.__running = not self.__running

	def __on_tick(self):
		self.board_control.update()
		self.update()

