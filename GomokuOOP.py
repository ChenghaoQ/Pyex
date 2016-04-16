action=['Up','Left','Down','Right','Restart','Exit']
letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
action_dict=dict(zip(letter_code,action*2))


def main():
	def init():
		game_board.reset()
		return 'Game'
	def not_game(state):
		game_board.draw()
		
	def game():
		game_board.draw()
	
	game_board=GameBoard()	
	game_board.draw()







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
			board[0][hor]=board[16][hor]='--'
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
	def move(self):
		def init_cursor():
			tmp=self.board[self.hor][self.ver]
			self.board[self.hor][self.ver]= '*'
		def move_cursor():
			pass		
		def recover_cursor():
			pass

		moves={}
		moves['Left']= lambda self.ver: self.ver -1
		moves['Right'] = lambda self.ver: self.ver +1
		moves['Up'] = lambda self.hor: self.hor -1
		moves['Down']= lambda self.hor: self.hor +1

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
					if self.board[self.hor][self.ver] = self.board[self.hor + xd*n][self.ver + xd*n]:
						counter +=1
					else:
						break
					if counter == 4:
						return True
		return False

	def reset(self):
		boardinit()
		































main()
