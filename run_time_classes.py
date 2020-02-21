#!/usr/bin/env python


Animal = type('Animal', (), {'move': lambda self: print("moving")})

def bark(self):
    print("woof! woof!")

color = "brown"


Dog = type('Dog', (Animal,), {'bark': bark, 'color': color})

d = Dog()

d.bark()
print(d.color)
d.move()

