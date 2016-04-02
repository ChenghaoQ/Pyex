def main():
	list3=[1,1,4,6]
	print(position(list3))
	print(calculate(list3))

def calculate(list1):
	num = 0
	pos=[[0,1,2],[0,2,1],[1,2,0]]
	for calc1 in range(4):
		if calc1 == 0:
			num = plus(list1[0],list1[1])
		if calc1 == 1:
			num = minus(list1[0],list1[1])
		if calc1 == 2:
			num = muti(list1[0],list1[1])
		if calc1 == 3:
			num = divid(list1[0],list1[1])
		list2 = [num,list1[2],list1[3]]
		for calc2 in pos:
			[n1,n2,n3]=calc2
			for calc in range(4):
				if calc == 0:
					num = plus(list2[n1],list2[n2])
				if calc == 1:
					num = minus(list2[n1],list2[n2])
				if calc == 2:
					num = muti(list2[n1],list2[n2])
				if calc == 3:
					num = divid(list2[n1],list2[n2])
				list3 = [num,list2[n3]]
				for calc in range(6):
					if calc == 0:
						num = plus(list2[0],list2[1])
					if calc == 1:
						num = minus(list2[0],list2[1])
					if calc == 2:
						num = muti(list2[0],list2[1])
					if calc == 3:
						num = divid(list2[0],list2[1])
					if calc == 4:
						num = minus(list2[1],list2[0])
					if calc == 5:
						num = divid(list2[1],list2[0])
					if num == 24:
						return list1

def position(list1):
	list2=[0,0,0,0];listcopy=[]
	distr={}
	counter=0
	for each1 in range(4):
		list2[0]=list1[each1]
		for each2 in range(4):
			if each2== each1:
				continue                                                
			list2[1]=list1[each2]
			for each3 in range(4):
				if each3==each1 or  each3==each2:
					continue
				list2[2]=list1[each3]
				for each4 in range(4):
					if each4==each1 or  each4==each2 or each4==each3:
						continue
					list2[3]=list1[each4]
					listcopy.append(list2[:])
					distr[counter]=listcopy[counter]
					counter+=1  				
	return distr						

def plus(x,y):
	return x+y
def minus(x,y):
	return x-y
def muti(x,y):
	return x*y
def divid(x,y):
	if y== 0:
		return 5000
	else:
		return x/y

main()		
