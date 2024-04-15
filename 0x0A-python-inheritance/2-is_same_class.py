#!/usr/bin/python3
""" Define a class checking function """


def is_same_class(obj, a_class):
    """ Check if an object is exactly an instance of the specified class.

    Args:
        obj: object to check.
        a_class: the class to match to obj to.
    Return:
        True if the obj is exactly an instance of the class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
