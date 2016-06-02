import requests
import json
import md5
import logging

logger = logging.getLogger('doubanfm') #get logger

class Netease(object):
	
	def __init__(self):
		pass

	def search(self,song_title,limit = 1):

		url = "http://music.163.com/api/search/pc"
		headers= {'Cookie':'appver =1.5.2',
			  'Referer':'http://music.163.com'}
		payload = {'s':song_title,
			   'limit':limit,
			   'type': 1}

		r =requests.post(url,params = payload, headers = headers)

		data = json.loads(r.text)

		if data['code'] == 200:
			return data['result']['songs'][0]
		else:
			return None

	def get_song_id(self,song_title):
		song = self.search(song_title)
	
		if song.get('hMusic',None):
			return song['hMusic']['dfsId'],song['hMusic']['bitrate']
		elif song.get('lMusic']['dfsId'],song['mMusic']['bitrate']
			return song['mMusic']['dfsId'],song['mMusic']['bitrate']
		elif song.get('lMusic',None):
			return song['lMusic']['dfsId'],song['lMusic']['bitrate']
		return None

	def get_url_and_bitrate(self,song_title):
		song_id,bitrate = self.get_song_id(song_title)
		url = 'http://m1.music.126.net/'
		if song_id:
			url += self.encrypted_id(song_id) + '/' +str(song_id)
			bitrate = str(bitrate/1000)
			return url,bitrate
		else:
			return None,None

	def encrypted_id(self,id):##########
		id = str(id)
		byte1 = bytearray('3go8&$8*3*3h0k(2)2')
		byte2 = bytearray(id)
		byte1_len=len(byte1)
		for i in xrange(len(byte2)):
			byte2[i] = byte2[i]^byte1[i%byte1_len]
		m = md5.new()
		m.update(byte2)###############
		result = m.digest().encode('base64')[:-1]
		result = result.replace('/','_')
		result = result.replace('+','-')
		return result

	if __name__ =='main':
		url,nitrate = Netease().get_url_and_bitrate("factory_of_faith")
		print url
		print bitrate


