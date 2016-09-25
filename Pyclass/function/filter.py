#get the number can be divided by 3 in 100

def divid3():
	times=100//3
	for each in range(times):
		print(each*3,end='')


divid3()
#Use the filter to get the same result
list(filter (lambada n: not(n%3), range(1,100)


#使用列表推导式
[i for i in range(1,100) if  not(i%3)]
