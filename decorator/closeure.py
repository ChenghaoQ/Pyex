
passline = 60
def func(val):
	if val >= passline:
		print('pass')
	else:
		print('failed')
	def in_func():
		print(val)
	in_func()
	return in_func

f=func(89)
#f()#in_func#print ->89
print(f.__closure__)
