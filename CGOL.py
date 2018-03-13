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
step_button = Button(Point(80,10), Point(50,20), 'Next..', board_control.update)
step_button.draw(window)

def main_loop():
	while window.closed == False:
		board_control.draw(window)
		window.update()
		mouseclick =  window.getMouse()
		close_button.click(mouseclick)
		step_button.click(mouseclick)
		board_control.click(mouseclick)

main_loop()