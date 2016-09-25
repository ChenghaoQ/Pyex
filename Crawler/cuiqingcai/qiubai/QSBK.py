import urllib.request
import re


class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
		self.headers={'User-Agent' : self.user_agent}
		self.j=0
		self.stories =[]
		self.enable = False

	def get_Page(self,pageIndex):
		try:
			url = "http://www.qiushibaike.com/8hr/page/%d/?s=4881134"%pageIndex
			req = urllib.request.Request(url,headers = self.headers)
			response = urllib.request.urlopen(req)
			pageCode = response.read().decode('utf-8')
			return pageCode
		except:
			print("failed to connect to QS wiki")
			return None
	def getPageItems(self,pageIndex):
		pageCode = self.get_Page(pageIndex)
		if not pageCode:
			print('Failed to load page')
			self.enable = False ######
			return None
		pattern = re.compile('<h2>(.+?)</h2>.*?<div class="content">(.+?)</div>.*? class="number">(.*?)</i>')
		items = re.findall(pattern,pageCode)
		pageStories = []
		for item in items:
			print('No.%d crawling finished'%self.j)
			pageStories.append(item)#########
			print(item)
			self.j+=1
		return pageStories
	def loadPage(self):
		if self.enable == True:
			pageStories = self.getPageItems(self.pageIndex)
			print('\n\nThe %d page finished\n\n'%self.pageIndex)
			if pageStories:
				self.stories.extend(pageStories)
				self.pageIndex +=1
	def start(self):
		self.enable = True
		while self.enable:
			self.loadPage()#loadpage() load getPageItems() and getPageItems() load getPage()
		
spider = QSBK()
spider.start()

