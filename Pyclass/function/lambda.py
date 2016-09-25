def funa(x,y=3):
	return x*y

# in lambda:
funalamb=lambda x,y=3 :x*y

#------------------
lambda x: x if x%2 else None
#back to normal
def is_odd(x):
	if x%2:
		return x
	else:
		return None
