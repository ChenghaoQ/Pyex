import os
action=['Up','Down','Complete','New','Postpone','Remove','Exit']#'Save','Quit']
letter_code="WSKJLRQwskjlrq"
action_dict=dict(zip(letter_code,action*2))
moves=set(['Up','Down'])

def main():
	
	todo=TODO()
        	
	def init():
		todo.reset('Reset')
		return 'Todo'
	def not_todo(state):
		todo.draw()
		action=get_user_action()
		response=defaultdict(lambda:state)
		response['Restart']
	def GoToDo():
		todo.draw()
		action = get_user_action()

		if action in moves:
			todo.move(action)
		else:
			todo.operation(action)
		return 'Todo'
		
	state='Init'
	state_actions={'Init':init,
					'Win':lambda:not_todo('Win'),
					'Todo':GoToDo}


	while state !='Exit':
		state=state_actions[state]()


        







def get_user_input():
	task = input("What Are We Gonna TODO today? :")
	return task



def get_user_action():
	char='N'
	char=input("please enter an action: ")

	while char not in action_dict:
		char =input("please enter an action again: ")
	return action_dict[char]



class TODO(object):
	
	def __init__(self):
		self.todolist=[]
		self.task_jar=[]
		self.status=['☐','☑','☒']
		self.counter=0
		self.cursor=0
		self.i=0
		self.tmp='[   ]'
		self.blank='________________________'
	def move(self,direction):
		def init_cursor(cursor,tmp):
			tmp=self.todolist[cursor][2]
			return cursor,tmp
		def move_cursor(direction):
			if direction == 'Up':
				self.cursor -= 1
			elif direction== 'Down':
				self.cursor += 1
		def put_cursor(cursor):
			self.todolist[cursor][2]='[ * ]'
		def restore_cursor(cursor,tmp):
			self.todolist[cursor][2]=tmp
		
		move_cursor(direction)
		restore_cursor(self.i,self.tmp)
		self.i,self.tmp=init_cursor(self.cursor,self.tmp)
		put_cursor(self.cursor)
	def operation(self,action):
		def new_todo():
			self.task_jar.append(get_user_input())
			if self.counter<5:
				self.todolist[self.counter]=[self.status[0],self.task_jar[self.counter],'[   ]']
			else:
				self.todolist.append([self.status[0],self.task_jar[self.counter],'[   ]'])
			self.counter+=1
		def complete_todo():
			self.todolist[self.cursor][0]=self.status[1]
		def postpone_todo():
			self.todolist[self.cursor][0]=self.status[2]
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
		os.system('clear')
		draw_title()
		draw_list()
	def reset(self,passwd):
		if passwd== 'Reset':
			del self.todolist[:]
			for n in range(5):
				self.todolist.append([self.status[0],self.blank,'[   ]'])
			self.tmp='[   ]'
			self.new=0

	
#task should be looks like ☐ todo ☑ completed ☒ postponed  ☐ ☑ ☒
# t
main()
