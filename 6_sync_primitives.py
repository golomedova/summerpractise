import threading

import time


def first_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/lock_ex.py """
    x = 0  # A shared value
    x_lock = threading.Lock()  # A lock for synchronizing access to x

    count = 1000000

    def foo():
        nonlocal x
        for i in range(count):
            x_lock.acquire()
            x += 1
            x_lock.release()

    def bar():
        nonlocal x
        for i in range(count):
            x_lock.acquire()
            x -= 1
            x_lock.release()

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)


def second_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/lock_with.py """
    x = 0  # A shared value
    x_lock = threading.Lock()  # A lock for synchronizing access to x

    count = 1000000

    def foo():
        nonlocal x
        for i in range(count):
            with x_lock:
                x += 1

    def bar():
        nonlocal x
        for i in range(count):
            with x_lock:
                x -= 1

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)


def third_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/rlock_ex.py """
    class Foo(object):
        lock = threading.RLock()

        def __init__(self):
            self.x = 0

        def add(self, n):
            with Foo.lock:
                self.x += n

        def incr(self):
            with Foo.lock:
                self.add(1)

        def decr(self):
            with Foo.lock:
                self.add(-1)

    # Two functions that will run in separate threads and call methods
    # on the above class.

    def adder(f, count):
        while count > 0:
            f.incr()
            count -= 1

    def subber(f, count):
        while count > 0:
            f.decr()
            count -= 1

    # Create some threads and make sure it works
    count = 100000
    f = Foo()
    t1 = threading.Thread(target=adder, args=(f, count))
    t2 = threading.Thread(target=subber, args=(f, count))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f.x)


def fourth_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/sema_signal.py """
    done = threading.Semaphore(0)
    item = None

    def producer():
        nonlocal item
        print("I'm the producer and I produce data.")
        print("Producer is going to sleep.")
        time.sleep(10)
        item = "Hello"
        print("Producer is alive. Signaling the consumer.")
        done.release()

    def consumer():
        print("I'm a consumer and I wait for data.")
        print("Consumer is waiting.")
        done.acquire()
        print("Consumer got", item)

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()


# Что будет, если Lock поменять на RLock?
def fifth_example():
    """ deadlock example """
    x = 0  # A shared value
    x_lock = threading.Lock()  # A lock for synchronizing access to x

    def meth1():
        nonlocal x
        while True:
            print('meth1, x = %d' % x)
            x_lock.acquire()
            x = x + 1

    def meth2():
        nonlocal x
        while True:
            print('meth2, x = %d' % x)
            x_lock.acquire()
            x = x - 1

    t1 = threading.Thread(target=meth1)
    t2 = threading.Thread(target=meth2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)

if __name__ == '__main__':
    # first_example()
    # second_example()
    # third_example()
    # fourth_example()
    fifth_example()
