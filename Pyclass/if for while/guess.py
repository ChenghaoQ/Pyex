import random
times=3

guess=int(input("请输入一个数字，1-10:"))
num=random.randint(1,10)
while  guess >10 or guess<0:
	guess=int(input("Error,1-10 only:")	
while times>0:
	if guess > num:
		print("too big")
		times-=1
	elif guess < num:
		print("too small")
		times-=1
	elif guess == num:
		print("Bingo!")
		break
	
