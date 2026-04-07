#!/usr/bin/python3
"""This module defines a function to check
 if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):

    """Return True if obj is an instance of
      a_class or its subclass, otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
