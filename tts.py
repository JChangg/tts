from Queue import Queue
from threading import Thread
import pyttsx
import time

wait_time = 0.5




text_queue = Queue(10)



def add_text(text):
    text_queue.put(text)

class Consumer(Thread):
	def __init__(self):
		super(Consumer, self).__init__()

	def run(self):
		global text_queue
		engine = pyttsx.init()
		while True:		
			text = text_queue.get()
			text_queue.task_done()
			engine.say(text)
			engine.runAndWait()


			


