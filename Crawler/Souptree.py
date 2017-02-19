from bs4.element import Tag
class Tode():

	def __init__(self,root):
		self.root = root
		self.child = {}



def load_node(roottag,child=None):
	tode = Tode(roottag)
	for each in roottag:
		if isinstance(each,Tag):
			subhook = load_node(each,tode.child)
			if each.name in tode.child:
				tode.child[each.name].append(subhook)
			else:
				tode.child[each.name]=[subhook,]
	return tode