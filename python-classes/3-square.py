#!/usr/bin/python3
"""This module defines a Square class that represents a square shape."""


class Square:
    """This class defines a square by its size with validation."""

    def __init__(self, size=0):
        """Initialize a new Square instance with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        return self.__size**2
