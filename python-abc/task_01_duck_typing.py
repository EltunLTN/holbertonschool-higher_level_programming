#!/usr/bin/python3
"""This module demonstrates duck typing with shapes."""
from abc import ABC, abstractmethod
import math


# Abstract class
class Shape(ABC):
    """Abstract class representing a shape."""
    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


# Circle class
class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class
class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Duck typing function
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
