

class Draw(object):
	def __init__(self,todolist,name):
		self.todolist=todolist
		self.name=name
	def draw_TODO(self):
		print("* * * * %s * * * * *"%self.name)
		print("-"*40)
		for each in self.todolist:
			try:
				print('{:<3}{:<35}{:<}'.format(each[0],each[1],each[2]))
			except IndexError:
				pass
	def draw_string(string):
		print(string+'\n')







