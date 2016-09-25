def make_repeat(n):
	return lambda s:s *n

double = make_repeat(2)
print(double(8))
print(double('FishC'))


#this is using lambda to do the closure
