#!/usr/bin/env python
from datetime import datetime
from functools import wraps

def timestamp(old_func):

    @wraps(old_func)
    def replacement(*args, **kwargs):
        print("{} called on {}".format(old_func.__name__, datetime.now().ctime()))
        return old_func(*args, **kwargs)

    return replacement


@timestamp
def spam(name):
    print("Hello from spam()")

@timestamp
def ham(day):
    print("hello from ham()")

# ham = timestamp(ham)
spam("Bob")
ham("Monday")
spam("Frieda")

print(spam.__name__)
print(ham.__name__)


def wombat(flag):

    def real_decorator(old_func):

        @wraps(old_func)
        def replacement(*args, **kwargs):
            print("hoo hoo: flag is", flag)
            return old_func(*args, **kwargs)

        return replacement
    return real_decorator


@wombat('alpha')
def wolverine():
    pass

wolverine = wombat('alpha')(wolverine)
















