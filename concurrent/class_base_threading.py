from datetime import datetime
from threading import Thread
from queue import Queue


class MyThread(Thread):
    def __init__(self,target,args):
        super().__init__()
        self.target = target
        self.args = args 


    def run(self):
        print(datetime.now())
        self.target(*self.args)


def sqrt(number, queue):
    queue.put(number ** 0.5)


numbers = [1,2,3,4,5,6,7,8,9,10]
queue = Queue()
threads = []

for number in numbers:
    t = MyThread(target=sqrt, args=(number, queue))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

results = []
while not queue.empty():
    results.append(queue.get())

print(results)


