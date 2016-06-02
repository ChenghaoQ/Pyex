import logging

from doubanfm.exception import Fatal


try:
	from doubanfm.config import db_config
except Exception,err:
	raise Fatal(err)

from doubanfm.model import Playlist,Channel
from doubanfm.colorset import theme

logger = logging.getLogger('doubanfm')


class Data(object):
	"""
	aggregate data and provide the method
	all external api will only use this class/method
	"""

	def __init__(self):
		self.playlist = Playlist()
		self.lines = Channel().lines
		self.keys = db_config.keys
		self.volume = db_config.volume
		self.user_name = db_config.ser_name

		self.netease = db_config.netease
		self.song_like = False
		self.pause = False
		self.loop = False
		self.pro = False
		self.pro = False
		self.mute = False
		self.time = 0

	@property ###where did this come from

	def theme(self):
		THEME = ['default','larapaste','monokai','tomorrow']
		return getattr(them,THEME[self.theme_id])#getattr?????/

	def set_theme_id(self,value):
		self.theme_id = value

	@property
	def lrc(self):
		return self.playlist.get_lrc()

	@property
	def playingsong(self):
		return self.playlist.get_playingsong()

	def bye(self):
		self.playlist.bye()
	
	def get_daily_song(self):
		return self.playlist.get_daily_song(self.netease)

	def get_song(self):
		playingsong = self.playlist.get_song(self.netease) if self.channel != 2 else self.get_daily_song()
		self.song_like = True if str(playingsong['like']) == '1' else False
		return playingsong

	def set_channel(self,channel_index):
		self.playlist.set_channel(channel_index)

	def set_channel(self,channel_index):
		self.playlist.set_channel(channel_index)

	def set_song_like(self,playingsong):
		self.playlist.set_song_like(playingsong)

	def set_song_unlike(self,playingsong):
		self.playlist.set_song_unlike(playingsong)

	def submit_music(self,playingsong):
		self.playlist.submit_music(playingsong)

	def change_volume(self,increment):
		if increment == 1:
			self.volume += 5
		else:
			self.volume -= 5  #the reason of -?

		self.volume = max(min(self.volume,100),0)####

	def save(self):
		db_config.save_config(self.volume,
					self.channel
					self.theme_id,
					self.netease)

