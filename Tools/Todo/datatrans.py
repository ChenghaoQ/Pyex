class Sav(object):
	def __init__(self,data):
		self.data=data
	def savedata(self,name):
		dat1=open("./bin/%s.dat"%name,'w')
		for line in self.data:
			for elem in line:
				if elem[2]=='[ * ]':

					elem[2]='[   ]'
				dat1.write(elem+',') 
			dat1.write('\n')
		dat1.close()
	

def savefile(datalist,name):
	wrote=Sav(datalist)
	wrote.savedata(name)

def loadfile():
	datafile=open('todolist.dat','r')
	listdata=[]
	for each in datafile:
		each=each.strip('\n')	
		b=each.split(',')
		b.pop()
		listdata.append(b)
	datafile.close()
	return listdata
def saveuser(usrdict,filename):
	f=open('./bin/%s'%filename,"a")
	#for line in usrdict.item():
	f.writelines('{} {} {}'.format(k,v,'\n') for k, v in usrdict.items())
	

