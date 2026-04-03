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
    @property
    def size(self):
        """Get the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
