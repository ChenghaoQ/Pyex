import curses



actions=['Up','Left','Down','Right','Restart','Exit']
letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
action_dict=dict(zip(letter_code,action*2))

def main(stdscr):
	def init():
	game_board.reset()
		return 'Game'

	def not_game(state):
		
		action =get_user_action(stdscr)
				
	def game();

		action = get_user_action(stdscr)
	



class GameBoard(object):
	
	def __init__(self,width=16,height=16,blackp='X',whitep='O',counter=0):
		self.width=width
		self.height=height
		self.blackp=blackp
		self.whitep=whitep
		self.counter=counter
	def boardinit(self):
		board=[['+' for row in range(17)]for col in range(17)]
		def setboarder(self):
			for hor in range(16):
				board[0][hor]='--'
				board[16][hor]=='--'
			for side in range(16):
				board[side][0] == '|'
				board[side][16] == '|'
			return board
		board = setboarder(board)
	
	def draw(self,screen):
		player1='	White'
		player2='	Black'
		
		def cast(string):
			screen.addstr(string+'\n')

		def draw_board(board):
			cast(board[row] for row in range(16))

		screen.clear()
		#maybe can cast the counter here
	def move_is_possible(self):
		#check if player can spawn the piece on the board
	def spawn(self):
		piece=self.blackp if self.counter%2==1 else self.whitep
		
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
                                        if counter ==5:
                                                return True
                                        else:
						False
					#return True if counter ==5 else False is not using properly here: return before assert
						
 
						
	def is_win(self):
		
	def reset(self);
		 					
