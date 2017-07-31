a = 1


class Foo:
    a = 2

    def spam(self):
        a = 3
        for i in range(1):
            a = 4
            print('In loop: a = %s' % a)
        print('In method: a = %s' % a)
        print('In class: a = %s' % Foo.a)

print('In global: a = %s' % a)
Foo().spam()

Foo.a = 5
print(Foo.a)