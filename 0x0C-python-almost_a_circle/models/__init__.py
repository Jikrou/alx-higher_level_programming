#!/usr/bin/python3

"""Package containing models for geometric shapes.

This package provides classes for representing geometric shapes such as
rectangles and squares. It includes functionality for creating, manipulating,
and serializing these shapes.

Modules:
    - base: Contains the Base class, which serves as the foundation for other
            classes in the package.
    - rectangle: Contains the Rectangle class, representing rectangles.
    - square: Contains the Square class, representing squares.
"""
from .base import Base
from .rectangle import Rectangle
from .square import Square
