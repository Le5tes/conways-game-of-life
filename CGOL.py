from graphics import *
from board import Board
from button import Button

CELL_SIZE = 10
MARGIN_SIZE = 20
window = GraphWin("Conway's Game of Life!", 1000, 800)
close_button = Button(Point(10,10), Point(50,20), 'Close', window.close)
close_button.draw(window)
def main_loop():
	while window.closed == False:
		mouseclick =  window.getMouse()
		close_button.click(mouseclick)

main_loop()