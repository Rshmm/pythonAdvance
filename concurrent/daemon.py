import time
from threading import Thread


def say_hi(name):
    time.sleep(1)
    print("hi ", name)

#
# Thread(target=say_hi,args=("Arsham",), daemon=True).start()
# Thread(target=say_hi,args=("Reza",), daemon=True).start()
# Thread(target=say_hi,args=("Maryam",), daemon=True).start()
# Thread(target=say_hi,args=("Amir",), daemon=True).start()



t = Thread(target=say_hi, args=("Arsham", ))
# print(t.isDaemon()) # deprecate
t.daemon = True
# t.setDaemon(True) # deprecate
print(t.daemon)
t.start()
