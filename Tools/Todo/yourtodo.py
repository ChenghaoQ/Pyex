import useraction
import checklist
import datatrans
import draw
import os
import operation
import movement
def your_todolist():

	today=checklist.TODO('* * * *Today * * * *')
	future=checklist.TODO('* * * * Future * * * *')
	switcher=0
	#current=today

	def init(current):

		try:
			#today.tmp='[   ]'
			future.reset('Reset')
			today.todolist=datatrans.loadfile()
		except FileNotFoundError:
			today.reset('Reset')
#                future.reset('Reset')
		#opera=operation.Operation(current.todolist,current.cursor,current.status,current.init,current.counter)
		#return opera
	def GoToDo():
		nonlocal current
		nonlocal switcher
		while True:
			#Draw the list
			os.system('clear')
			a=draw.Draw(today.todolist,today.name)
			b=draw.Draw(future.todolist,future.name)
			a.draw_TODO()
			b.draw_TODO()
			print(current.todolist)
			print("-----%d------"%switcher)
			print("-"*40)
			action = useraction.get_user_action()
			
			
			if action == 'Switch':
				switcher+=1
				
				continue
			if switcher%2==0:
				current=today
			elif switcher%2==1:
				current=future
			
			if action in useraction.moves:
				while True:
					try:
						movement.moves(action,current.todolist,current.cursor,current.tmp,current.i)
						break
					except IndexError:
						action=useraction.get_user_action()
						continue
			else:
				op=operation.Operation(current.todolist,current.cursor,current.status,current.init,current.counter)
				if op.execution(action)==0:
					break
	init()

	GoToDo()
	

your_todolist()
