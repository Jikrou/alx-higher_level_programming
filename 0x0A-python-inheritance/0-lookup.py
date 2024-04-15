#!/usr/bin/pyhton3
""" A module that contain the lookup functon. """


def lookup(obj):
    """ A function that return the available attribute and
    methods of an objet.
    """
    return dir(obj)
