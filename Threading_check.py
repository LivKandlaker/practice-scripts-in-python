from threading import Thread
from datetime import datetime
from time import time, sleep


def task_thread_1():
    while True:
        sleep(10 - time() % 10)
        print("Thread 1")
        print(datetime.now().now().strftime("%H:%M:%S"))


def task_thread_2():
    while True:
        sleep(10 - time() % 10)
        print("Thread 2")
        print(datetime.now().now().strftime("%H:%M:%S"))


Thread(target=task_thread_1).start()
Thread(target=task_thread_2).start()

