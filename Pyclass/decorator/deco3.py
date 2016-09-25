def deco(func):
	def cmp(val):
		line = func()
		if val >= func():
			print('pass')
		else:
			print('failed')
	return cmp

@deco
def passline_150():
	return 90 
passline_150(88)


@deco
def passline_100():
	return 60
passline_100(88)


passline_150(60)
passline_100(60)
