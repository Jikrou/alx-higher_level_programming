#!/usr/bin/python3
""" 2-square

This module contains a simple class.

    Classes:
        Square: a class that define a square.

"""


class Square:

    """ A class that define a square."""

    def __init__(self, size=0):
        """ Initialize a Square instance.

        Args:
            __size: private instance attribute representing the size of
            the square must be a non negative int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
