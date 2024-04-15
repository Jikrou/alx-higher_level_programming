#!/usr/bin/python3
""" Define a class checking function """


def is_same_class(obj, a_class):
    """ Check if an object is exactly an instance of the specified class.

    Args:
        obj (any): Object to check.
        a_class (type): The class to match to obj to.
    Return:
        If the obj is exactly an instance of the a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
