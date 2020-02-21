#!/usr/bin/env python
import types

class Spam():
    ANIMAL = "wombat"

    def __init__(self, color):
        self.color = color

    def ham(self):
        print("ham!")

    def to_json(self):
        print("converting myself to JSON")

s = Spam("green")
print(s.color)
s.ham()
print()

print(dir(s))
print()

h = s.ham

print(type(h))
h()

method = "ham"

h2 = getattr(s, method)
color = getattr(s, "color")

print(h2, color)

for attr in dir(s):
    print("{:20s} {}".format(attr, getattr(s, attr)))

if hasattr(s, 'to_json'):
    func = getattr(s, 'to_json')
    print(s.to_json())



def new_ham(self):
    print("Porky Pig")

#       class name in class     new value for name
setattr(Spam, "ham",             new_ham)

s.ham()

def cheese(self):
    print("yum! cheese!")

setattr(Spam, "wildebeest", cheese)

print(dir(Spam))
s.wildebeest()

setattr(Spam, 'car', 'Maserati')

print(s.car)


m = Spam('pink')
print(m.car)

setattr(s, 'city', 'Albany')

print(s.city)

def wow():
    print("WOW O WOW")

# setattr(s, 'wow', types.MethodType(s, wow, Spam))

s.wow()






