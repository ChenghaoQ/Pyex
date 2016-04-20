
action=['Up','Down','Complete','New','Postpone','Clear']
letter_code="WSKJLCwskjlc"
action_dict=dict(zip(action,letter_code))


def main():

















def get_user_action():
	pass



class TODO(object):
	
	def __init__(self):
		self.todolist=[]
		self.task_jar=[]
		self.status=(☐,☑,☒)
		self.counter=0
		self.tmp='[   ]'
	def move(self):
		def init_cursor(counter,tmp):
			tmp=self.todolist[counter][2]
			return tmp
		def move_cursor(direction):
			if direction == 'Up':
				self.counter -= 1
			elif direction= 'Down':
				self.counter += 1
		def put_cursor():
			self.todolist[counter][2]='[ * ]'
		def restore_cursor(counter,tmp):
			self.todolist[counter][2]=tmp
		
		move_cursor(direction)
		restore_cursor(self.counter,self.tmp)
		self.tmp=init_cursor(self.tmp)
		put_cursor
	def operation(self,action):
		def new_todo(self,task)::
			self.todolist.append((self.status[0],self.task_jar[counter],'%25s'%'[   ]'):
			self.counter+=1
		def complete_todo(self):
			self.todolist[counter][0]=self.status[1]
		def postpone_todo(self):
			self.todolist[counter][0]=self.status[2]
		def remove_task(self):
			del self.todolist[counter]
		def clear(action):
			del self.todolist[:]
	def draw(self):
		def title():
			print("* * * * Welcome to Chenghao's todo list * * * * *")

#task should be looks like ☐ todo ☑ completed ☒ postponed  ☐ ☑ ☒
# t
