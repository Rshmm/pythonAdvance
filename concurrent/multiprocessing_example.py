import multiprocessing

def worker(num):
    """
    get a number and print it
    """
    print(f"worker: {num}")


if __name__ == '__main__':
    processes = []


    for i in range(5):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("all the processes finished")


