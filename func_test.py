import time


def timer1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('timer1 run {sec} seconds'.format(sec=stop_time - start_time))


def timer(func):
    def wrapper(*a):
        start_time = time.time()
        func(*a)
        stop_time = time.time()
        print('timer run {sec} seconds'.format(sec=stop_time - start_time))

    return wrapper


@timer
def i_can_sleep(a, b, c):
    print(a + b + c)
    time.sleep(0.1)


# num = timer(i_can_sleep)
# num()

i_can_sleep(1, 5, 10)
