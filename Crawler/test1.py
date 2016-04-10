import re
import urllib
import urllib.request
from collections import deque

queue = deque() # deque for locking the list, can just operate with the top and end
visited = set() # container 

url = 'http://news.dbanotes.net' #Entry

queue.append(url) 
cnt=0

while queue:
	url = queue.popleft() #get the head element
	visited |= {url}     #marked for |= (visited = visited | {url},actually it will append element to a new list, but why

	print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
	cnt+=1
	
	urlop =urllib.request.urlopen(url)  #Now open the url
	if 'html' not in urlop.getheader('Content-Type'):
		continue 
	
	#avoid the exception terminate the program, use try catch
	try:
		data = urlop.read().decode('utf-8')
	except:
		continue #ignore the exception

	linkre = re.compile('href=\"(.+?)\"')
	for x in linkre.findall(data):	
		if 'http' in x and x not in visited:
			queue.append(x)
			print('加入队列 --->	' + x)


	
