def outside():
	print('I am outside')
	def inside():
		print('I am inside')
	inside()
outside()
#inside()  Inside not defined so cannot be find
#so it should call inside() in outside at line 5
#Part A
def outside():
	var =5
	def inside():
		var=3
		print(var)
	insdie()
ouside()

#Part B, cannot print var on line 20
def outside():
	var =5
	def inside():
		print(var)
		var=3
	inside()
ouside()

