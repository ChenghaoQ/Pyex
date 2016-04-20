
board=[['+' for row in range(10)] for col in range(10)]
def change(board,row,col):
	playboard=board[:]
	directions=[[(1,1),(-1,-1)],[(0,1),(0,-1)],[(1,0),(-1,0)],[(-1,1),(1,-1)]]
	for lines in directions:
		print("redo at line",lines)
		for eachway in lines:
			print("redo at eachway",eachway)
			xd,yd =eachway
			for n in range(1,5):
				
				playboard[row + xd*n][col + yd*n] = playboard[row][col]

				for each in range(10):
					print(' '.join(playboard[each]))

				print('\n')						
#for each in range(10):
#	print(board[each])
print('\n')

row=int(input('enter row:'))
col=int(input('enter col:'))
board[row][col]='X'
change(board,row,col)

