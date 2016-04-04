import curses
form random import randrange,choice
from collections import defaultdict  #what is defaultdict
#主逻辑

#用户行为
	actions=['Up','Left','Down','Right','Restart','Exit']#define six user actions
	letter_codes=[ord(ch) for ch in 'WASDRQwasdrq'] #ord以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常
	action_dict=dict(zip(letter_code,action*2)) #将用户行为和键入的字母对应起来，大小写各对应一次，所以action *2
	
#状态机，处理游戏主逻辑常用技术，将游戏状态分块
def main(stdscr):
	def init():
	#重置游戏棋盘
	game_field.reset()
	return 'Game'
	
	def not_game(state):
	#画出 Gameover 或者 Win 的界面
	#读取用户输入得到的action,判断是重启游戏还是结束程序
	responses = defaultdict(lambda:state)#m默认是当前状态，没有行为就会在当前界面循环
	responses['Restart'],responses['Exit']='Init','Exit'#对应不同的行为到不同的状态
	return response[action]
	
	def game()；
	#画出当前棋盘状态
	#读取用户输入的得到action
	if action =='Restart':
		return 'Init'
	elif action== 'Exit':
		return 'Exit'
	#if 成功移动了一步
		if 游戏胜利了：
			return 'Win'
		if 游戏失败了：
			return 'Gameover'
		return 'Game'  #等价于重复调用自身，等于while true

	state_actions={
		'Init':init,
		'Win':lambda:not_game('Win')
		'Gameover':lambda:not_game('Gameover') #为什么这里要加lambda
		'Game':game
	}

	state='Init'

	#状态机循环
	while state != 'Exit'
		state = state_action[state]()


	
#用户输入处理
#阻塞+循环，直到获得用户有效输入才返回对应行文
def get_user_action(keyboard):
	char="N"
	while char not in actions_dict:
		char=keyboard.getch()
	return actions_dict[char]

#矩阵转置与矩阵逆转
#加入这两个操作可以大大减少代码量，感受一下
#矩阵转置
def transpose(field):
	return [list(row) for row in zip(*field)]


