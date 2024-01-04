#!/usr/bin/python3
"""creating a module to handle a Rectangle object"""


class Rectangle:
    """Defining the Rectangle object"""

    def __init__(self, width=0, height=0):
        """The initialzation of a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """measure and  return the Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """measure and return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rectangle_str = ""
        if self.__width != 0 and self.__height != 0:
            rectangle_str += "\n".join("#" * self.__width for _ in range(self.__height))
        return rectangle_str
