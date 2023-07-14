#!/usr/bin/python3
""" define the class student """


class Student:
    """ represnt the class """

    def __init__(self, first_name, last_name, age):
        """ initialize the function to new student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function get dict """

        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}

        return self.__dict__

    def reload_from_json(self, json):
        """ function to replace all attr """
        for x, a in json.items():
            setattr(self, x, a)
