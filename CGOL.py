from window import CGOLWindow
# from board import Board


# CELL_SIZE = 10
# MARGIN_SIZE = 20
window = CGOLWindow(1000, 800, 100)
# close_button = Button(Point(10,10), Point(50,20), 'Close', window.close)
# close_button.draw(window)
# board_control = BoardControl(Board(100),Point(30,30),5)
# step_button = Button(Point(80,10), Point(50,20), 'Next..', board_control.update)
# step_button.draw(window)
window.draw()
def main_loop():
	while window.closed() == False:
		# board_control.draw(window)
		window.update()
		mouseclick =  window.getMouse()
		window.click(mouseclick)
		# close_button.click(mouseclick)
		# step_button.click(mouseclick)
		# board_control.click(mouseclick)

main_loop()