import urllib.request
import re
import time
import gzip

def youmeizi():
	header = {
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
	girl = 0
	pages = int(input("Please enter the pages you want: "))
	girls_basket = []
	page = 1
	while page <= pages:
		url = "http://www.youmzi.com/xg/list_10_%d.html"%page
		requests = urllib.request.Request(url,headers =header)
		opened = urllib.request.urlopen(requests)
		content= opened.read().decode('gbk')
		repattern = re.compile(r'<li>.*?<img src="(.*?)".*?</li>',re.S)
		girls_link = re.findall(repattern,content)
		for each in girls_link:
			girls_basket.append(each)
		page+=1
	for link in girls_link:
		a = open(str(girl)+'.jpg','wb')
		b = urllib.request.Request(link,headers = {"Accept-Encoding": "gzip"})
		c = urllib.request.urlopen(b)
		d = gzip.GzipFile(fileobj = c)
		e = d.read()
		a.write(e)
		print("No. %d Girl downloaded"%girl)
		girl += 1

youmeizi()
