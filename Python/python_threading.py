import threading
from queue import Queue
import time
from random import randint

queue = Queue()

file_lock = threading.Lock()

variable_lock = threading.Lock()

def initialize_file():
    file = open("python_threading.rtf", "w")
    file.write("Thread name \t Job number \t Start time \t End time \t count\n")
    file.close()

def process(job):
    start_time = time.asctime(time.localtime())
    time.sleep(1)
    with variable_lock:
        count = randint(1, 100)
    with file_lock:
        file = open("python_threading.rtf", "a")
        file.write(threading.current_thread().name + "\t" + str(job) + "\t" +
                   start_time + "\t" + time.asctime(time.localtime()) + "\t"
                   + str(count) + "\n")
        file.close()

def threader():
    while True:
        job = queue.get()
        process(job)
        queue.task_done()

initialize_file()

for worker in range(10):
    thread = threading.Thread(target = threader)
    thread.daemon = True
    thread.start()

start = time.time()

for job in range(20):
    queue.put(job)

queue.join()

print("Run time: " + str(time.time() - start))
print("Program terminating")
