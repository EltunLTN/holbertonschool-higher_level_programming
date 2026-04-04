#!/usr/bin/python3
"""This module defines a Node and SinglyLinkedList class."""


class Node:
    """This class defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance with data and next_node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with validation.

        Args:
            value (int): The new data of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation.

        Args:
            value (Node): The new next node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Return string representation of the linked list."""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """Insert a new Node in correct sorted position.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None:
            if value < current.next_node.data:
                break
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
