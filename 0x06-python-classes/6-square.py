#!/usr/bin/python3
""" 6-square
This module contains a simple class.

    Classes:
        Square: a class that define a square.
"""


class Square:

    """ A class that define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a Square instance.

        Args:
            __size: private instance attribute representing the size of
            the square must be a non negative int.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Position of the square. """

        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square. """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
