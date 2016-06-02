"""
make lyric to dictionary
reference: (http://reverland.org/python/2014/10/09/lrc/)
"""
import re


def lrc2dict(lrc):
	def remove(x):
		return x.strip('[|]')


	lrc_dict = {}
	for line in lrc.split('\n'):
		if line.strip('\n'):
			time_stamps = re.finadall(r'\[[^\]]+\]',line)
			if time_stamps: #######?????
			# get the lrc
				lyric = line
				for tplus in time_stamps:
					lyric = lyric.replace(tplus,'')
			#get the time
				for tplus in time_stamps:
					t = remove(tplus)#####???????
					tag_flag = t.split(':')[0] ####???
					#pass :
					if not tag_flag.isdigit():
						continue

					# time accumulate
					time_lrc = int(tag_flag) * 60
					time_lrc += int(t.split(':')[1].split('.'[0])
					lrc_dict[time_lrc] = lyric
		return lrc_dict

def main():
	with open('3443588.lrc','r')as F:
		lrc = F.read()
	lrc_dict = lrc2dict(lrc)
	for key in lrc_dict:
		print(key,lrc_dict[key]

if __name__ = '__main__':
	main()

