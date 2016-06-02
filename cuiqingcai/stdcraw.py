

class UrlManager(object):
	def __init__(self):
		self.new_urls=set()
		self.old_urls=set()


	def add_new_url(self):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			sel.fnew_urls.add(url)

	def add_new_urls(self):	
		if urls is None or len(urls)==0:
			return
		for url in urls:
			self.add_new_url(url)
	def has_new_url(self):
		return len(self.new_urls)!=0
	

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url


class HtmlDownloader(object):
	
	def download(self,url):
		if url is None:
			return None
		response=urllib.request.urlopen(url)
			
		if response.getcode() !=200:
			return None
		return response.read()#######decode!!!??


class HtmlParser(object):

	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links = soup.find_all('a',href = re.compile(r'/view/\d+\.htm')s
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls
	def _get_new_data(self,page_url,soup):
		res_data={}
		#url
		res_data['url']=page_url
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title"))###########
		res_data['title']=title_node.get_text()
		
		summary_node = soup.find('div',class = "lemma-summary")
		res_data['summary']=title_node.get_text()

	
	def parse(self,page_url,html_cont):
		if page_url is None or htm;_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')#############

		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data


class HtmlDownload(object):
	
	def download(self,url):
		if url is None:
			return None
	response = urllib.request.urlopen(url)

	if response.getcode()!=200
		return None
	
	return response.read().decode('utf-8')
		
