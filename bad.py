"""This module is used to add the square of two numbers"""

import math


def messy_func(x, y):
    """This function returns the sum of 2 square numbers"""
    return math.pow(x, 2) + math.pow(y, 2)


print(messy_func(3, 4))
