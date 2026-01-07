from time import sleep
from multiprocessing import Process


def process_1():
    print('process 1 started')
    sleep(2)
    print('process 1 completed')


def process_2():
    print('process 2 started')
    sleep(2)
    print('process 2 completed')


# in windows , not in linux
if __name__ == '__main__':
    Process(target=process_1).start()
    Process(target=process_2).start()