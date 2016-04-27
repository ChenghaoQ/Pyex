class Move(object):
	def __init__(self,todolist,cursor,tmp):
		self.tmp=tmp
		self.cursor=cursor
		self.todolist=todolist
	#	self.i=i
	def init_cursor(self):
		self.tmp[0]=self.todolist[self.cursor[0]][2]
	def move_cursor(direction):
		if direction == 'Up':
			self.cursor[0] -= 1
		elif direction== 'Down':
			self.cursor[0] += 1
	def put_cursor(self):
		self.todolist[self.cursor[0]][2]='[ * ]'
	def restore_cursor(self):
		self.todolist[self.cursor[0]][2]=self.tmp[0]



def moves(action,todolist,cursor,tmp):
	a=Move(todolist,cursor,tmp)
	a.move_cursor(direction)
	a.restore_cursor()
	a.init_cursor()
	a.put_cursor()
	
