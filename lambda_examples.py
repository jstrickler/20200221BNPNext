#!/usr/bin/env python
import operator


def squared(x):
    return x ** 2

def cubed(x):
    return x ** 3


def doit(n, func):
    return func(n)


print(doit(5, squared))
print(doit(.5, squared))
print(doit(5, cubed))

print(doit(5, lambda x: 10 * x))

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

f1 = sorted(fruits, key=lambda e: e.upper())
print("f1:", f1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people, key=lambda e: e[-1]):
    print(person)


# lambda x, y: x + y

print(operator.add(5, 10))
print(operator.pow(2, 16))

print(operator.truediv(5, 3))

def doit(s):
    return s[:3].upper()

print(doit("watermelon"))

f3 = map(doit, fruits)
print("f3:", list(f3), '\n')

f3 = (f[:3].upper() for f in fruits)























