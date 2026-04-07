#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle."""
    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
