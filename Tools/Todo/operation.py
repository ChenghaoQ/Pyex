import useraction
import helpdoc
import datatrans
import os
class Operation(object):
	def __init__(self,current,post,comp,future,today):
		self.todolist=current.todolist
		self.cursor=current.cursor
		self.status=current.status
		self.init=current.init
		self.counter=current.counter
		self.blank='_'*30
		self.post=post
		self.comp=comp
		self.future=future
		self.today=today
		self.a=current

	def new_todo(self):
		task=useraction.get_user_input()

		if self.counter[0]<5:
			self.todolist[self.counter[0]]=[self.status[0],task,'[   ]']
		else:
			self.todolist.append([self.status[0],task,'[   ]'])
		print("Further details need to describe?'\n'-->",end='')
		description=input()
		self.todolist[self.counter[0]].append(description)
		self.counter[0]+=1
	def complete_todo(self):
		self.todolist[self.cursor[0]][0]=self.status[1]
		self.comp.todolist.append(self.todolist[self.cursor[0]])
		self.remove_task()

	def postpone_todo(self):
		self.todolist[self.cursor[0]][0]=self.status[2]
		self.post.todolist.append(self.todolist[self.cursor[0]])
		self.remove_task()
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
				self.a.reset('Reset')
				break
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
				if os.path.exists('./data/usr/%s'%name):
					pass
				else:
					os.mkdir('./data/usr/%s'%name)
				datatrans.savefile(self.today,name,"today")
				datatrans.savefile(self.future,name,'future')
				datatrans.savefile(self.post,name,'postpone')
				datatrans.savefile(self.comp,name,'complete')
				break
			elif other == 'Load':
				pass
			elif other == 'Return':
				break
			elif other == ('Back' or 'Quit'):
				return 0
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



