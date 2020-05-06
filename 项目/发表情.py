import time
import threading
from queue Queue

class CustomThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()



def moyu_time(name,delay,counter):
    while counter:
        time.sleep(delay)
        print("{} 开始摸鱼 {}".format(name,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
        counter -= 1

if __name__ == '__main__':
    pool = ThreadPoolExecutor(20)
    for i in range(1,5):
        pool.submit(moyu_time('jiajun'+str(i),1,3))