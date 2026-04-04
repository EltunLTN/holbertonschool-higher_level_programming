#!/usr/bin/python3
"""This module defines a Square class that represents a square shape."""


class Square:
    """This class defines a square by its size with comparison support."""

    def __init__(self, size=0):
        """Initialize a new Square instance with optional size.

        Args:
            size (number): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (number): The new size of the square.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if square is less than other based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if square is less than or equal to other based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if square is greater than other based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if square is greater than or equal to other based on area."""
        return self.area() >= other.area()
