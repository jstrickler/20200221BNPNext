#!/usr/bin/env python
from pprint import pprint

x = 5
animal = 'wombat'

def spam():
    superhero = 'Deadpool'
    print(locals())


g = globals()
pprint(g)

print()
spam()

print(g['animal'])

g['color'] = "blue"

print(color)

g['bark'] = lambda : print("Woof! Woof!")

bark()

print('foo')
print(type(bark))

print(__builtins__)
print(dir(__builtins__))

class Spam():
    def ham(self):
        pass

s = Spam()
print(dir(s))

print(dir(x))

print("foo".upper())











