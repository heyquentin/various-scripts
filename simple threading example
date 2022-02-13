#!/usr/bin/python3
import time
import threading

def print1():
    while (True):
        print("first thread")
        time.sleep(15)

def print2():
    while (True):
        print("every 2 seconds")
        time.sleep(2)

th1 = threading.Thread(target=print1)
th2 = threading.Thread(target=print2)

th1.start()
th2.start()
