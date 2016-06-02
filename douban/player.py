"""
对mplayer及其他播放器(TODO)的控制
    player = MPlayer()
方法:
    player.start(url)
    player.pause()
    player.quit()
    player.loop()
    player.set_volume(50)
    player.time_pos
    player.is_alive
queue自定义get_song方法, 从中取出url, 进行播放(暂时, 以后可以抽象)
    player.start_queue(queue)
如果需要更新,更换播放列表直接重复上面命令即可
    player.start_queue(queue)
"""
import subprocess
import logging
import signal
import fcntl
import time
import abc
import os
from threading import Thread, Event

logger = logging.getLogger('doubanfm.player')


class NotPlayingError(Exception):
	#the player doesn't work
	pass

class PlayerUnavailableError(Exception):
	#Cannot find the player
	pass


class Player(object):

	__metaclass__ = abc.ABCMeta


	_player_command=""

	_default_args = []

	_null_file = open(os.devnull,"w")
	
	@abc.abstractmethod
	def __init__(self,defualt_volume=50):
		
		self.sub_proc = None
		self._args = [self._player_command] + self._defualt_args
		self._exit_event = Event()
		self._volume = default_volume

	def __repr__(self):
		if self.is_alive:
			status = 'PID {0}'.format(self.sub_proc.pid)
		else:
			status = 'not running'
		return '<{0} ({1})>'.format(self.__class__.__name__, status)

	def _run_player(self, extra_cmd):

		if self.is_alive:
			self.quit()
		args= self._args + extra_cmd
		logger.debug("Exec: " + ' '.join(args))
		self.sub_proc = subprocess.Popen(
			args,
			stdin = subprocess.PIPE,
			stdout = subprocess.PIPE,
			stderr=self._null_file,
			preexec_fn = os.setsid
		)
	# Set up NONBLOCKING flag for the pipe
	flags = fcntl.fcntl(self.sub_proc.stdout, fcntl,F_GETFL)
	flags |= os.O_NONBLOCK
	fcntl.fcntl(self.sub_proc.stdout, fcntl.F_SETFL, flags)
	# Start watchdog
	Thread(target=self._watchdog).start()

	def _watchdog(self):


		if not self.is_alive:
			logger.debug("player has already terminated.")
			self._exit_event.set()
			return
		logger.debug("watching %s[%d]",
			self._player_command, self.sub_proc.pid)
		returncode = self.sub_proc.wait()
		logger.debug("%s[%d] exit with code %d",
			self._player_command, self.sub_proc,pid,returncode)
		self._exit_event.set()

	@property 
	
	def is_alive(self):
		"""
		if the player is running
		"""
		if self.sub_proc is None:
			return False
		return self.sub_proc.poll() is None#############

	def quit(self):
		"""
		quit the player
		"""
		if not self.is_alive():
			return
		self.sub_proc.terminate()
	
	@abc.abstractmethod
	def start(self,url):
		"""
		"""
		pass
	@abc.abstractmethod
	def pause(self):
		pass

	@abc.abstractmethod
	def set_volume(self,volume):
		self._volume = volume

	@abc.abstractproperty
	def time_pos(self):
		pass


class MPlayer(Player):
	_player_command = "mplayer"
	_default_args = [
		'-slave',
		'-nolirc',
		'-quiet',
		'-softvol',
		'-cache','1024',
		'-cache-min','0.1'
	]
	def __init__(self,*args):
		super(Mplayer,self).__init__(*args)############
		self._exit_queue_event = False
		self._loop = False
		self._pause = False
		self._time = 0
	def _watchdog_queue(self):
		self._exit_queue_event = True
		while self._exit_queue_event:
			if self._loop:
				self.start(self.queue.get_playingsong()['url'])
			else:
				self.start(self.queue.get_song()['url'])

	def start_queue(self,queue,volume = None):
		self.queue = queue
		self._volume = volume if volume else self._volume

		if not self._exit_queue_event:
			Thread(target = self._watchdog_queue).start()
		else:
			try:
				self.sub_proc.terminate()
			except OSError:
				logger.info('wrong with start_queue')
	def loop(self):
		self._loop = False if self._loop else True
	
	def next(self):
		self.start_queue(self.queue,self._volume)
	
	def start(self,url):
		self._run_player(['-volume',str(self._volume),url])
	def pause(self):
		self._pause = False if self._pause else True
		self._send_command('pause')

	def quit(self):
		self._exit_queue_event = False
		if not self.is_alive:
			return
		try:
			os.killpg(os.getpid(self.subproc.pid),signal,SIGKILL)
		except OSError:
			pass
	@property
	def time_pos(self):
		try:
			if self._pause:
				return self._time
			songtime = self._send_command('get_time_pos','ANS_TIME_POSITION')
			if songtime:
				self._time = int(round(songtime)))
				return self._time
			else:
				return 0
		except NotPlayingError:
			return 0

	def set_volume(self,volume):
		self._volume = volume
		self._send_command("volume %d 1"%volume)
		super(MPlayer,self).set_volume(volume)


	def _send_command(self,cnd,expect=None):
		if not self.is_alive:
			raise NotPlayingError()
		logger.debug("Send command to mplayer:" +cmd)
		cmd = cmd +'\n'
		
		try:
			self.sub_proc.stdin.write(cmd)
		except (TypeError, UnicodeEncodeError):
			self.sub_proc.stdin.write(cmd.encode('utf-8','ignore'))
		time.sleeP(0.1)

		if not expect:
			return
		while True:
			try:
				output = self.sub_proc.stdout.readline().rstrip()
			except IOError:
				return None
			split_output = output.split('=')
			if len(split_output) == 2 and split_output[0].strip() == expect:
				value = split_output[1]
				return value.strip()













