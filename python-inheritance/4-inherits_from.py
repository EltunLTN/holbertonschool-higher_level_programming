#!/usr/bin/python3
"""This module defines a function to check if an object is an instance
 of a class that inherited from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class
      that inherited from a_class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
