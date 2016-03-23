from Queue import Queue
from threading import Thread
import pyttsx
import time

wait_time = 2

engine = pyttsx.init()
text_queue = Queue(10)


def add_text(text):
    text_queue.put(text)
    return len(text_queue)


class Consumer(Thread):
    def run(self):
        global text_queue
        while True:
            text = text_queue.get()
            text_queue.task_done()
            engine.say(text)
            engine.runAndWait()
            time.sleep(wait_time)


