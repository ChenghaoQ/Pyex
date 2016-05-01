class Sav(object):
	def __init__(self,todo):
		self.data=todo.todolist
		self.cursor=todo.cursor
		self.counter=todo.counter
		self.i=todo.i
		self.tmp=todo.tmp
	def savedata(self,id,title):
		dat1=open("./data/usr/%s/%s.dat"%(id,title),'w')
		for line in self.data:
			if line[2]=='[ * ]':
				line[2]='[   ]'
			try:
				dat1.writelines('{},{},{},{},{}'.format(line[0],line[1],line[2],line[3],'\n'))
			except:
				dat1.writelines('{},{},{},{}'.format(line[0],line[1],line[2],'\n'))
		dat1.close()
	def saveargs(self,id,title):
		dat2=open("./data/usr/%s/%s_args.dat"%(id,title),'w')
		dat2.writelines(('{},{},{},{},{}'.format(self.cursor[0],self.counter[0],self.i[0],self.tmp[0],'\n')))
		dat2.close()
def savefile(todo,userid,title):
	wrote=Sav(todo)
	wrote.savedata(userid,title)
	wrote.saveargs(userid,title)

def loadfile(id,title):
	datafile=open("./data/usr/%s/%s.dat"%(id,title),'r')
	listdata=[]
	for each in datafile:
		each=each.strip('\n')	
		b=each.split(',')
		b.pop()
		listdata.append(b)
	datafile.close()
	return listdata
def loadargs(id,title):
	dat3=open("./data/usr/%s/%s_args.dat"%(id,title),'r')
	ldata=[]
	for each in dat3:
		each=each.strip('\n')	
		b=each.split(',')
		b.pop()
		#ldata.append(b)
		#print(b)

	return int(b[0]),int(b[1]),int(b[2]),b[3]

def loadall(userid,today,future,post,comp):
	today.todolist=loadfile(userid,'today')
	future.todolist=loadfile(userid,'future')
	post.todolist=loadfile(userid,'postpone')
	comp.todolist=loadfile(userid,'complete')
	today.cursor[0],today.counter[0],today.i[0],today.tmp[0]=loadargs(userid,'today')
	future.cursor[0],future.counter[0],future.i[0],future.tmp[0]=loadargs(userid,'future')
	post.cursor[0],post.counter[0],post.i[0],post.tmp[0]=loadargs(userid,'postpone')
	comp.cursor[0],comp.counter[0],comp.i[0],comp.tmp[0]=loadargs(userid,'complete')


def saveuser(usrdict,userid):
	f=open('./data/Userdata.dat',"w")
	#for line in usrdict.item():
	for k, v in usrdict.items():
		f.writelines('{} {} {} {}'.format(k,v,userid[k],'\n') )
	f.close()

def loaduser():
	g=open('./data/Userdata.dat','r')
	list1=[]
	list2=[]
	list3=[]
	for each in g:
		each=each.strip('\n')
		c=each.split(' ')
		list1.append(c[0])
		list2.append(c[1])
		list3.append(c[2])
	dic=dict(zip(list1,list2))
	dic2=dict(zip(list1,list3))
	return dic,dic2
	g.close()

