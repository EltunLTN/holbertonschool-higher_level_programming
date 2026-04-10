#!/usr/bin/python3
"""This module defines an abstract class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Class representing a dog, inheriting from Animal."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat, inheriting from Animal."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
