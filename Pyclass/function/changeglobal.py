count =5
def myfun():
	count=10
	print(count)
myfun()
print(count)
def myglobalfun():
	global count   #use global instead local here
	count=10	#change the number of the global variable
	print(count)
myglobalfun()
print(count)

#nonlocal keyword is for the variable outside the local but not global
