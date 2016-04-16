import os
action=['Up','Left','Down','Right','Spawn','Restart','Exit']
#letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
letter_code='WASDGEQwasdgrq'
action_dict=dict(zip(letter_code,action*2))
i,j,tmp=0,0,'+'# move section backup value initial

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
#		while True:
#			if action != 'Spawn':
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
#			else:
#				game_board.spawn()
#				break
		return 'Game'
	
	state='Init'
	state_actions={'Init':init,
			'Win':lambda:not_game('Win'),
			'Game':game}
	
	while state !='Exit':
		state = state_actions[state]()


def get_user_action():
	char=input("Move cursor please: ")
	while char not in action_dict:
		char=input("Wrong direction, again please")
	return action_dict[char]


class GameBoard(object):
	def __init__(self,blackp='X',whitep='O'):
		self.hor =8 
		self.ver =8
		self.blackp=blackp
		self.whitep=whitep
		self.tmp=None
	def boardinit(self):
		board=[['+' for row in range(17)]for col in range(17)]
		#set boarder
		for hor in range(17):
			board[0][hor]=board[16][hor]='-'
		for side in range(17):
			board[side][0]=board[side][16] = '|'
		self.board = board

	def draw(self):
		player1='	White'
		player2='	Black'

	#	def draw_board(row):
	#		print (' '.join(self.board[row]))

		os.system('clear')
		for row in range(17):
	#		draw_board(row)
			print (' '.join(self.board[row]))
	def move(self,direction):
		global i,j,tmp
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
		backup_cursor(i,j,tmp)
		i,j,tmp=init_cursor(i,j,tmp)
		put_cursor()
		
	def spawn(self):
		piece = self.balcp if self.counter%2 ==1 else self.whitep
		board[self.hor][self.ver] = piece
		self.counter +=1

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
