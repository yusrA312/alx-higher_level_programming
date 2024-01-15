#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv


class Base:
    """the hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """init."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to josn."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves to file."""
        if list_objs is not None:
            list_objs = [oX.to_dictionary() for oX in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fX:
            fX.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """from json."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create."""
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        elif cls.__name__ == "Square":
            n = cls(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """Load from file."""
        from os import path

        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as flad:
            return [cls.create(**d) for d in cls.from_json_string(flad.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv."""
        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[X.id, X.width, X.height, X.x, X.y]
                             for X in list_objs]
            else:
                list_objs = [[X.id, X.size, X.x, X.y] for X in list_objs]
        with open(
            "{}.csv".format(cls.__name__), "w", newline="", encoding="utf-8"
        ) as fsave:
            writer = csv.writer(fsave)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Loads to csv."""
        from models.rectangle import Rectangle
        from models.square import Square

        sQ = []
        with open(
            "{}.csv".format(cls.__name__), "r", newline="", encoding="utf-8"
        ) as Lf:
            reader = csv.reader(Lf)
            for w in reader:
                w = [int(r) for r in w]
                if cls is Rectangle:
                    dX = {
                        "id": w[0],
                        "width": w[1],
                        "height": w[2],
                        "x": w[3],
                        "y": w[4],
                    }
                else:
                    dX = {"id": w[0], "size": w[1], "x": w[2], "y": w[3]}
                sQ.append(cls.create(**dX))
        return sQ

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange

        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Random shap"""
        import turtle
        import time
        from random import randrange

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(4):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(45)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(60)
            turt.hideturtle()

        turtle.exitonclick()
