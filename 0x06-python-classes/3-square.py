#!/usr/bin/python3
""" 3-square

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

    def area(self):
        """ Calculate the area of the square.

        Return:
           int: the area of the square
        """

        return self.__size ** 2
