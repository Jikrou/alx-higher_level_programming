#!/usr/bin/python3
""" A module that defines a function that serialize a string to JSON."""
import json


def to_json_string(my_obj):
    """A function that returns the JSON
    representation of an object (string)."""
    return (json.dumps(my_obj))
