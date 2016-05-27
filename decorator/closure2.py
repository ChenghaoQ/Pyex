def func_150(val):
	passline = 60
	if val >= passline:
		print('pass')
	else:
		print('failed')
def func_100(val):
	passline = 90
	if val >= passline:
		print('pass')
	else:
		print('failed')

def set_passline(passline):
	def cmp(val):
		if val >= passline:
			print('Pass')
		else:
			print('failed')
	return cmp

f_100 = set_passline(60) #f_100 is a function 'cmp' with passline 60 set
f_100(89)
f_150 = set_passline(90)#f_150 is 'cmp' with passline 90 in settings
f_150(89)# call the 'cmp' with passline 90, val 89
