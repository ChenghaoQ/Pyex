n=0
a=open('todolist.dat','r')
g=[]
for each in a:
	each=each.strip('\n')	
	b=each.split(',')
	b.pop()
	g.append(b)
	
print(g)
a.close()
