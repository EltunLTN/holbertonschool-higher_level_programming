#!/usr/bin/env python3
"""Module that defines shapes using abstract base classes and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        raise NotImplementedError()

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        raise NotImplementedError()


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius  # goes through the property setter

    @property
    def radius(self):
        """Return the radius."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set radius, always storing absolute value."""
        self.__radius = abs(value)

    def area(self):
        """Return the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = abs(value)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = abs(value)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
