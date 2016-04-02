def main():
	g=open("24_data.txt",'r')
	while True:
		list_24=[]
		list_24=g.readline()
		print(list_24)
		if list_24=='':
			g.close()
			break
		list_24=list_24.strip('\n')
		list_24=list_24.split(' ')
		for i in range(4):
			if list_24[i]=='A':
				list_24[i]=1
			elif list_24[i]=='J':
				list_24[i]=11
			elif list_24[i]=='Q':
				list_24[i]=12
			elif list_24[i]=='K':
				list_24[i]=13
			list_24[i]=int(list_24[i])


		distri = position(list_24)	
		for i in range(24):
			calculate(distri[i])


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
			n1,n2,n3=calc2
			for calc2 in range(4):
				if calc2 == 0:
					num = plus(list2[n1],list2[n2])
				if calc2 == 1:
					num = minus(list2[n1],list2[n2])
				if calc2 == 2:
					num = muti(list2[n1],list2[n2])
				if calc2 == 3:
					num = divid(list2[n1],list2[n2])
				list3 = [num,list2[n3]]
				for calc3 in range(6):
					if calc3 == 0:
						num = plus(list3[0],list3[1])
					if calc3 == 1:
						num = minus(list3[0],list3[1])
					if calc3 == 2:
						num = muti(list3[0],list3[1])
					if calc3 == 3:
						num = divid(list3[0],list3[1])
					if calc3 == 4:
						num = minus(list3[1],list3[0])
					if calc3 == 5:
						num = divid(list3[1],list3[0])
					if num == 24:
						Str1 ='('+str(list1[0])+sign(calc1)+str(list1[1])+')'
						#Str1 = " ".join(Str1)
						list20 = [Str1,str(list2[1]),str(list2[2])]
						list4 = [0,0,0]
						list4[n1] =list20[0]
						list4[n2] =list20[1]
						list4[n3] =list20[2]
						print('(%s%s%s)%s%s'%(list4[0],sign(calc2),list4[1],sign(calc3),list4[2]))
						
	return list1


def get_list():
	g=open("24_data.txt",'r')
	list_24=[]
	list_24=g.readline()
	list_24=list_24.strip('\n')
	list_24=list_24.split(' ')
	for i in range(4):
		if list_24[i]=='A':
			list_24[i]=1
		elif list_24[i]=='J':
			list_24[i]=11
		elif list_24[i]=='Q':
			list_24[i]=12
		elif list_24[i]=='K':
			list_24[i]=13
		list_24[i]=int(list_24[i])
	return list_24
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
def sign(x):
	if x==0:
		return '+'
	elif x==1 or x==4:
		return '-'
	elif x==2:
		return 'x'
	elif x==3 or x==5:
		return 'div'



main()		
