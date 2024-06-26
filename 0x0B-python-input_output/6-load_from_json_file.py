#!/usr/bin/python3
""" A module defines a function that create an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)
