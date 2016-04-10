import re
import urllib
import urllib.request
from collections import deque


data={}
data['word'] = 'Jecvay Notes'
url_values=urllib.parse.urlencode(data) #print word=Jecvay+Notes, urlencode to make the string to url format
url="http://www.baidu.com/s?"
full_url=url+url_values

data=urllib.request.urlopen(full_url).read() # data from the search result page
data=data.decode('UTF-8') # use utf-8 decode the data
print(data)

