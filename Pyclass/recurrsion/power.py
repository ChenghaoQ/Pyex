def power(x,y):
	if y==1:
		return x
	if y>0:
		return x*power(x,y-1)

number= int(input("plesse enter the number:" ))
times=int(input("please enter the times:"))

print(power(number,times))
