def deco(func):
	def in_deco(x,y):
		print('in deco')
		func(x,y)     #or 
	print('call deco')
	return in_deco

@deco
def bar(x,y):
	print('in bar',x+y)
print(type(bar))
bar(1,2)
