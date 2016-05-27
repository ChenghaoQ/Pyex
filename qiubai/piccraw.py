import urllib.request
import re

page=int(input("please enter the pages you want to craw:"))

headers = {  
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        } 
j=0
for i in range(1,page+1):
	
	tmp=urllib.request.Request("http://www.qiushibaike.com/pic/page/%s/?s=4878168"%str(i),headers=headers)
	urls=urllib.request.urlopen(tmp)
	buf=urls.read().decode('utf-8')
	piclist=re.findall(r'http:.+\.jpg',buf)

	for pic in piclist:
		f=open(str(j)+'.jpg','wb')
		links=urllib.request.urlopen(pic)
		picture=links.read()
		f.write(picture)
		print("Finished crawling No.%d"%j)
		j+=1

