#!/usr/bin/python3
""" Define a class checking function """


def is_same_class(obj, a_class):
    """ Check if an object is exactly an instance of the specified class.

    Args:
        obj(any): object to check.
        a_class(type): the class to match to obj to.
    Return:
        if the obj is exactly an instance of the class - True,
        otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
