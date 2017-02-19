from bs4.element import Tag


class Tode():
	def __init__(self,node,parent):
		self.children=[]
		self.parent = parent
		self.node = node

class BSTree():

	def __init__(self,root):

		self.root = root
		self.tree = None
	def load_nodes(self,roottag=None):
		L =[]
		if roottag == None:
			roottag = self.root
		for each in roottag:
			if isinstance(each,Tag):
				pass
			else:
				pass
		return L



'''def tree_dict(roottag):
	L={}
 	for each in roottag:
 		print(each.name)
 		if isinstance(each,Tag):
 			subdir=tree_dict(each)
 			if each.name in L:
 				L[each.name].append(subdir)
 			else:
 				L[each.name]=[subdir,]
 		else:
 			L[each.name]=each

 	retur'.n L'''