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
		if Checkifwin(playboard,row,col,counter) == True:
			print("\n\n\n\白方胜！！\n\n\n")
			break
		print("* * * * 黑棋，棋子为'X'* * * * ")
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
		if Checkifwin(playboard,row,col,counter) == True:
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
def Checkifwin(board,x,y,times):
	if times%2==0:
		piece='O'
	else:
		piece='X'
	a=0;b=0;c=0;d=0;i=0;j=0;
	direc=[[1,0][1,1][0,1][-1,1][-1,0][-1,-1][0,-1][1,-1]]
	for i in range(8):
		for j in range(5):
			if board[row+direc[i][0]][col+direc[i][1]]==board[row][col]:
				if direc[i][0]==0:
					a+=1
				elif direc[i][1]==0:
					b+=1
				#Unsure with the line below
				elif direc[i][0] != 0 and direc[i][1]==1:
					c+=1
				elif direc[i][1]==-1:
					d+=1
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
