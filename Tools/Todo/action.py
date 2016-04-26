class Operation(object):
        def __init__(self,todolist,cursor,status,init,counter):
                self.todolist=todolist
                self.cursor=cursor
                self.status=status
                self.init=init
                self.counter=counter
        def new_todo(self):
                task=useraction.get_user_input()
                if task =='Reset':
                        return 'Init'

                if self.counter<5:
                        self.todolist[self.counter]=[self.status[0],task,'[   ]']
                else:
                        self.todolist.append([self.status[0],self.task_jar[self.counter],'[   ]'])
                self.counter+=1
        def complete_todo(self):
                self.todolist[self.cursor][0]=self.status[1]
        def postpone_todo():
                self.todolist[self.cursor][0]=self.status[2]
        def remove_task(self):
                del self.todolist[self.cursor]
                self.counter-=1
                self.init-=1
                if self.init<5:
                        self.todolist.append([self.status[0],self.blank,'[   ]'])
                        self.init+=1
	def other_command(self):
		while True:
			other=input("Please enter your command: ")
			if other == 'Reset':
				pass
			elif other == 'Clear':
				pass
			elif other == 'Save':
				pass
			elif other == 'Load':
				pass
			elif other == 'Back':
				break
			elif other == ('Exit' or 'Quit'):
				return 0;
			else:
				print("Sorry, I can't do that, try again please~")
        def execution(self,action):
                if action ==  'New':
                        self.new_todo()
                elif action == 'Complete':
                        self.complete_todo()
                elif action == 'Postpone':
                        self.postpone_todo()
                elif action == 'Remove':
                        self.remove_task()
                elif action == 'Help' :
                        pass
                elif action == 'Other':
                        self.other_command()        

def TODO_operation(todo,action):
        opera=Operation(todo.todolist,todo.cursor,todo.status,todo.init,todo.counter)
        opera.execution(action)


