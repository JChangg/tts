import pygame
import os
import Queue
from threading import Thread, Condition


class MusicPlayer(Thread):
	def __init__(self, relative_path_to_dir=""):
		super(MusicPlayer, self).__init__()
		dir = os.path.dirname(__file__)
		self.dir = os.path.join(dir, relative_path_to_dir)
		self.queue = Queue.Queue()
		self.current = None
		self.paused = True
		pygame.mixer.init()
		pygame.init()
		
	def add_song(self, song_file, **kwargs):
		alias = kwargs.get('alias', song_file)
		remote_url = kwargs.get('remote_url', None)
		
		song_info = {
			'local_name': os.path.join(self.dir, song_file),
			'alias': alias,
			'remote_url': remote_url
		}
		self.queue.put(song_info)	
		return self.queue.qsize()

	def skip_song(self):
		pygame.mixer.music.stop()
		
	def pause_song(self):
		self.pause = True
		pygame.mixer.music.pause()

	def unpause_song(self):
		pygame.mixer.music.unpause()
		self.pause = False
	
	def run(self):
		while True:	
			song_info = self.queue.get()
			name = song_info['local_name']
			self.current = song_info['alias']
			pygame.mixer.music.load(name)
			pygame.mixer.music.play()

			while pygame.mixer.music.get_busy()or self.paused:				
				pygame.time.Clock().tick(10)



if True:#__name__ == '__main__':
	mp = MusicPlayer()
	mp.daemon = True
	mp.start()
	mp.add_song('Hello.wav')	
	mp.add_song('Hello.wav')
	mp.add_song('Hello.wav')
	mp.add_song('Hello.wav')


