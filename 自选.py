"""
记录型信号量解决生产者-消费者问题
"""

from threading import Thread, Semaphore
from time import sleep


def proceducer():
    global in_index, out_index
    empty.acquire()
    mutex.acquire()
    buffer[in_index] = 1
    in_index = (in_index + 1) % n
    print("缓冲池:", *buffer)
    full.release()
    mutex.release()


def consumer():
    global in_index, out_index
    full.acquire()
    mutex.acquire()
    buffer[out_index] = 0
    out_index = (out_index + 1) % n
    print("缓冲池:", *buffer)
    empty.release()
    mutex.release()


if __name__ == '__main__':
    in_index = 0
    out_index = 0
    n = 6
    buffer = [0] * n
    mutex = Semaphore(1)
    empty = Semaphore(n)
    full = Semaphore(0)
    process_list = [1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
    for t in process_list:
        if t == 1:
            thread = Thread(target=proceducer, args=())
            thread.start()
        if t == 2:
            thread = Thread(target=consumer, args=())
            thread.start()
