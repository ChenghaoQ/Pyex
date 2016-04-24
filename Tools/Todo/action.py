class Operation(object):
        def __init__(self,todolist,cursor,status,init,counter):
                self.todolist=todolist
                self.cursor=cursor
                self.status=status
                self.init=init
                self.counter=counter
        def new_todo():
                task=useraction.get_user_input()
                if task =='Reset':
                        return 'Init'

                if self.counter<5:
                        self.todolist[self.counter]=[self.status[0],task,'[   ]']
                else:
                        self.todolist.append([self.status[0],self.task_jar[self.counter],'[   ]'])
                self.counter+=1
        def complete_todo():
                self.todolist[self.cursor][0]=self.status[1]
        def postpone_todo():
                self.todolist[self.cursor][0]=self.status[2]
        def remove_task():
                del self.todolist[self.cursor]
                self.counter-=1
                self.init-=1
                if self.init<5:
                        self.todolist.append([self.status[0],self.blank,'[   ]'])
                        self.init+=1
        
        def execution(action):
                if action ==  'New':
                        new_todo()
                elif action == 'Complete':
                        complete_todo()
                elif action == 'Postpone':
                        postpone_todo()
                elif action == 'Remove':
                        remove_task()
                elif action == 'Help' :
                        pass
                elif action == 'Other':
                        pass        

def TODO_operation(todo,action):
        opera=Operation(todo.todolist,todo.cursor,todo.status,todo.init,todo.counter)
        opera.execution(action)
                
