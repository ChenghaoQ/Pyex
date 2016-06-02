import urllib.request
import re
#import thread
#import time


class QBwiki:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
		
		self.headers = {'User-Agent' : self.user_agent}
		self.stories = []
		self.enable = False # to check if the

	def getPage(self,pageIndex): # why put pageIndex here
		try:
			url= "http://www.qiushibaike.com/hot/page/%s/?s=4878178"%str(pageIndex) 
			request = urllib.request.Request(url,headers = self.headers)
			response = urllib.request.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode

		except:
			print("Failed to connect to QS wiki")
			return None

	def getPageItems(self,pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print("Failed to load page")
			return None
		pattern = re.compile('<div class="content"[^.]+?</div>')
		items = re.findall(pattern,pageCode)
		pageStories = []
		for item in items:
			replaceBR = re.compile('<div class="content">|</div>')
			text = re.sub(replaceBR,"\n",item)
			pageStories.append(text)
		return pageStories
	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1
	def getOneStory(self,pageStories,page):
		for story in pageStories:
			a=input()
			self.loadPage()
			#The program won't exit until get 'Q'
			if a == 'Q':
				self.enable = False
				return
			print(story)#######################
	def start(self):
		print("正在读取糗事百科,按回车查看新段子，Q退出")
		self.enable = True
		self.loadPage()
		nowPage=0
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage +=1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)

spider = QBwiki()
spider.start()
 






 
			
