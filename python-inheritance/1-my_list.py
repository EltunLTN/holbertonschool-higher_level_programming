#!/usr/bin/python3
"""This module defines a MyList class that inherits from the
built-in list class and adds a method to print the list in sorted order."""


class MyList(list):

    """This class inherits from the built-in list class and adds a
    method to print the list in sorted order."""
    def print_sorted(self):
        print(sorted(self))
