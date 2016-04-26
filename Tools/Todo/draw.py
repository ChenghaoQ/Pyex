

class Draw(object):
	def __init__(self,todolist,name):
		self.todolist=todolist
		self.name=name
	def draw_TODO(self):
		print("* * * * %s* * * * *"%self.name+'\n')
		for each in self.todolist:
			print('  '.join(each))
	def draw_string(string):
		print(string+'\n')







