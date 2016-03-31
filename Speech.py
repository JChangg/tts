import pygame, os, Queue

from gtts import gTTS
from threading import Thread

DIR = os.path.join(os.path.dirname(__file__), 'audio_cache')

class TextToSpeech:
    def __init__(self):
        self.dir = DIR
        pygame.mixer.init()
        pygame.init()

    def speak(self, text):
        speech = gTTS(text=text, lang='en')
        filename = os.path.join(self.dir, 'tmp.mp3')
        speech.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

class QueryHandler(Thread):
    def __init__(self):
        super(QueryHandler, self).__init__()
        self.queue = Queue.Queue(5)
        self.daemon = True

    def add(self, text):
        try:
            self.queue.put(text, timeout=1)
            return self.queue.qsize()
        except Queue.Full:
            return -1

    def run(self):
        engine = TextToSpeech()
        while True:
            text = self.queue.get()
            self.queue.task_done()
            engine.speak(text)
