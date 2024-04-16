#!/usr/bin/python3
"""iA module defines a function to write an object using
JSON representation to a file ."""
import json


def save_to_json_file(my_obj, filename):
    """ A function that writes an Object to a text file,
    using a JSON representation. """
    with open(filename, "w") as file:
        jsnfle = file.write(json.dumps(my_obj))
