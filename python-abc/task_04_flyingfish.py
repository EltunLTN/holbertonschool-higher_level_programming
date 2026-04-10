#!/usr/bin/python3
"""This module defines a FlyingFish class that
 demonstrates multiple inheritance."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message indicating the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message indicating the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish that inherits from both Fish Bird."""

    def fly(self):
        """Print a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a message indicating the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")

# Testing the FlyingFish class


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.fly()       # Output: The flying fish is soaring!
    flying_fish.swim()      # Output: The flying fish is swimming!
    flying_fish.habitat()   # The flying fish lives both in water and the sky!

    # Exploring method resolution order
    print(FlyingFish.mro())
