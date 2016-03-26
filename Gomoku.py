#这是一个五子棋双人客户端
def main():
	playboard=[]
	playboard=InitBoard(playboard)
	counter=0


def InitBoard(board):
	board=[['+'for x in range(15)]for y in range(15)]
	return board
def printBoard(board):
	i=0
	for i in range(15):
		print(board[i])
def Checkifwin(board,x,y,times):
	if times%2==0:
		piece='O'
	else:
		piece='X'	
	if board[x-2][y-2]==piece and board[x-1][y-1]==piece and board[x][y]==piece and board[x+1][y+1]==piece and board[x+2][y+2]==piece:
		return True
	elif board[x-2][y]==piece and board[x-1][y]==piece and board[x][y]    ==piece and board[x+1][y]==piece and board[x+2][y]==piece:
		return True
	elif board[x][y-2]==piece and board[x][y-1]==piece and board[x][y]    ==piece and board[x][y+1]==piece and board[x][y+2]==piece:
		return True
	elif board[x-2][y+2]==piece and board[x-1][y+1]==piece and board[x][y]    ==piece and board[x+1][y-1]==piece and board[x+2][y-2]==piece:
		return True
	else:
		return False
def movepiece(board,row,col,times):
	if times%2==0:
		piece='O'
	else:
		piece='X'
	
	if board[row][col]=='+':
		board[row][col]=piece
def checkoccuption():
	if board[row][col]!='+'
		return False
	else
		return True
		
