import os
#import curses
action=['Up','Left','Down','Right','Spawn','Restart','Exit']
letter_code='WASDGEQwasdgrq'
action_dict=dict(zip(letter_code,action*2))
#letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
#i,j,tmp=0,0,'+'# move section backup value initial

def main():
	
	game_board=GameBoard()	
	def init():
		game_board.reset()
#		initcursor=game_board.move()
#		initcursor.init_cursor()
		return 'Game'
	def not_game(state):
		game_board.draw()
		action = get_user_action
		response=defaultdict(lambda:state)
		response['Restart']
		
	def game():

		game_board.draw()
		action =get_user_action()
		if action =='Init':
			return 'Init'
		elif action == 'Exit':
			return 'Exit'
#		
		if action != 'Spawn':
			try:
				if game_board.move(action):
					if game_board.Judge():
						return 'Win'
			except:
				print("Out of range right now,Try again please")
				action =get_user_action()
				if game_board.move(action):
					if game_board.Judge():
						return 'Win'
		else:
			game_board.spawn(action)
#			break
		return 'Game'
	
	state='Init'
	state_actions={'Init':init,
			'Win':lambda:not_game('Win'),
			'Game':game}
	
	while state !='Exit':
		state = state_actions[state]()


def get_user_action():
	#print("Move cursor please: ",end='')
	char = input("Move cursor please: ")
	while char not in action_dict:
		char=input("Wrong direction, again please: ")
	return action_dict[char]


class GameBoard(object):
	def __init__(self,blackp='X',whitep='O',counter=0):
		self.i=self.hor =8 
		self.j=self.ver =8
		self.blackp=blackp
		self.whitep=whitep
		self.counter=counter
		self.tmp='+'
	def boardinit(self):
		board=[['+' for row in range(17)]for col in range(17)]
		#set boarder
		for hor in range(17):
			board[0][hor]=board[16][hor]='-'
		for side in range(17):
			board[side][0]=board[side][16] = '|'
		self.board = board

	def draw(self):
		player1='* * * * * * 白方下棋 * * * * * *'
		player2='* * * * * * 黑方下棋 * * * * * *'
		help_string='(W)光标向上(S)光标向下(A)光标向左(D)光标向右'
		help_string2= '(G)下子(R)重新开始(Q)退出游戏'
		def draw_board(row):
			print (' '.join(self.board[row]))
		def draw_status():
			if self.counter%2 == 0:
				print(player2)
			else:
				print(player1)

			print("当前步数:   %d"%self.counter)
			print(help_string,'\n',help_string2)
		os.system('clear')
		for row in range(17):
			draw_board(row)
		draw_status()

	def move(self,direction):
		#global i,j,tmp
		#Move cursor
		def init_cursor(i,j,tmp):
			i,j=self.hor,self.ver   #record position
			tmp=self.board[self.hor][self.ver] #record content
			return i,j,tmp
	
		def move_cursor(direction):
			if direction == 'Left':
				self.ver-=1
			elif direction == 'Right':
				self.ver += 1
			elif direction == 'Up':
				self.hor -=1
			elif direction == 'Down':
				self.hor += 1
		def put_cursor():
			self.board[self.hor][self.ver]='@'
		def backup_cursor(i,j,tmp):
			self.board[i][j]=tmp
		move_cursor(direction)
		backup_cursor(self.i,self.j,self.tmp)
		self.i,self.j,self.tmp=init_cursor(self.i,self.j,self.tmp)
		put_cursor()
		
	def spawn(self,action):
		piece = self.blackp if self.counter%2 ==1 else self.whitep
		def spawn_piece(action,piece):
			if action == 'Spawn':
				self.board[self.hor][self.ver] = piece
				self.counter +=1
				self.tmp=piece
		spawn_piece(action,piece)
	def Judge(self):
		directions=[[(1,1),(-1,-1)],[(0,1),(0,-1)],[(1,0),(-1,0)],[(-1,1),(1,-1)]]
		for lines in directions:
			counter=0
			for eachway in lines:
				xd,yd =eachway
				for n in range(1,5):
					if self.board[self.hor][self.ver] == self.board[self.hor + xd*n][self.ver + xd*n]:
						counter +=1
					else:
						break
					if counter == 4:
						return True
		return False

	def reset(self):
		self.boardinit()
		































main()
