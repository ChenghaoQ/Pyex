import useraction
import todolist
import datatrans
import draw
import os
import action
def your_todolist():
	
	today=todolist.TODO('* * * *Today * * * *')
       # future=todolist.TODO('* * * *Future * * * *') 
	def init():
		try:
			today.tmp='[   ]'
			today.todolist=datatrans.loadfile()
		except FileNotFoundError:
			today.reset('Reset')
        #                future.reset('Reset')
		return 'Todo'
	def GoToDo():
                os.system('clear')
	        draw.Draw(today,today.name)
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
			action.operation(today,action)
			
		return 'Todo'
		
	state='Init'
	state_actions={'Init':init,
			'Todo':GoToDo}


	while state !='Exit':
		state=state_actions[state]()

