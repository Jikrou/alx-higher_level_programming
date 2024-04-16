#!/usr/bin/python3
""" A module that defines a functions that write to a file."""


def write_file(filename="", text=""):
    """ A function that writes a string to a text file (UTF8)
    and returns the number of characters written. """
    with open(filename, "w") as file:
        num_char = file.write(text)
    return num_char
