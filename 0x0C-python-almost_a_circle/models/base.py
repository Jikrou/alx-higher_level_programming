#!/usr/bin/python3
"""models/base.py

Description:
    This module contains the Base class, which serves as the foundation for
    other classes in the application.

Classes:
    - Base: The base class from which other classes inherit.

Functions:
    - to_json_string: Converts a list of dictionaries to a JSON string.
    - from_json_string: Converts a JSON string to a list of dictionaries.
    - save_to_file: Saves a list of objects to a JSON file.
    - create: Creates an instance of a class with attributes provided
    in a dictionary.
    - load_from_file: Loads a list of instances from a JSON file.
"""
import json
import os


class Base:
    """Base class for managing instances."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + '.json'

        with open(filename, 'w') as file:
            strJson = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
            file.write(strJson)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes from a dictionary."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise ValueError('Class must be Rectangle or Square')

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""
        filename = cls.__name__ + '.json'
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)

            instances = []
            for dictionary in dictionaries:
                instance = cls.create(**dictionary)
                instances.append(instance)

            return instances
