import time
import threading

class MyThread(threading.Thread):
        def run(self):
               something()
                # for i in range(5):
               #         print('thread {},@number:{}'.format(self.name,i))

def main():
        print("start main threading")
        threads = [MyThread() for i in range(3)]

        for t in threads:
                t.start()
        print("End")



def something():
        for i in range(5):
                print('thread {},@number:{]')

main()

