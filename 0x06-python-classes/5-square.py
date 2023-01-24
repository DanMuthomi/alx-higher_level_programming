#!/usr/bin/python3
"""Define square class"""


class Square:
    """define square attributes"""

    def __init__(self, size=0):
        """Initializr a new square.

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
        """Set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return are of square"""
        return (self.__size * self.__size)

    def my_prints(self):
        """Prints text to represent the square in # characters"""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size is 0:
            print()
