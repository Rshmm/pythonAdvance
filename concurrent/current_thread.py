import time
from tqdm import tqdm
from threading import Thread, current_thread

def task(iterations):
    thread_name = current_thread()
    for i in tqdm(range(iterations), desc=thread_name.name):
        time.sleep(0.1)


Thread(target=task, args=(10, )).start()
Thread(target=task, args=(20, )).start()
Thread(target=task, args=(30, )).start()
Thread(target=task, args=(40, )).start()
