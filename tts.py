import Queue
from threading import Thread
import pyttsx
import time

wait_time = 0.5

text_queue = Queue.Queue(5)



def add_text(text):
	try:
		text_queue.put(text, timeout=1)	
		return text_queue.qsize()
	except Queue.Full:
		return -1
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


			


