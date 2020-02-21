#!/usr/bin/env python

class Foo():
    COLOR = "taupe"
    def __init__(self, name):
        self._name = name

    def bar(cls):
        print(cls.COLOR)

    bar = classmethod(bar)

    def name(self):
        return self._name

    print(type(name))
    name = property(name)
    print(type(name))




f = Foo("Fred")
f.bar()
Foo.bar()


# @spam
# def ham():
#     pass
#
# ham = spam(ham)






def doit(some_func):
    x = some_func()
    print(x)


def whiz():
    print("whizzzzz!")
    return 88


doit(whiz)












