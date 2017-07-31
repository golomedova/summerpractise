# Функция
def func(x):
    return sum([i for i in range(x)])


# Простой декоратор
def outer(func):
    def inner(x):
        return func(x+1)
    return inner


# Декорирование
@outer
def func1(x):
    return func(x)
print('func1(5) = %s' % func1(x=5))
# ИЛИ
func2 = outer(func)
print('func1(5) = %s' % func2(x=5))


# Функция замера времени выполнения функции
import datetime
def timeit(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        delta = datetime.datetime.now() - start
        print('Time: %s' % str(delta))
        return result
    return inner

# Пример
func3 = timeit(func)
func3(10)

# Декоратор измерения всех функций класса
def time_class(cls):
    class NewCls(cls):
        def __getattribute__(self, s):
            x = super().__getattribute__(s)
            # проверяем, что x является методом
            if hasattr(x, '__call__'):
                print('func: %s' % str(x.__name__))
                return timeit(x)
            return x
    return NewCls


@time_class
class Foo:
    def spam1(self):
        return 1

    def spam2(self):
        return 2


foo = Foo()
foo.spam1()
foo.spam2()


# Декораторы с параметрами
def ext_time_class(methods: list):
    def time_class(cls):
        class NewCls(cls):
            def __getattribute__(self, s):
                x = super().__getattribute__(s)
                # проверяем, что x является методом
                if hasattr(x, '__call__') and x.__name__ in methods:
                    print('func: %s' % str(x.__name__))
                    return timeit(x)
                return x

        return NewCls
    return time_class


# Пример
@ext_time_class(['spam2'])
class Bar:
    def spam1(self):
        return 1

    def spam2(self):
        return 2

bar = Bar()
bar.spam1()
bar.spam2()
