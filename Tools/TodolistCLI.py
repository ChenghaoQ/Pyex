
action=['Up','Down','Complete','New','Postpone','Remove','Save','Quit']
letter_code="WSKJLRCwskjlrc"
action_dict=dict(zip(letter_code*2,action*2))
moves=set(['Up','Down'])

def main():
	
	todo=TODO()
	
	def init():
		todo.reset(reset)
	def GoToDo():
		todo.draw()
		action = get_user_action()

		if action in moves:
			todo.move(action)
		else:
			todo.operation(action)

		return 'LIST'
        GoToDo()













def get_user_input():
	task = input("What Are We Gonna TODO today? :")
	return task



def get_user_action():
	char='N'
	char=raw_input("please enter an action: ")
	while char not in letter_code:
		char =raw_input("please enter an action: ")
	return action_dict[char]



class TODO(object):
	
	def __init__(self):
		self.todolist=[]
		self.task_jar=[]
		self.status=('☐','☑','☒')
		self.counter=0
		self.tmp='[   ]'
	def move(self):
		def init_cursor(counter,tmp):
			tmp=self.todolist[counter][2]
			return tmp
		def move_cursor(direction):
			if direction == 'Up':
				self.counter -= 1
			elif direction== 'Down':
				self.counter += 1
		def put_cursor(counter):
			self.todolist[counter][2]='[ * ]'
		def restore_cursor(counter,tmp):
			self.todolist[counter][2]=tmp
		
		move_cursor(direction)
		restore_cursor(self.counter,self.tmp)
		self.tmp=init_cursor(self.tmp)
		put_cursor(self.counter)
	def operation(self,action):
		def new_todo():
			self.task_jar.append(get_user_action())
			self.todolist.append((self.status[0],self.task_jar[self.counter],'[   ]'))
			self.counter+=1
		def complete_todo():
			self.todolist[self.counter][0]=self.status[1]
		def postpone_todo():
			self.todolist[self.counter][0]=self.status[2]
		def remove_task():
			del self.todolist[self.counter]
		def execution(action):
			if action ==  'New':
				new_todo()
			elif action == 'Complete':
				complete_todo()
			elif action == 'Postpone':
				postpone_todo()
			elif action == 'Remove':
				remove_task()
			elif action == 'Clear' :
				clear_list()
		execution(action)
	def draw(self):
		def draw_title():
			print("* * * * Welcome to Chenghao's todo list * * * * *")
		def draw_list():
			for each in self.todolist:
				print('  '.join(each))

		draw_title()
		draw_list()
	def reset(passwd):
		if passwd== 'Reset':
			del self.todolist[:]
			for n in range(5):
				self.todolist.append((self.status[0],self.blank,'[   ]'))
			self.tmp='[   ]'

	
#task should be looks like ☐ todo ☑ completed ☒ postponed  ☐ ☑ ☒
# t
main()
