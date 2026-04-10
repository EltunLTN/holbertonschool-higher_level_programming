# Background:
# Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The iter function, which returns an iterator object, provides the __next__ method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

# Objective:
# Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.

# Instructions:
# Setting up the CountedIterator Class:
# Define a class CountedIterator.
# In the constructor (__init__), initialize two attributes: the iterator object (using the iter function) and a counter to track the number of items iterated.
# Provide a method get_count to return the current value of the counter.
# Overriding the next Method:
# Within the CountedIterator class, override the __next__ method.
# In this method, increment the counter each time the __next__ method is called.
# Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the StopIteration exception.
# Testing:
# Instantiate a CountedIterator object using a list or another iterable.
# Iterate over items using a loop or manual calls to the __next__ method.
# Use the get_count method to retrieve and print the number of items that have been fetched.
# Hints:

# Remember that the __next__ method should raise a StopIteration exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
# You can initialize the iterator object in the CountedIterator constructor using: self.iterator = iter(some_iterable).
#!/usr/bin/python3
"""This module defines a CountedIterator class that extends the built-in iterator."""


class CountedIterator:
    """Class that extends the built-in iterator to count the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the current count of items iterated."""
        return self.count
