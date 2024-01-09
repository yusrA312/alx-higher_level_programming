#!/usr/bin/python3
"""json module """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                my_dict[k] = v
        return my_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
