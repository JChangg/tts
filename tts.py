import Queue
from threading import Thread

import pyttsx

wait_time = 0.5


class TextToSpeaker(Thread):
    def __init__(self):
        super(TextToSpeaker, self).__init__()
        self.queue = Queue.Queue(5)
        self.daemon = True

    def add_text(self, text):
        try:
            self.queue.put(text, timeout=1)
            return self.queue.qsize()
        except Queue.Full:
            return -1

    def run(self):
        engine = pyttsx.init()
        while True:
            text = self.queue.get()
            self.queue.task_done()
            engine.say(text)
            engine.runAndWait()
