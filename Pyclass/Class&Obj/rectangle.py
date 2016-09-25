class Rectangle:
	width=5
	height =3

	def getRect(self):
		print("width is %d"%self.width)
		print("Height is %d"%self.height)
	
	def setRect(self):
		self.height=int(input("set the height:"))
		self.width=int(input("set the width:"))
