#!/usr/bin/python3
"""Define square class"""


class Square:
    """define square attributes"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size(int): this is the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__ * self.__size)
