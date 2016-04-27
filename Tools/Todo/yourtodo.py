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
		opera=operation.Operation(today.todolist,today.cursor,today.status,today.init,today.counter)
		return opera
	def GoToDo():
		while True:
			#Draw the list
			os.system('clear')
			a=draw.Draw(today.todolist,today.name)
			a.draw_TODO()
			action = useraction.get_user_action()
			print(op.counter)

			if action in useraction.moves:
				while True:
					try:
						movement.moves(action,today.todolist,today.cursor,today.tmp.today.i)
						break
					except IndexError:
						action=useraction.get_user_action()
						continue
			else:
				if op.execution(action)==0:
					break
	op=init()

	GoToDo()
	

your_todolist()
