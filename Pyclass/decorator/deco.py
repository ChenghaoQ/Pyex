def dec(func):
	print('call dec')
	def in_dec(*arg):
		print('in dec arg=',arg)
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val,int):
				return 0
		return func(*arg)
	return in_dec

@dec
def my_sum(*arg):
	print('in my_sum')
	return sum(arg)
print(my_sum(1,2,3,4,5)) #my_sum has already get the function in_dec 
@dec
def my_average(*arg):
	print('in my_avg')
	return sum(arg)/len(arg)
print(my_average(1,2,3,4,5))
#my_sum1 = dec(my_sum)
#my_sum1(1,2,3,4,5)
#print(my_sum1(1,2,3,4,5))
#print(my_sum(1,2,3,4,5))
#print(my_average(1,2,3,4,5))
