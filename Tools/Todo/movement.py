class Move(object):
	def __init__(self,current):
		self.tmp=current.tmp
		self.cursor=current.cursor
		self.todolist=current.todolist
		self.i=current.i
	def init_cursor(self):
		
		self.tmp[0]=self.todolist[self.cursor[0]][2]
		self.i[0]=self.cursor[0]
	def move_cursor(self,direction):
		if direction == 'Up':
			self.cursor[0] -= 1
		elif direction== 'Down':
			
			self.cursor[0] += 1
	def put_cursor(self):
		self.todolist[self.cursor[0]][2]='[ * ]'
	def restore_cursor(self):
		self.todolist[self.i[0]][2]=self.tmp[0]



def moves(action,current):
	a=Move(current)
	a.move_cursor(action)
	a.restore_cursor()
	a.init_cursor()
	a.put_cursor()
	
