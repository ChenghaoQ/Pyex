import re,time,threading,urllib.request

pool = []
page = 0
lock = threading.Lock()
class ProxySeeker(threading.Thread):

        def __init__(self,thread_id,func):
                super(ProxySeeker,self).__init__()
                self.thread_id = thread_id
                self.func = func
        def run(self):
                print("线程 %d 开始工作"%self.thread_id)
                self.func(self.thread_id)
                print("线程 %d 完成任务"%self.thread_id)


def seeker(parafunc):
        def in_seeker(thread_id):#decorate need closure to wrap
                global pool
                header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
                global page
                source_name,pages,urls,repattern,thread_id = parafunc(thread_id)
                while page < pages:
                        lock.acquire() #get the lock in case url get page changed by other thread before next line executed
                        page += 1
                        page_number = page #copy the page number in case other changes number and cause the Done print with wrong number
                        url = eval(urls)
                        lock.release()#release the lock 
                        request = urllib.request.Request(url, headers = header)
                        content = urllib.request.urlopen(request).read().decode('utf-8')
                        reprox = re.compile(repattern,re.S)
                        proxies = re.findall(reprox,content)
                        for prox in proxies:
                                prox = prox + (source_name,)
                                if prox not in pool:
                                        pool.append(prox)
                        print("Thread %d get page %d Done!"%(thread_id,page_number))
                        #time.sleep(1)
        return in_seeker


@seeker
def kuaidaili(thread_id):
        source_name = " |  快代理  "
        pages = 15
        urls = '"http://www.kuaidaili.com/proxylist/%d/"%page'
        repattern  = r'<td data-title="IP">(.+?)</td>.*?<td data-title="PORT">(.+?)</td>.*?<td data-title="匿名度">(.+?)</td>.*?<td data-title="类型">(.+?)</td>.*?<td data-title="get/post支持">(.+?)</td>.*?<td data-title="位置">(.+?)</td>.*?<td data-title="响应速度">(.+?)</td>.*?<td data-title="最后验证时间">(.+?)</td>'
        return source_name,pages,urls,repattern,thread_id




def Proxypool():
        global pool
        page = 1
        print("主线程开始...")
        threads = [ProxySeeker(i,kuaidaili) for i in range(1,6)]
        for thread in threads:
                #time.sleep(0.5)
                thread.start()
        print("主线程结束...")
        
Proxypool()



