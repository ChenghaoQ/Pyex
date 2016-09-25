L=[i*i for i in range(10)]
#the list comprehensions
List=[]
for i in range(10):
	List.append(i*i)
print(L,List)

#recover the code below
list1=[(x,y)for x in range(10) for y in range(10) if x%2 ==0 if y%2!=0]
print(list1)
list2=[]
for x in range(10):
	if x%2==0:
		for y in range(10):
			if y%2!=0:
				list2.append((x,y))
print(list2)
