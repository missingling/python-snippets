import time
import threading 
from threading import Thread

def t1():
    for _ in range(3):
        time.sleep(1.0)
        print "hello thread 1\n"
        
def t2():
    for _ in range(3):
        time.sleep(1.0)
        print "hello thread 2\n"

thread1 = Thread(target = t1)
thread2 = Thread(target = t2)

thread1.start()
thread2.start()

thread2.join()
thread1.join()
