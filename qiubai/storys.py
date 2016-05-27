import urllib.request
import re
#<div class="content"> </div>
page=int(input("please enter the pages you want to craw:"))

headers = {  
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        } 
j=0
f=open('story.md','w')
for i in range(1,page+1):
	
	tmp=urllib.request.Request("http://www.qiushibaike.com/hot/page/%s/?s=4878178"%str(i),headers=headers)
	urls=urllib.request.urlopen(tmp)
	buf=urls.read().decode('utf-8')
	a=re.compile('<h2>(.+?)</h2>.*?<div class="content">(.+?)</div>.*? class="number">(.*?)</i>',re.S)
	stylist=re.findall(a,buf)
	for sty in stylist:
		form="Author:%s\n Post:%s Like:%s\n* * *"%(sty[0],sty[1],sty[2])
		print("No.%d story crawled"%j)
		f.writelines(form)
		j+=1
f.close()
"""	for pic in piclist:
		f=open(str(j)+'.jpg','wb')
		links=urllib.request.urlopen(pic)
		picture=links.read()
		f.write(picture)
		print("Finished crawling No.%d"%j)
		j+=1
"""
