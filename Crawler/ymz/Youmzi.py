import urllib.request
import re
import time
import gzip
import os
header = {      "Accept-Encoding": "gzip",
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
girl_entry = []

def get_entry_link():

        global girl_entry
        pages = int(input("Please enter the pages you want:"))
        page = 1
        while page <= pages:
                url = "http://www.youmzi.com/xg/list_10_%d.html"%page
                requests = urllib.request.Request(url,headers =header)
                opened = urllib.request.urlopen(requests)
                content= opened.read().decode('gbk')
                list_part_pattern=re.compile(r"</dl>(.*?)</ul>",re.S)
                list_part = re.findall(list_part_pattern,content)
                repattern = re.compile(r'<li>.*?<a href="(.+?).html" title="(.+?)".*?<p><a href.*?</li>',re.S)
                girl_link_found = re.findall(repattern,list_part[0])
                for each in girl_link_found:
                        girl_entry.append(each)
                page+= 1


def worker():
        global girl_entry
        entry_base = girl_entry.pop(0)
        pic_link_pool=pic_seeker(entry_base[0])
        pic_downloader(pic_link_pool,entry_base[1])


def pic_seeker(entry_link):
        link_pool = series_link(entry_link)
        pic_links = []
        num = 0
        for link in link_pool:
                req = urllib.request.Request(link,headers =header)
                oped = urllib.request.urlopen(req)
                cont = oped.read().decode('gbk')
                pic_pattern = re.compile(r"<div class=\"arpic\">.*?<ul>.*?<li>.*?<img src='(.+?)'.*?</li>.*?</ul>",re.S)
                pic_link = re.findall(pic_pattern,cont)
                pic_links.append(pic_link[0])
                num+=1
                print(pic_link[0],num)
        return pic_links        

def pic_downloader(pic_link_pool,series_name):
        if os.path.exists(os.path.join(os.path.dirname(__file__),'%s'%series_name)):
                return
        else:
                os.mkdir(os.path.join(os.path.dirname(__file__),'%s'%series_name))
        girl = 0
        for link in pic_link_pool:
                print('---link')
                a = open('%s/'%series_name+str(girl)+'.jpg','wb')
                b = urllib.request.Request(link,headers = header)
                c = urllib.request.urlopen(b)
                try:
                        d = gzip.GzipFile(fileobj = c)
                        e = d.read()
                except OSError:
                        e = c.read()
                a.write(e)
                print("No. %d Girl downloaded, - %s"%(girl,series_name))
                girl+=1
                a.close()                
                time.sleep(1)

def series_link(url_base):
        global header
        girl_series = []
        girl_series.append(url_base+'.html')
        begin = 2
        end = 100
        while begin+1 < end:
                mid = (begin+end)//2
                url = url_base+'_%d'%mid+'.html'
                try:
                        a = urllib.request.Request(url,headers= header)
                        b = urllib.request.urlopen(a)
                        ###
                        begin = mid
                except:
                        end = mid
        for each in range(2,begin+1):
                tmp_url = url_base+'_%d'%each+'.html' 
                girl_series.append(tmp_url)
        return girl_series


def main():
        global girl_entry
        get_entry_link()        
        #while girl_entry:
        worker()

 

main()






