from threading import Thread, current_thread, Lock
import time

# def my_thread(arg1, arg2):
#     print(current_thread().getName() + ' start')
#     print('%s  %s' % (arg1, arg2))
#     print(current_thread().getName(), 'stop')
#
#
# class MyThread(Thread):
#     def run(self):
#         print(current_thread().getName() + ' start')
#         print('run')
#         print(current_thread().getName(), 'stop')
#
#
# for i in range(1, 6):
#     t = Thread(target=my_thread, args=(i, i + 1))
#     t.start()
#
# t1 = MyThread()
# t1.start()
# t1.join()
#
# print(current_thread().getName(), 'stop')

# def loop():
#     print('thread %s is running...' % current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (current_thread().name, n))
#         time.sleep(1)
#     print('thread %s end.' % current_thread().name)
#
#
# print('thread %s is running...' % current_thread().name)
# t = Thread(target=loop, name='loopThread')
# t.start()
# t.join()
# print('thread %s ended.' % current_thread().name)

balance = 0
lock = Lock()


def change_it(n):
    global balance
    lock.acquire()
    try:
        balance += n
        balance -= n
    finally:
        lock.release()


def run_thread(n):
    for i in range(1000000):
        change_it(n)


t1 = Thread(target=run_thread, args=(5,))
t2 = Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance=%d' % balance)
