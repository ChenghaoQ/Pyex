import useraction
import checklist
import datatrans
import draw
import os
import operation
def your_todolist():

	today=checklist.TODO('* * * *Today * * * *')
	def init():
		try:
			today.tmp='[   ]'
			today.todolist=datatrans.loadfile()
		except FileNotFoundError:
			today.reset('Reset')
#                future.reset('Reset')
		return 'Todo'
	def GoToDo():
		#Draw the list
		os.system('clear')
		a=draw.Draw(today.todolist,today.name)
		a.draw_TODO()
		action = useraction.get_user_action()


		if action in useraction.moves:
			while True:
				try:
					movement.moves(action,today.todolist,today.cursor,today.tmp.today.i)
					break
				except IndexError:
					action=useraction.get_user_action()
					continue
		else:
			if operation.TODO_operation(today,action)==0:
				return 'Exit'

		return 'Todo'

	state='Init'
	state_actions={'Init':init,
	'Todo':GoToDo}


	while state !='Exit':
		state=state_actions[state]()

your_todolist()
