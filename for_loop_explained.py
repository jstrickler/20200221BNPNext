#!/usr/bin/env python


letters = ['a', 'b', 'c']

for letter in letters:
    print(letter, end=' ')
print()
print('-' * 60)

iletter = iter(letters)
while True:
    try:
        letter = next(iletter)
    except StopIteration:
        break
    print(letter, end=' ')






