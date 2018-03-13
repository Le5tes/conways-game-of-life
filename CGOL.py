from lib import window
win = window.CGOLWindow(1000, 800, 100)
win.draw()

def main_loop():
	while win.closed() == False:

		win.update()
		mouseclick =  win.getMouse()
		win.click(mouseclick)

main_loop()