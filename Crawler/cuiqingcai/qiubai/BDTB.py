import urllib
import re

headers=


class Tool:
	
	removeImg=re.compile('<img.*?>| {7}|')
	removeAddr = re.compile('<a.*?>|</a?')
	replaceLine=re.compile('<tr>|<div>|</div>|</p>'
	replaceTD= re.compile('<tr>|<div>|</div>|</p>')
	replacePara = re.compile('<p.*?>')
	replaceBR = re.compile('<br><br>|</br>')
	removeExtraTag = re.compile('<.*?>')
	def replace(self.x)
		x =re.sub(self.removeImg|self.removeAddr|
	#########
class BDTB:
	def __init__(self,baseUrl,seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()
		self.files = None
		self.floor =1
		self.defaultTitle =u"BDTB"
		self.fllorTag = floorTag

	def getPage(self.pageNum):
		try:
			url = self.baseURL + self.seeLZ +'&pn=' + str(pageNum)
			request = urllib.request.Request(url)
			response =urllib.request.urloprn(request)
			print(response.read())
			return response.read().decode('utf-8')
		except:
			print('error occured')
			return None
code=input("please enter the post code:")
baseURL = 'http://tieba.baidu.com/p/'+str(code)
floorTag=input("Would like to get the floor info?(1/0)")
bdtb = BDTB(baseURL,seelz,floorTag)
bdtb.start()

