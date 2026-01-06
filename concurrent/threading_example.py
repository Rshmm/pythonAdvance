import threading
import time
from queue import Queue

def power_2(number, queue):
    time.sleep(2)
    queue.put(number ** 2)

numbers = [1,2,3,4,5,6,7,8,9,0]
queue = Queue()
threads = []

for number in numbers:
    t = threading.Thread(target=power_2, args=(number, queue))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

results = []
while not queue.empty():
    results.append(queue.get())

print(results)
