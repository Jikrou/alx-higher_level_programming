#!/usr/bin/python3
""" A module defines a read frrom file function."""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r") as file:
        content = file.read().rstrip()
        print(content)
