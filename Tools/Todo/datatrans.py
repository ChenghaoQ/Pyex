class Sav(object):
	def __init__(self,data):
		self.data=data
	def savedata(self,id,title):
		dat1=open("./data/usr/%s/%s.dat"%(id,title),'w')
		for line in self.data:
			if line[2]=='[ * ]':
				line[2]='[   ]'
			dat1.writelines('{},{},{},{}'.format(line[0],line[1],line[2],'\n'))
		dat1.close()
	

def savefile(datalist,name,title):
	wrote=Sav(datalist)
	wrote.savedata(name,title)

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

