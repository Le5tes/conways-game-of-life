from graphics import *
from board import Board
from button import Button
from board_control import BoardControl

CELL_SIZE = 10
MARGIN_SIZE = 20
window = GraphWin("Conway's Game of Life!", 1000, 800, autoflush=False)
close_button = Button(Point(10,10), Point(50,20), 'Close', window.close)
close_button.draw(window)
board_control = BoardControl(Board(100),Point(30,30),5)
board_control.draw(window)
def main_loop():
	while window.closed == False:
		window.update()
		mouseclick =  window.getMouse()
		close_button.click(mouseclick)

main_loop()