import threading
import psutil
import time

def consume_system_resources():
    for i in range(50):
        for j in range(1000000):
            _ = j * j



def print_system_resources():
    while True:

        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory_percent = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_percent}% \t | Memory Usage: {memory_percent}%")



def main():

    resource_consumer_thread = threading.Thread(target=consume_system_resources)
    resource_consumer_thread.start()

    resource_printer_thread = threading.Thread(target=print_system_resources)
    resource_printer_thread.daemon = True
    resource_printer_thread.start()


    time.sleep(3)



if __name__ == "__main__":
    main()