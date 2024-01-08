#!/usr/bin/python3
"""Module for Rectangle class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A subclass."""

    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """What is the  area of square."""
        return self.__size**2

    def __str__(self):
        """Return  this square."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
