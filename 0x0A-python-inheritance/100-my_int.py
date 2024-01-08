#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    def __eq__(self, other):
        """!= is now =="""
        return int(self) != other

    def __ne__(self, other):
        """== is now !="""
        return int(self) == other
