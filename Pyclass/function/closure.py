def funX(x):
	def FunY(y):
		return x*y
	return FunY

i= FunX(8)
#i =FunY(y) and the x is 8
i(5) #return 40
FunX(8)(5) #return 40
#use function()() to 


def Funa():
	a=6
	def funb():
		nonlocal a 
		a+=1
		return a 
	return funb

a=Funa()
print(a())
print(a())
print(a())
