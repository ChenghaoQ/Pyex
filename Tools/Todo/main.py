import useraction
import todolist
import datatrans
import draw
import os
def main():
	
	today=todolist.TODO('* * * *Today * * * *')
        future=todolist.TODO('* * * *Future * * * *') 
	def init():
		try:
			today.tmp='[   ]'
			today.todolist=datatrans.loadfile()
		except FileNotFoundError:
			today.reset('Reset')
                        future.reset('Reset')
		return 'Todo'
	def not_todo(state):
                os.system('clear')
	        draw.Draw(today,today.name)
                draw.Draw(future,future.name)	
		action=useraction.get_user_action()
		response=defaultdict(lambda:state)
		response['Exit']='Exit'
	def GoToDo():
                os.system('clear')
	        draw.Draw(today,today.name)
                draw.Draw(future,future.name)	
                action = useraction.get_user_action()

		if action=='Exit':
			datatrans.savefile(todo.todolist)
			return 'Exit'

		if action in useraction.moves:
			while True:
				try:
					todo.move(action)
					break
				except IndexError:
					action=useraction.get_user_action()
					continue
		else:
			todo.operation(action)
			
		return 'Todo'
		
	state='Init'
	state_actions={'Init':init,
			'Win':lambda:not_todo('Win'),
			'Todo':GoToDo}


	while state !='Exit':
		state=state_actions[state]()

if __name__ == '__main__':
	main()
