#!/usr/bin/python3
"""This module defines a VerboseList class that extends the built-in list class
   and provides notifications for certain operations."""


class VerboseList(list):
    """A list that provides notifications when items are added or removed."""

    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """Remove the first occurrence of an item from the list and print a notification."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at a given index and print a notification."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
