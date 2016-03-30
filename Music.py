import Queue
import os
from threading import Thread

import pygame

DIR = os.path.join(os.path.dirname(__file__), 'songs')


class MusicPlayer(Thread):
    def __init__(self, path_to_music=DIR):
        super(MusicPlayer, self).__init__()
        self.dir = path_to_music
        self.queue = Queue.Queue()
        self.current = None
        self.pause = False
        self.daemon = True
        pygame.mixer.init()
        pygame.init()

    def add_song(self, song_file, **kwargs):
        alias = kwargs.get('alias', song_file)

        song_info = {
            'local_name': os.path.join(self.dir, song_file),
            'alias': alias,
        }

        self.queue.put(song_info)

    def skip_song(self):
        pygame.mixer.music.stop()

    def pause_song(self):
        self.pause = True
        pygame.mixer.music.pause()

    def un_pause_song(self):
        pygame.mixer.music.unpause()
        self.pause = False


    def run(self):
        while True:
            song_info = self.queue.get()
            name = song_info['local_name']
            self.current = song_info['alias']
            pygame.mixer.music.load(name)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() or self.pause:
                pygame.time.Clock().tick(10)
