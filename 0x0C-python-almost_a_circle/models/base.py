#!/usr/bin/python3
""" define the bass class """
import csv
import json
from os import path
import turtle


class Base:
    """ represnet the base class
    attribute:
         __nb_objects: number of instantiated base
     """
    __nb_objects = 0

    def __init__(self, id=None):
        """ inittializion new class bass"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ function to ruturn the python to json """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ func to store data in the file """
        filename = cls.__name__ + ".json"

        with open(filename, "w") as j_file:

            if list_objs is None:
                j_file.write("[]")
            else:
                list_ds = [x.to_dictionary() for x in list_objs]

                j_file.write(Base.to_json_string(list_ds))

    @staticmethod
    def from_json_string(json_string):
        """ func to return json into python """

        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ func to return the class from dictionary """
        if dictionary and dictionary != {}:

            if cls.__name__ == "Rectangle":
                new_r = cls(1, 1)
            else:
                new_r = cls(1)

            new_r.update(**dictionary)

            return new_r

    @classmethod
    def load_from_file(cls):
        """ func to return list from file of json string """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as j_file:
                list_ds = Base.from_json_string(j_file.read())

                return [cls.create(**di) for di in list_ds]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ func to return the csv """

        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csv_f:

            if list_objs is None or list_objs == []:
                csv_f.write("[]")

            else:
                if cls.__name__ == "Rectangle":

                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writ = csv.DictWriter(csv_f, fieldnames=fieldnames)

                for ob in list_objs:
                    writ.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ func to return the class from csv file """

        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as csv_f:

                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_ds = csv.DictReader(csv_f, fieldnames=fieldnames)
                list_ds = [dict([x, int(v)] for x, v in d.items())
                           for d in list_ds]

                return [cls.create(**di) for di in list_ds]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ function to draw the rectange and square """

        tur = turtle.Turtle()
        tur.screen.bgcolor("#b7312c")
        tur.pensize(3)
        tur.shape("turtle")
        tur.color("#ffffff")
        for rct in list_rectangles:

            tur.showturtle()
            tur.up()
            tur.goto(rct.x, rct.y)
            tur.down()

            for x in range(2):
                tur.forward(rct.width)
                tur.left(90)
                tur.forward(rct.height)
                tur.left(90)

            tur.hideturtle()

        tur.color("#b5e3d8")

        for sq in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sq.x, sq.y)
            tur.down()

            for x in range(2):
                tur.forward(sq.width)
                tur.left(90)
                tur.forward(sq.height)
                tur.left(90)

            tur.hideturtle()

        tur.exitonclick()
