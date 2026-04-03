#!/usr/bin/python3
'''This module defines a Square class that represents a square shape.'''


class Square:
    '''This class defines a square by its properties and future behaviors.'''


    def __init__(self, size=0):
        self.__size = size


        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        elif self.__size < 0:
            raise ValueError("size must be >= 0")
