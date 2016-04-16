action=['Up','Left','Down','Right','Restart','Exit']
letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
action_dict=dict(zip(letter_code,action*2))


def main():
	
	game_board=GameBoard()	
	def init():
		game_board.reset()
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
		if game_field.move(action):
			if game_field.Judge():
				return 'Win'
		return 'Game'
		game_board.move()
	state='Init'
	state_actions={'Init':init,
			'Win':lambda:not_game('Win')
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
		self.hor =1 
		self.ver =1
		self.blackp=blackp
		self.whitep=whitep
		self.board=None
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

		#os.system('clear')
		for row in range(17):
	#		draw_board(row)
			print (' '.join(self.board[row]))
	def move(self,direction):
		i,j=0,0
		tmp=None
		#Move cursor
		def init_cursor(i,j,tmp):
			i,j=self.hor,self.ver   #record position
			tmp=self.board[self.hor][self.ver] #record content
			self.board[self.hor][self.ver]= '@'
			return i,j,tmp
	
		def movement(direction):
			if direction == 'Left':
				self.ver-=1
			elif direction == 'Right':
				self.ver += 1
			elif direction == 'Up':
				self.hor -=1
			elif direction == 'Down':
				self.hor += 1
		def backup_cursor(i,j,tmp):
			self.board[i][j]=tmp
		i,j,tmp=init_cursor(i,j,tmp)
		move_cursor(direction)
		self.board[self.hor][self.ver]='@'
		backup_cursor(i,j,tmp)
		
		
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
		boardinit()
		































main()
