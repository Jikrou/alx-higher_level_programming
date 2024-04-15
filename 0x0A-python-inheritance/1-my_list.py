#!/usr/bin/python3
""" A module that contain a class tha inherit from list """


class MyList(list):
    """ a class that inherit from list """

    def print_sorted(self):
        """ a methode that print a sorted list """
        self.print_sorted = sorted(self)
        print(self.print_sorted)
