#!/usr/bin/python3
"""square.py

Description:
    This module contains the Square class, which represents a square shape.

Classes:
    - Square: Represents a square shape.

Functions:
    - __init__: Initializes a Square instance.
    - size: Getter and setter for the size attribute.
    - update: Updates the attributes of the square.
    - __str__: Returns a string representation of the square.
    - to_dictionary: Converts the square attributes to a dictionary.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ public method that assigns attributes."""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def __str__(self):
        """String representation of Square"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
