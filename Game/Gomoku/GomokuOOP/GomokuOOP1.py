import getch
import gameboard 
action=['Up','Left','Down','Right','Spawn','Restart','Exit']
letter_code='WASDGEQwasdgrq'
action_dict=dict(zip(letter_code,action*2))
#letter_code=[ord(ch) for ch in 'WASDRQwasdrq'] 
#i,j,tmp=0,0,'+'# move section backup value initial

def main():
	
	game_board=gameboard.GameBoard()	
	def init():
		game_board.reset()
#		initcursor=game_board.move()
#		initcursor.init_cursor()
		return 'Game'
	def not_game(state):
		game_board.draw()
		action = get_user_action()
		response=defaultdict(lambda:state)
		response['Restart']
		
	def game():

		game_board.draw()
		action =get_user_action()
		if action =='Init':
			return 'Init'
		elif action == 'Exit':
			return 'Exit'
#		
		if action != 'Spawn':
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
		else:
			game_board.spawn(action)
#			break
		return 'Game'
	
	state='Init'
	state_actions={'Init':init,
			'Win':lambda:not_game('Win'),
			'Game':game}
	
	while state !='Exit':
		state = state_actions[state]()


def get_user_action():
	print("Move cursor please: ")
	#char = input("Move cursor please: ")
	char= getch.getch()
	while char not in action_dict:
		print("Wrong direction, again please: ")
		char=getch.getch()
	return action_dict[char]



		































main()
