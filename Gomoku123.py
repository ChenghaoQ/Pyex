import curses



actions=['Up','Left','Down','Right','Restart','Exit']
letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
action_dict=dict(zip(letter_code,action*2))

def main(stdscr):
	def init():
		game_board.reset()
			return 'Game'

	def not_game(state):
		game_board.draw(stdscr)	
		action =get_user_action(stdscr)
		response = defaultdict(lambda:state)
	def game();
		game_board.draw(stdscr)
		action = get_user_action(stdscr)
		if action == 'Restart':
			return 'Init'
		if action =='Exit':
			return 'Exit'
	state_actions = {'Init':init,  #put state into a dictionary
		#	'Win':lambda:not_game('Win'),
		#	'Gameover':lambda:not_game('Gameover'),
			'Game':game
		}


	curses.use.default_colors()
	game_board=GameBoard()
	state='Init'

	while state != 'Exit':
		state = state_actions[state]()

def get_user_action(keyboard):
	char = 'N'
	while char not in action_dict:
		char= keboard.getchar()
	return action_dict[char]


class GameBoard(object):
	
	def __init__(self,hor,ver,blackp='X',whitep='O',counter=0):
		self.hor=hor
		self.ver=ver
		self.blackp=blackp
		self.whitep=whitep
		self.counter=counter
		self.reset()
	def boardinit(self):
		board=[['+' for row in range(17)]for col in range(17)]
		for hor in range(17):
			board[0][hor]= board[16][hor]='--'
		for side in range(17):
			board[side][0]=board[side][16] = '|'
		self.board = board
	
	def draw(self,screen):
		player1='	White'
		player2='	Black'
		
		def cast(string):
			screen.addstr(string+'\n')

		def draw_board(board):
			cast(' ',join(self,board[row]) for row in range(18))

		screen.clear()
		
		#maybe can cast the counter here
#	def move_is_possible(self):
		#check if player can spawn the piece on the board
	def move(self,direction):
		def init_cursor(i,j):
			tmp=board[i][j]
			board[i][j]='*'
		def move_cursor(direction,moves):#self, direction
			board[i][j]=tmp
			#down=i+1
			#up=i-1
			#left=j-1
			#right=j+1
			board[i][j]='*'
			#if the cursor moved, temp back to the board
		moves={}
		moves['Left'] = lambda j: j-1
		moves['Right'] = lambda j: j+1
		moves['Up'] = lambda i : i-1
		moves['Down'] = lambda i: i+1

		if direction in moves:   # mark down
			if #self.move_is_possible(direction):
				self.board[i][j]=moves[direction]
				self.spawn()
				return True
			else:
				return False
	def spawn(self):
		piece=self.blackp if self.counter%2==1 else self.whitep
		board[self.hor][self.ver]=piece
		
	def Judge(self):
		directions=[[(1,1),(-1,-1)],[(0,1),(0,-1)],[(1,0),(-1,0)],[(-1,1),(1,-1)]]
		for lines in directions:
			counter=0
			for eachway in lines:
				xd,yd = eachway
				for n in range(1,5):
					# if board[x][y] = board[x+xd*n][y+yd*n] else break doesn't work: break is statement not condition expression
					if board[x][y] = board[x+xd*n][y+yd*n]:
                                                counter+=1
                                        else:
                                                break 
                                        if counter ==4:
                                                return True
                                        else:
						False
					#return True if counter ==5 else False is not using properly here: return before assert
						
 
						
	def is_win(self):
		
	def reset(self);
		self.board=
			 					
