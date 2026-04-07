#!/usr/bin/python3
"""This module defines an empty class BaseGeometry."""


class BaseGeometry:
    """An empty class representing base geometry."""
    def area(self):
        """Calculate and return the area of the geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be a positive integer".format(name))
