import curses

def main(stdscr):
	def init():
	game_board.reset()
		return 'Game'

	def not_game(state):
		
	def game();


	



class GameBoard(object):
	
	def __init__(self,width=16,height=16,blackp='X'.whitep='O'):
		self.width=width
		self.height=height
		self.blackp=blackp
		self.whitep=whitep
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
	def move_is_possible(self):
	
	def spawn(self):
		piece=self.blackp if counter%2==1 else self.whitep
		
			
	def winner(self):
					
