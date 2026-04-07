#!/usr/bin/python3
"""This module defines a function to check if an object
is an exact instance of a class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return type(obj) is a_class
