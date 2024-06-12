from threading import Thread
import time


def func1():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


thread1 = Thread(target=func1)

thread1.start()
for j in 'abcdefghij':
    print(j)
    time.sleep(1)

thread1.join()