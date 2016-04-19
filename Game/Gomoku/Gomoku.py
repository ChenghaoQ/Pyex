#这是一个五子棋双人客户端
def main():
	playboard=[]
	playboard=InitBoard(playboard)
	counter=0
	printBoard(playboard)
	while True:
		
		print("* * * * 白方，棋子为'O'* * * * ")
		while True:
			row=int(input("请输入横行坐标："))
			col=int(input("请输入竖行坐标："))
			row-=1;col-=1;
			if checkoccupation(playboard,row,col)==True:
				movepiece(playboard,row,col,counter)
				printBoard(playboard)
				counter+=1
				break
			else:
				print("对不起，此处已有棋子，请重新输入！")
		if Checkifwin(playboard,row,col) == True:
			print("\n\n\n\白方胜！！\n\n\n")
			break
		print("* * * * 黑棋，棋子为'X'* * * * ")
		while True:
			row=int(input("请输入横行坐标："))
			col=int(input("请输入竖行坐标："))
			row-=1;col-=1;
			if checkoccupation(playboard,row,col,counter)==True:
				movepiece(playboard,row,col)
				printBoard(playboard)
				counter+=1
				break
			else:
				print("对不起，此处已有棋子，请重新输入！")
		if Checkifwin(playboard,row,col) == True:
			print("\n\n\n\黑方胜！！\n\n\n")
			break
	


def InitBoard(board):
	board=[['+'for x in range(15)]for y in range(15)]
	return board
def printBoard(board):
	i=0
	print("   ",end='')
	for i in range(15):
		print("%d"%(i+1)+' 'if i<9 else "%d"%(i+1) ,end='')
	print("\n")
	for i in range(15):
		print("%d"%(i+1)+' '+' '.join(board[i]) if i+1>=10  else "%d"%(i+1)+'  '+' '.join(board[i]))
def Checkifwin(playboard,row,col):
	directions=[[(1,1),(-1,-1)],[(0,1),(0,-1)],[(1,0),(-1,0)],[(-1,1),(1,-1)]]
	for lines in directions:
		counter=0
		for eachway in lines:
			xd,yd =eachway
			for n in range(1,5):
				if playboard[row][col] == playboard[row + xd*n][col + xd*n]:
					counter +=1
				else:
						break
				if counter == 4:
					return True
	return False
def movepiece(board,row,col,times):
	if times%2==0:
		piece='O'
	else:
		piece='X'
	
	if board[row][col]=='+':
		board[row][col]=piece
def checkoccupation(board,row,col):
	if board[row][col]!='+':
		return False
	else:
		return True

main()		
