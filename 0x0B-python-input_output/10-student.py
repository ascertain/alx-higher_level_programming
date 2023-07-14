#!/usr/bin/python3
""" define the class student """


class Student:
    """ represnt the class student """

    def __init__(self, first_name, last_name, age):
        """ function to define the new student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function to define and get dict """

        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):

            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
