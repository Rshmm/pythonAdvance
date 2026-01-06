# sequential programming

import time


# def say_hi(name):
#     time.sleep(1)
#     print(f"Hello {name}! nice to meet you.")
#
#
#
# say_hi("Arsham")
# say_hi("Reza")
# say_hi("Maryam")
#
#
# print("*" * 50)

# concurrent programming

import threading


def say_hi(name):
    time.sleep(1)
    print(f"Hello {name}! nice to meet you.")


# threading.Thread(target=say_hi, args=("Arsham",)).start()
# threading.Thread(target=say_hi,args=("Reza",)).start()
# threading.Thread(target=say_hi,args=("Maryam",)).start()


t1 = threading.Thread(target=say_hi, args=("Arsham",))
t2 = threading.Thread(target=say_hi,args=("Reza",))
t3 = threading.Thread(target=say_hi,args=("Maryam",))


t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()