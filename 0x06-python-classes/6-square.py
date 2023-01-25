#!/usr/bin/python3
"""Define square class"""


class Square:
    """define square attributes"""

    def __init__(self, size=0):
        """Initialize a new square

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
        """set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints text to represent the square in # characters"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
