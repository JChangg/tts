import Queue, pygame, os

from gtts import gTTS
from threading import Thread

DIR = os.path.join(os.path.dirname(__file__), 'audio_cache')

class TTSEngine:
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





