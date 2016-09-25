l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
#zip by tuple
l3=list(zip(l1,l2))
print(l3)
#list by list 
l4=list(map(lambda x,y:[x,y],l1,l2))
print(l4)
