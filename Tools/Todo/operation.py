import useraction
import helpdoc
import datatrans
class Operation(object):
	def __init__(self,todolist,cursor,status,init,counter):
		self.todolist=todolist
		self.cursor=cursor
		self.status=status
		self.init=init
		self.counter=counter
		self.blank='_'*30
	def new_todo(self):
		task=useraction.get_user_input()

		if self.counter[0]<5:
			self.todolist[self.counter[0]]=[self.status[0],task,'[   ]']
		else:
			self.todolist.append([self.status[0],task,'[   ]'])
		self.counter[0]+=1
	def complete_todo(self):
		self.todolist[self.cursor[0]][0]=self.status[1]
	def postpone_todo(self):
		self.todolist[self.cursor[0]][0]=self.status[2]
	def remove_task(self):
		del self.todolist[self.cursor[0]]
		self.counter[0]-=1
		self.init-=1
		if self.init<5:
			self.todolist.append([self.status[0],self.blank,'[   ]'])
			self.init+=1
	def other_command(self,name):
		while True:
			other=input("Please enter your command: ")
			if other == 'Reset':
				pass
			elif other == 'Clear':
				i=0
				L=len(self.todolist)
				
				while i < L:
					if self.todolist[i][0]=='☒':
						del self.todolist[i]
						i-=1
						L-=1
					i+=1
						
						
					print(self.todolist)
				if L<5:
					b=(5-L)
					print(b)
					for n in range(b):
						self.todolist.append(['☐',self.blank,'[   ]'])
				break
			elif other == 'Save':
				datatrans.savefile(self.todolist,name)
				break
			elif other == 'Load':
				pass
			elif other == 'Back':
				break
			elif other == ('Exit' or 'Quit'):
				return 0;
			else:
				print("Sorry, I can't do that, try again please~")
	def execution(self,action,name):
		if action ==  'New':
			self.new_todo()
		elif action == 'Complete':
			self.complete_todo()
		elif action == 'Postpone':
			self.postpone_todo()
		elif action == 'Remove':
			self.remove_task()
		elif action == 'Help' :
			print(helpdoc.help)
			input("Press Enter to continue...")
		elif action == 'Other':
			if self.other_command(name)==0:
				return 0        

def TODO_operation(todo,action):
	opera=Operation(todo.todolist,todo.cursor,todo.status,todo.init,todo.counter)
	if opera.execution(action)==0:
		return 0



