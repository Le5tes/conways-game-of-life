from graphics import *
from board import Board

CELL_SIZE = 10
MARGIN_SIZE = 20
window = GraphWin("Conway's Game of Life!", 1000, 800)

def main_loop():
	while window.closed == False:
		print window.getMouse()


main_loop()