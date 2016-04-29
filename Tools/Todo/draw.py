

class Draw(object):
	def __init__(self,todolist,name):
		self.todolist=todolist
		self.name=name
	def draw_TODO(self):
		print("* * * * %s * * * * *"%self.name+'\n')
		print("-"*40)
		for each in self.todolist:
			print('{:<3}{:<35}{:<}'.format(each[0],each[1],each[2]))
		print('\n')
		
	def draw_string(string):
		print(string+'\n')







