import threading
import time


def say_hi(name):
    time.sleep(1)
    print("hi : " + name + "\n")

if __name__ == "__main__":
    names = ["mmreza","arsham","reza","armita"]
    locks = []

    for name in names:
        lock = threading.Lock()
        lock.acquire()
        locks.append(lock)
        threading.Thread(target=say_hi, args=(name,)).start()
        lock.release()


    print("Successfully done")