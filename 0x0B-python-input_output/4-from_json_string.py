#!/usr/bin/python3
""" A module defines a function that deserialize a JSON string to an object."""
import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string."""
    return json.loads(my_str)
