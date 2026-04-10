#!/usr/bin/python3
"""
Module that defines abstract Shape class and concrete implementations
using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Must be implemented by subclasses.
        """
        raise NotImplementedError()

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Must be implemented by subclasses.
        """
        raise NotImplementedError()


class Circle(Shape):
    """
    Circle class that represents a circle shape.
    """

    def __init__(self, radius):
        """
        Initialize a circle with a given radius.

        Args:
            radius (float): radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: area of the circle
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (float): width of the rectangle
            height (float): height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape.

    This function uses duck typing: it assumes the object
    has area() and perimeter() methods.

    Args:
        shape: any object with area() and perimeter() methods
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle:")
    shape_info(circle)  # Should print the area and perimeter of the circle

    print("\nRectangle:")
    shape_info(rectangle) 
