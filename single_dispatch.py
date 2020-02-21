#!/usr/bin/env python
from singledispatch import singledispatch

@singledispatch
def barf(x):
    pass

@barf.register(float)
def _barf(x: float):
    print("float!")

@barf.register(int)
def _barf(x: int):
    print("int!")

@barf.register(str)
def _barf(x: str):
    print("str!")

barf(5)
barf(5)
barf(5.0)
barf("5")
