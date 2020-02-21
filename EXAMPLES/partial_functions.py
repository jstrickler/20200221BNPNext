#!/usr/bin/env python
#
import re
from functools import partial

start = 0
stop = 25

print(list(range(0, 25, 2)), '\n')

count_by = partial(range, start, stop)  # <1>

print((list(count_by(1))))  # <2>   range(0, 25, 1)
print((list(count_by())))  # <2>   range(0, 25, 1)
print((list(count_by(3))))  # <2>   range(0, 25, 3)
print((list(count_by(5))))  # <2>
print()

has_a_number = partial(re.search, r'\d+')  # <3>

# m = re.search(pattern, text)

strings = [
    'abc', '123', 'abc123', 'turn it up to 11', 'blah blah'
]

for s in strings:
    print("{}:".format(s), end=' ')
    if has_a_number(s): # <4>
        print("YES")
    else:
        print("NO")

onetoten = partial(range, 1, 11)

for i in onetoten():
    print(i, end=' ')
print()
