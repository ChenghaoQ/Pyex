#有一个长阶梯，上不同步子大小剩下阶梯数不同


num=0
while True:
	if num%2==1:
		if num%3==2:
			if num%5==4:
				if num%6==5:
					if num%7==0:
						print(num)
						break
	num+=1
