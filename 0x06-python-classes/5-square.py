#!/usr/bin/python3
""" 5-square
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
        self.__size = size

    @property
    def size(self):
        """ size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area of the square.

        Return:
           int: the area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """ Print the square with the character #."""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
