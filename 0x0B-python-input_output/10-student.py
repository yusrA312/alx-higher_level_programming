#!/usr/bin/python3
""" json module """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student"""
        try:
            for atr in attrs:
                if type(atr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_d = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                my_d[k] = v
        return my_d
