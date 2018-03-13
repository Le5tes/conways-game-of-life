import thread
import time

class Timer:
	def __init__(self, time_period,function):
		self.function = function
		self.time_period = time_period
		self.running = False

	def start(self):
		self.running = True
		self.thread = thread.start_new_thread(self.function_loop,())
		# self.thread.start()

	def stop(self):
		self.running = False

	def function_loop(self):
		while self.running:
			time.sleep(self.time_period)
			self.function()


