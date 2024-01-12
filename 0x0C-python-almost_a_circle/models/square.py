#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inhrting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """init."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the Returns string."""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """the Size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __up(self, id=None, size=None, x=None, y=None):
        """to updates instance."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """to Updates instance."""
        if args:
            self.__up(*args)
        elif kwargs:
            self.__up(**kwargs)

    def to_dictionary(self):
        """THE dictionary."""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
