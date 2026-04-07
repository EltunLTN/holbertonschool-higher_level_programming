#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""This module defines a Square class that inherits from Rectangle."""


class Square(Rectangle):
    """This class defines a square."""
    def __init__(self, size):
        self.__size = size
        self.integer_validator(size, self.__size)

    def area(self):
        return self.__size*self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
