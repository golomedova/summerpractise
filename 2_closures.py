# Замыкание
def closure(x):
    def inner(a):
        return x + a
    return inner

clos = closure(5)
print('closure = %s' % clos(5))


def func_closure(func):
    def inner(x):
        return func(x)
    return inner

clos1 = func_closure(lambda x: x**3)
print('func_closure = %s' % clos1(3))
