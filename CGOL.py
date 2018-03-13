from window import CGOLWindow

window = CGOLWindow(1000, 800, 100)
window.draw()

def main_loop():
	while window.closed() == False:

		window.update()
		mouseclick =  window.getMouse()
		window.click(mouseclick)

main_loop()