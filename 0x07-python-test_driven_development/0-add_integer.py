#!/usr/bin/python3
"""
A simple module for performing addition operation.

functions:add_integer: add two number and return the result.
"""


def add_integer(a, b=98):

    """  add to number and return the result
         a + b
         :return: the sum of a and b.  """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    x = int(a) + int(b)
    return x
