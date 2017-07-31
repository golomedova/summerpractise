import time
import threading


def first_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/countdown.py """
    class CountdownThread(threading.Thread):
        def __init__(self, count):
            threading.Thread.__init__(self)
            self.count = count

        def run(self):
            while self.count > 0:
                print("Counting down", self.count)
                self.count -= 1
                time.sleep(5)
            return

    # Sample execution
    t1 = CountdownThread(10)
    t1.start()
    t2 = CountdownThread(20)
    t2.start()


def second_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/countdown2.py """
    def countdown(count):
        while count > 0:
            print("Counting down", count)
            count -= 1
            time.sleep(5)
        return

    # Sample execution
    t1 = threading.Thread(target=countdown, args=(10,))
    t1.start()
    t2 = threading.Thread(target=countdown, args=(20,))
    t2.start()


def third_example():
    """ join example """
    def countdown(count):
        while count > 0:
            print("Counting down", count)
            count -= 1
            time.sleep(5)
        return

    # Sample execution
    t1 = threading.Thread(target=countdown, args=(10,))
    t1.start()
    t1.join(timeout=6)
    print('Thread joined')


def fourth_example():
    """ http://www.dabeaz.com/usenix2009/concurrent/race.py """
    x = 0  # A shared value

    count = 10000000

    def foo():
        nonlocal x
        for i in range(count):
            x += 1

    def bar():
        nonlocal x
        for i in range(count):
            x -= 1

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)


if __name__ == '__main__':
    first_example()
    # second_example()
    # third_example()
    # fourth_example()
