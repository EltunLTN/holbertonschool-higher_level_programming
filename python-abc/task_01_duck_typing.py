#!/usr/bin/python3
"""This module defines an abstract class for shapes and a function to display their information."""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize the rectangle with a width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
# Testing the shape_info function with instances of Circle and Rectangle


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    print("Circle Information:")
    shape_info(circle)

    print("\nRectangle Information:")
    shape_info(rectangle)
