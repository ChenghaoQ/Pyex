from threading import Thread
#import notification # desktop notification
import subprocess,logging,Queue,sys,os

from doubanfm import data,getch
from doubanfm.player import MPlayer
from doubanfm.controller.main_contriller import MainController
from doubanfm.controller.lrc_contrller import LrcController
from doubanfm.controller.help_controller import HelpController
from doubanfm.controller.manager_controller import ManagerController
from doubanfm.contrller.quit_controller import QuitController


reload(sys)
sys.setdefaultencoding('utf8')

loggin.basicConfig(
	format=" %(asctime)s - \
[%(process)d]%(filename)s:%(lineno)d - %(levelname)s: %(message)s",
	datefmt='%Y-%m-%d %H:%I:%S',
	filename=os.path.expanduser('~/.doubanfm.log'),
	level = logging.INFO
)

#set up our own logger
logger = logging.getLogger('doubanfm')
logger.setLevel(logging.INFO)




class Router(object):
	

	def __init__(self):
		self.player = MPlayer()
		self.data = data.Data()
		self.quit_quit= False #????
		self.current_controller = None
		#--------------------------------------------
		self.switch_queue = Queue.Queue(0) #??????
		self.key_queue = Queue.Queue(0) #???

		self.view_control_map ={
			'main': MainController(self.player,selfdata,self.key_queue),
			'lrc': LrcController(self.player,self.data,self.key_queue),
			'help': HelpController(self.player,self.data,self.key_queue),
			'manager': ManagerController(self.player,self.data,self.key_queue),
			'quit': QuitController(self.player,sele.data,self.key_queue)
		}

	#Switch the thread
		Thread(target=self,_watchdog_switch).start()
		Thread(target=self._watchdog_key).start()

	def _watchdog_switch(self):
		
		#init
		self.current_controller = self.view_control_map['main']
		self.current_controller.run(self.switch_queue)

		while not self.quit_quit:
			key = self.switch_queu.get()
			if key == 'quit_quit':
				self.quit_quit = True
			else:
				self.current_controller = self.view_control_map[key]
				sel.fcurrent_controller.run(self.switch_queue)

		self.quit()
		os._exit(0)

	def quit(self):

		self.data.save()
		subprocess.call('echo -e "\033[?25h";clear', shell = True)

	def _watchdog_key(self):
		# why not use the instant one
		while True:
			k = getch.getch()
			self.key_queue.put(k)
	

	#Then let's write the main

def main():
	router = Router() # initial the object
	from flask import Flask, request
	app = Flask(__name__)

	@app.route('/',methods=['POST'])
	def index():
		router.key_queue.put(request.form['ch'])
		return 'OK'
	app.run()

if __name__ == "__main__":
	main()










	
