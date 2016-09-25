a = [19,3,15,7,11,9,13,5,17,1]
print("%s%13s%17s"%('Element','Value','Histogram'))

for i in range(1,10):
	print('\n%7d%13d	'%(i,a[i]),end='')
	for j in range(1,a[i]):
		print('*',end='')

