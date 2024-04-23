#!/usr/bin/python3
"""models/rectangle.py

Description:
    This module contains the Rectangle class, which represents a rectangle
    shape.

Classes:
    - Rectangle: Represents a rectangle shape.

Functions:
    - area: Calculates the area of the rectangle.
    - display: Displays the rectangle with "#" characters.
    - __str__: Returns a string representation of the rectangle.
    - update: Updates the attributes of the rectangle.
    - to_dictionary: Converts the rectangle attributes to a dictionary.
"""

from .base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y attribute."""

        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""

        return self.__width * self.__height

    def display(self):
        """Display the rectangle with '#' characters."""
        print(self.y * '\n')
        for i in range(self.__height):
            print(self.x * ' ', end="")
            print(self.__width * '#')

    def __str__(self):
        """String representation of the Rectangle."""

        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}"
                )

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes."""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""

        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height
                }
