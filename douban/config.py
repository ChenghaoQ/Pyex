from threading import Thread
import cPickle as pickle
import ConfigParser
import logging
import time
import os 


from doubanfm.API.login import request_token
from doubanfm.check import is_latest, update_package, is_mplayer
from doubanfm.exceptions import ConfigError

is_mplayer()#check first

logger = logging.getLogger('doubanfm')

THEME = ['default','larapaste','monokai','tomorrow']
PATH_CONFIG = os.path.expanduser('~/.doubanfm_config') ###
PATH_HISTORY = os.path.expanduser('~/.doubanfm_history')
PATH_TOKEN = os.path.expanduser('~/.doubanfm_token')
CONFIG = '''
[key]
UP = k
DOWN = j
TOP = g
BOTTOM = G
OPENURL = w
RATE = r
NEXT = n
BYE = b
QUIT = q
PAUSE = p
LOOP = l
MUTE = m
LRC = o
HELP = h
HIGH = i
'''
KEYS = {
	'UP':'k',
	'DOWN':'j',
	'TOP':'g',
	'BOTTOM':'G',
	'OPENURL':'w',
	'RATE':'r',
	'NEXT':'n',
	'BYE':'b',
	'QUIT':'q',
	'PAUSE':'p',
	'LOOP':'l',
	'MUTE':'m',
	'LRC':'o',
	'HELP':'h',
	'HIGH':'i'
	}

class Config(object):
	"""
	Offer the default value
	"""
	def __init__(self):
		self.volume = 50 
		self.channel = 0
		self.theme_id = 0
		self.user_name = ''
		self.netease = False #whether using netease320k
		self.run_times = 0 # log in times
		self.last_time = time.time() #current time
		self.total_time = 0#time in total
		self.liked = 0 # the song with ❤
		self.banned = 0 # the song never play again
		self.played = 0 # song played in total
		self.is_latest = True

		self.login_data = self.get_login_data()
	def output(args):#what is this used for 
		def _deco(func):
			def _func(self):
				print('\033[31m❤\033[0m ' +args)
				tmp = func(self)
				print('[\033[32m OK \033[0m]')
				return tmp
			return _func
		return _deco  #how to use closure,why we use that

	def get_login_data(self):
	#offers the login certification with default settings
	
	if os.path.exist(PATH_TOKEN):
		#use the token saved last time
		with open(PATH_TOKEN,'r') as f: #python3 may need binary mode
			login_data = pickle.load(f)
		if 'cookies' not in login_data:
			login_data = request_token()
	else:
		#didn't log in yet
		login_data = request_token()
	############
	self.get_default_set(login_data)
	self.get_user_states(login_data)
	self.get_is_latest_version(login_data)

	Thread(target = self.check_version).start()
	
	return login_data

	def check_version(self):
		self.is_latest = is_lateset('douban.fm')

	def get_is_latest_version(self,login_data):
		self.is_latest = is_latest('douban.fm')
		if not self.is_latest:
			if_update = input('seems to be a new version available,wanna have a try?[Y/N]:')
			if if_update.lower() == 'y':
				update_package('douban.fm')
				with open(PATH_TOKEN,'w') as f: #binary again?
					login_data['is_latest'] = True
					pickle.dump(login_data,f)
				print('Please restart douban.fm(sudoer privilage may need')
				os.exit(0)

	def get_default_set(self,login_data):
		"""
		record the status before quit
		"""
		self.cookies = login_data.get('cookies','')
		self.user_name = login_data.get('user_name','')
		print('\033[31m♥\033[0m Get local token - username: \033[33m%s \033[0m' %[login_data['user_name']
		self.channel = login_data.get('channel',0)
		print('\033[31m♥\033[0m Get channel [\033[32m OK \033[0m]')
		self.volume = login_data.get('volume',50)
		print('\033[31m♥\033[0m Get volume [\033[32m OK \033[0m]')
		self.them_id = login_data.get('netease',False)
		self.keys = self.get_keys()

	def get_user_states(self,login_data):
	# stat of user info
	self.run_times = login_data.get('run_times',0)
	self.total_time = login_data.get('total_time',0)

	@output('Get keys') #OMG how to use decorator
	def get_keys(self):
		'''
		get the settings and check if it was modified
		'''
		if not os.path.exists(PATH_CONFIG):
			with open(PATH_CONFIG,'w') as F: #binary again?
				F.write(CONFIG)
		else:
			config = ConfigParser.ConfigParser()
			with open(PATH_CONFIG,'r') as cfgfile:
				config.readfp(cfgfile) # what does readfp do
				options = config.options('key')
				for option in options:
					option = option.upper()
					if option in KEYS:
						KEYS[option] = config.get('key',option)
		return KEYS
	@property #Decorator again
	def history(self):#history is what
		try:
			with open(PATH_HISTORY,'r')as f:
				history = pickle.load(f)
		except IOError:
			history = []
		return history
	def save_config(self,volume,channel,theme,netease) #?????
		'''
		save the history and login_data
		'''
		self.login_data['cookies']=self.cokkies
		self.login_data['volume'] = volume
		self.login_data['channel'] = channel
		self.login_data['theme_id'] = theme
		self.login_data['netease'] = netease
		self.login_data['run_times'] = self.run_times + 1
		self.login_data['last_time'] = self.total_time + tome.time() - self.last_time
		self.login_data['is_lastest'] = self.is_latest
		with open(PATH_TOKEN,'wb') as f:#pickle need binary in python3
			pickle.dump(self.login_data,f)
		#with open(PATH_HISTORY,'wb') as f:
		#	pickle.dump(history,f)


db_config = config()
