#!/usr/bin/python3
"""Modumkople for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The Width."""
        return self.__width

    @width.setter
    def width(self, value):
        self.v_inT("width", value, False)
        self.__width = value

    @property
    def height(self):
        """The Height."""
        return self.__height

    @height.setter
    def height(self, value):
        self.v_inT("height", value, False)
        self.__height = value

    @property
    def x(self):
        """THE x of rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.v_inT("x", value)
        self.__x = value

    @property
    def y(self):
        """THE y of rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.v_inT("y", value)
        self.__y = value

    def v_inT(self, name, value, eqL=True):
        """validating the value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eqL and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eqL and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """THE area."""
        return self.width * self.height

    def display(self):
        """Prints representation oF THE rectangle."""
        s = "\n" * self.y + (" " * self.x +
                             "#" * self.width + "\n") * self.height

        print(s, end="")

    def __str__(self):
        """THE info OF rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """THE updates instance."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """THE Updates instance."""

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """THE dictionary ."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
