class Move(object):
	def __init__(self,todolist,cursor,tmp,i):
		self.tmp=tmp
		self.cursor=cursor
		self.todolist=todolist
		self.i=i
	def move_cursor(direction):
		if direction == 'Up':
			self.cursor -= 1
		elif direction== 'Down':
			self.cursor += 1
	def put_cursor(cursor):
		self.todolist[cursor][2]='[ * ]'
	def restore_cursor(cursor,tmp):
		self.todolist[cursor][2]=tmp



def moves(action,todolist,cursor,tmp,i):
	a=Move(todolist,cursor,tmp,i)
	a.move_cursor(direction)
	a.restore_cursor(a.i,a.tmp)
	a.i,a.tmp=init_cursor(a.cursor,a.tmp)
	a.put_cursor(a.cursor)
	
