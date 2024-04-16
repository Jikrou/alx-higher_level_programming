#!/usr/bin/python3
""" A module defines a function to append to a file."""


def append_write(filename="", text=""):
    """ A function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added."""
    with open(filename, "a") as file:
        num_char = file.write(text)
        return num_char
