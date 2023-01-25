#!/usr/bin/python3
"""Define square class"""


class Square:
    """define square attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size(int): this is the size of the square.
        """
        self.size = size
        self.position = position

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

    @propoerty
    def position(self):
        """get position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
