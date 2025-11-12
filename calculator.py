# https://github.com/aSquidE/lab11-WL-AP
# Partner 1: William Lin
# Partner 2: Abid Panahie

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if b <= 0 or b == 1 or a <= 0:
        raise ValueError
    return math.log(a, b)
def exp(a, b):
    return a ** b




