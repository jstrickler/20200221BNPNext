#!/usr/bin/env python


with open('DATA/mary.txt') as mary_in:
    first_line = next(mary_in)
    for line in mary_in:
        print(line.rstrip())


class MyIterable:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        else:
            num = self.start
            self.start += 1
            return num

m = MyIterable(0, 10)
print(next(m))
print(next(m))
