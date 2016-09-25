#three color balls, red 3 yellow 3 green 6,get 8 ball randomly, get the rate
print('red\tyellow\tblue')
for red in range(0,4):
	for yellow in range(0,4):
		for green in range(2,7):
			if red + yellow + green==8:
				print(red,'\t',yellow,'\t',green)

red不需要定义类型赋值，在for loop里面已经赋予了值，即它当前循环次数
