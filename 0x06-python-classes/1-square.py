#!/usr/bin/python3
""" 1-square

This module contains a simple class.

    Classes:
        Square: a class that define a square.

"""


class Square:

    """ A class that define an empty square."""

    def __init__(self, size=None):
        """ Initialize a Square instance.

        Args:
            size: private instance attribute representing the size of
            the square.
        """
        self.__size = size
