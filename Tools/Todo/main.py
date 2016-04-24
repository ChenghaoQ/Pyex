import useraction
import today
import datatrans
def main():
	
	todo=today.TODO() 
	def init():
		try:
			todo.tmp='[   ]'
			todo.todolist=datatrans.loadfile()
		except FileNotFoundError:
			todo.reset('Reset')
		return 'Todo'
	def not_todo(state):
		todo.draw()
		action=useraction.get_user_action()
		response=defaultdict(lambda:state)
		response['Exit']='Exit'
	def GoToDo():
		todo.draw()
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
