import gameboard 
import useraction
from collections import defaultdict 

def main():
	
	game_board=gameboard.GameBoard()	
	def init():
		game_board.reset()
#		initcursor=game_board.move()
#		initcursor.init_cursor()
		return 'Game'
	def not_game(state):
		game_board.draw()
		action = useraction.get_user_action()
		response=defaultdict(lambda:state)
		response['Restart']
		
	def game():

		game_board.draw()
		action =useraction.get_user_action()
		if action =='Init':
			return 'Init'
		elif action == 'Exit':
			return 'Exit'
#		
		if action != 'Spawn':
			try:
				game_board.move(action)
			except:
				print("Out of range right now,Try again please")
				action =useraction.get_user_action()
				game_board.move(action)
		else:
			game_board.spawn(action)
			if game_board.Judge():
				return 'Win'
#			break
		return 'Game'
	
	state='Init'
	state_actions={'Init':init,
			'Win':lambda:not_game('Win'),
			'Game':game}
	
	while state !='Exit':
		state = state_actions[state]()


if __name__=='__main__':
	main()
